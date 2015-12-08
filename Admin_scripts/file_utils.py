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
        date=None
    ):
        self.infile = infile
        self.outfile = outfile
        self.fix_terminal_style = fix_terminal_style
        self.parskip = parskip 
        self.font_size = font_size
        self.notitle = notitle
        self.date = date

        if not os.path.exists(self.infile):
            raise Error('Input file not found "' + self.infile + '". Cannot continue')


    def _nbconvert_to_tex(self, infile, outfile):
        cmd = 'jupyter nbconvert --execute --to latex --output ' + outfile + ' ' + infile

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
''')

        to_replace = {'\#': '#', '\$': '$', '\_': '_'}
        in_lstlisting = False

        for i in range(len(lines)):
            if lines[i] == r'''    \begin{Verbatim}[commandchars=\\\{\}]''':
                if lines[i+1].startswith(r'''{\color{incolor}In '''):
                    lines[i] = r'''    \vspace{0.5em}\begin{Verbatim}[commandchars=\\\{\}]'''
                    cmd = lines[i+1].split(' ', maxsplit=2)[-1]
                    lines[i+1] = r'''\llap{\LARGE\faKeyboardO }\colorbox{gray}{\color{white}''' + cmd + '}'
                else:
                    lines[i] = r'''    \begin{lstlisting}'''
                    in_lstlisting = True
                    continue

            if in_lstlisting:
                if lines[i] == r'''    \end{Verbatim}''':
                    lines[i] = r'''    \end{lstlisting}'''
                    in_lstlisting = False
                else:
                    for key, val in to_replace.items():
                        lines[i] = lines[i].replace(key, val)
                   



    def _remove_title(self, lines):
        for i in range(len(lines)):
            if lines[i] == r'''    \maketitle''':
                lines.pop(i)
                break

    def _set_section_heading_style(self, lines):
        lines.insert(1, r'''\usepackage{sectsty}
\allsectionsfont{\color{blue}\fontfamily{lmss}\selectfont}
\usepackage{charter}
''')


    def _remove_syntax_highlighting(self, lines):
        for i in range(len(lines)):
            if r'''\begin{document}''' in lines[i]:
                lines.insert(i, r'''\renewcommand{\PY}[2]{{#2}}''')
                return


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

