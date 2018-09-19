import subprocess
import os

class Error (Exception): pass


class Ipynb_to_tex_converter:
    def __init__(self,
        infile,
        outfile,
        fix_terminal_style=True,
        notitle=True,
        parskip=True,
        font_size=11,
        execute_notebook=True,
        date=None
    ):
        self.infile = infile
        self.outfile = outfile
        self.fix_terminal_style = fix_terminal_style
        self.parskip = parskip
        self.font_size = font_size
        self.notitle = notitle
        self.date = date
        self.execute_notebook = execute_notebook

        if not os.path.exists(self.infile):
            raise Error('Input file not found "' + self.infile + '". Cannot continue')


    def _nbconvert_to_tex(self, infile, outfile):
        # on xenial, the --output foo puts foo in the same directory
        # as the infile, so use absolute path
        outfile = os.path.abspath(outfile)

        cmd = 'jupyter nbconvert'
        if self.execute_notebook:
            cmd += ' --execute'

        cmd += ' --to latex --output ' + outfile + ' ' + infile

        try:
            subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as error:
            errors = error.output.decode()
            raise Error('Error running\n' + cmd + '\nErrors are:\n' + error)


    #def _fix_tex_verbatim_tabs(self, lines):
    #    for i in range(len(lines)):
    #        if lines[i] == r'''    \begin{Verbatim}[commandchars=\\\{\}]''':
    #            lines[i] = r'''    \begin{Verbatim}[obeytabs,commandchars=\\\{\}]'''

    def _remove_useless_first_lines(self, lines):
        while len(lines) and not lines[0].startswith(r'''\documentclass'''):
            lines.pop(0)


    #def _fix_figures(self, lines):
    #    for i in range(len(lines)):
    #        if lines[i].startswith(r'''\begin{figure}'''):
    #           assert lines[i+2].startswith(r'''\includegraphics''')
    #           assert lines[i+3].startswith(r'''\caption''')
    #           assert lines[i+4] == r'''\end{figure}'''
    #           graphics_string = lines[i+3].split('{')[-1][:-1]
    #           lines[i] = ''
    #           lines[i+1] = r'''\begin{center}'''
    #           lines[i+2] = lines[i+2].split('{')[-1][:-1]
    #           lines[i+2] = r'''\includegraphics[''' + graphics_string + ']{' + lines[i+2] + '}'
    #           lines[i+3] = r'''\end{center}'''
    #           lines[i+4] = ''

    def _set_figure_maxheight(self, lines):
        for i in range(len(lines)):
            if "\\renewcommand{\includegraphics}" in lines[i]:
                lines[i] = str("\\renewcommand{\includegraphics}[1]{\Oldincludegraphics[width=.8\maxwidth, height=.55\\textheight, keepaspectratio]{#1}}")

    def _fix_figure_position(self, lines):
        for i in range(len(lines)):
            if "\\begin{figure}" in lines[i]:
                lines[i] += str("[!h]")

    def _fix_table_style(self, lines):
        lines.insert(1, r'''\renewcommand{\arraystretch}{1.5} % Default value: 1''')
        for i in range(len(lines)):
            longtable_rules = ['toprule', 'midrule', 'bottomrule']
            if any(s in lines[i] for s in longtable_rules):
                lines[i] = "\\hline"   

    def _set_bold_caption_style(self, lines):
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        for i in range(len(lines)):
            if "\\captionsetup" in lines[i]:
                pp.pprint(lines[i])
                lines[i] = str("    \\captionsetup{labelformat=nolabel, textfont=bf}")
                pp.pprint(lines[i])

    def _fix_terminal_style(self, lines):
        lines.insert(1, r'''\usepackage{listings}
\lstset{
basicstyle=\small\ttfamily,
tabsize=8,
columns=flexible,
breaklines=true,
frame=tb,
rulecolor=\color[rgb]{0.8,0.8,0.7},
backgroundcolor=\color[rgb]{1,1,0.91},
postbreak=\raisebox{0ex}[0ex][0ex]{\ensuremath{\color{red}\hookrightarrow\space}}
}
\usepackage{fontawesome}


\usepackage{mdframed}
\newmdenv[
  backgroundcolor=gray,
  fontcolor=white,
  nobreak=true,
]{terminalinput}


''')

        to_replace = {'\#': '#', '\$': '$', '\_': '_', r'''{\ldots}''': '...'}
        in_lstlisting = False
        in_verbatim = False

        for i in range(len(lines)):
            if lines[i] == r'''    \begin{Verbatim}[commandchars=\\\{\}]''':
                if lines[i+1].startswith(r'''{\color{incolor}In '''):
                    lines[i] = '\n'.join([r'''\begin{terminalinput}''', r'''\begin{Verbatim}[commandchars=\\\{\}]'''])
                    cmd = lines[i+1].split(' ', maxsplit=2)[-1]
                    if cmd.startswith("}]:}"):
                        cmd = cmd[len("}]:}"):]
                    lines[i+1] = r'''\llap{\color{black}\LARGE\faKeyboardO\hspace{1em}}''' + cmd
                    import pprint
                    pp = pprint.PrettyPrinter(indent=4)
                    pp.pprint(cmd)
                    in_verbatim = True
                    continue
                else:
                    lines[i] = r'''    \begin{lstlisting}'''
                    in_lstlisting = True
                    continue

            if in_lstlisting:
                if lines[i] == r'''    \end{Verbatim}''':
                    lines[i] = r'''    \end{lstlisting}'''
                    in_lstlisting = False

                    # sometimes there is no output, which would leave a small empty box
                    if lines[i-2] == r'''    \begin{lstlisting}''' and lines[i-1] == '':
                        lines[i-1] = '(no output)'
                else:
                    for key, val in to_replace.items():
                        lines[i] = lines[i].replace(key, val)
            if in_verbatim and lines[i] == '\end{Verbatim}':
                lines[i] += '\n' + r'''\end{terminalinput}'''
                in_verbatim = False





    def _remove_title(self, lines):
        for i in range(len(lines)):
            if lines[i] == r'''    \maketitle''':
                lines.pop(i)
                break

    def _set_section_heading_style(self, lines):
        lines.insert(1, r'''\usepackage{sectsty}
\allsectionsfont{\color{blue}\fontfamily{lmss}\selectfont}
\usepackage{fontspec}
\setmainfont{XCharter}
''')


    def _remove_syntax_highlighting(self, lines):
        for i in range(len(lines)):
            if r'''\begin{document}''' in lines[i]:
                lines.insert(i, r'''\renewcommand{\PY}[2]{{#2}}''')
                return


    def _fix_image_files(self, lines):
        pass

    # because emph might end up being underline, not italics
    def _change_emph_to_italics(self, lines):
        for i in range(len(lines)):
            lines[i] = lines[i].replace(r'''\emph{''', r'''\textit{''')


    def run(self):
        self._nbconvert_to_tex(self.infile, self.outfile)

        with open(self.outfile) as f:
            lines = [line.rstrip() for line in f.readlines()]

        self._remove_useless_first_lines(lines)
        lines[0] = r'''\documentclass[''' + str(self.font_size) + 'pt]{article}'''

        if self.parskip:
            lines.insert(1, r'''\usepackage{parskip}''' + '\n')

        if self.fix_terminal_style:
            self._fix_terminal_style(lines)

        if self.notitle:
            self._remove_title(lines)

        self._remove_syntax_highlighting(lines)

        self._set_section_heading_style(lines)
        self._set_figure_maxheight(lines)
        self._fix_figure_position(lines)
        self._fix_image_files(lines)
        self._fix_table_style(lines)
        self._set_bold_caption_style(lines)
        self._change_emph_to_italics(lines)

        with open(self.outfile, 'w') as f:
            for line in lines:
                print(line, file=f)


class Tex_catter:
    def __init__(self, infiles, outfile):
        self.infiles = infiles
        self.outfile = outfile


        for filename in self.infiles:
            if not os.path.exists(filename):
                raise Error('File not found "' + filename + '". Cannot continue')


    def _get_tex_header(self, infile):
        '''Gets the header part of tex file (Eveything before begin{document}).
           Returns a list of the lines (wihtout trailing newline characters)'''
        lines = []
        with open(infile) as f:
            for line in f:
                if r'''\begin{document}''' in line:
                    return lines

                lines.append(line.rstrip())

        raise Error(r'''Error! \begin{document} not found in file "''' + infile + '". Cannot continue')


    def _add_fancy_headers(self, lines):
        '''Adds headers/footers to the preamble, using fancyhdr package'''
        lines.extend([
            r'''\usepackage{fancyhdr}''',
            r'''\pagestyle{fancy}''',
            r'''\rhead{\color{gray}\sf\small\rightmark}''',
            r'''\lhead{\nouppercase{\color{gray}\sf\small\leftmark}}''',
            r'''\cfoot{\color{gray}\sf\thepage}''',
            r'''\renewcommand{\footrulewidth}{1pt}''',
        ])


    def _get_tex_body(self, infile):
        '''Gets the body part of tex file (eveything between begin and end{document}).
           Returns a list of the lines (wihtout trailing newline characters)'''
        lines = []
        in_body = False

        with open(infile) as f:
            for line in f:
                if r'''\begin{document}''' in line:
                    in_body = True
                    continue
                elif r'''\end{document}''' in line:
                    break

                if in_body:
                    lines.append(line.rstrip())

        assert len(lines) >= 2
        return lines


    def _write_lines_to_file(self, lines, f):
        for line in lines:
            print(line, file=f)


    def run(self):
        with open(self.outfile, 'w') as f:
            lines = self._get_tex_header(self.infiles[0])
            self._add_fancy_headers(lines)
            self._write_lines_to_file(lines, f)
            print(r'''\begin{document}''', file=f)

            for filename in self.infiles:
                lines = self._get_tex_body(filename)
                self._write_lines_to_file(lines, f)
                if filename != self.infiles[-1]:
                    print(r'''\newpage''', file=f)

            print(r'''\end{document}''', file=f)

