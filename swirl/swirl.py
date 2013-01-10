"""Contains a class that represents a LaTeX document.

.. moduleauthor:: Chris Dembia <cld72@cornell.edu>

"""

import os

class LaTeXDoc(object):
    """Represents a LaTeX document. Allows writing and compilation."""

    ext = '.tex'

    def __init__(self, name):
        """Loading, writing, and typesetting are done by different methods.

        Parameters
        ----------
        name : str
            Name of the entity.

        """
        # Cheriton's NamedInterface: every entity has a name.
        self._name = name
        self._lines = []

    @property
    def name(self): return self._name

    def load(self, path, filename):
        """Not implemented."""
        raise Exception("TODO")

    def next_is(self, line):
        self._lines += [line]

    def write(self, path, filename, typeset_pdf=False):
        """Writes the stored file to path+filename.

        Parameters
        ----------
        path : str
            The path where the file is located.
        filename : str, optional
            The name of the .TEX file, without the .TEX extension. Default is
            the object's name (passed in by the constructor).
        typeset_pdf : boolean
            Typeset the document as a .PDF.

        """
        if len(path) == 0: path = '.'
        path = path if path[len(path)-1] == os.sep else path + os.sep
        fid = open(path + filename + self.ext, 'w')
        for line in self._lines:
            fid.write(line + '\n')
        fid.close()
        if typeset_pdf: self.typeset(path, filename, 'pdf')

    def typeset(self, path, filename, outtype='pdf'):
        """Typesets the document.

        Parameters
        ----------
        path : str
            The path where the output should be placed.
        filename : str
            The name of the file to typeset to.
        outtype : str
            A string identifying the type of file to typseset to.

        """
        if outtype == 'pdf':
            os.system('rubber --pdf {0}'.format(path + filename + self.ext))
        else:
            raise Exception("Unsupported outtype.")

    def section(self, heading):
        """Create a new section.

        Parameter
        ---------
        heading : str
            The name/heading of this new section.

        """
        self.next_is("\\section{%s}" % heading)

    def subsection(self, heading):
        """Create a new subsection.

        Parameter
        ---------
        heading : str
            The name/heading of this new subsection.

        """
        self.next_is("\\subsection{%s}" % heading)

    def subsubsection(self, heading):
        """Create a new subsubsection.

        Parameter
        ---------
        heading : str
            The name/heading of this new subsubsection.

        """
        self.next_is("\\subsubsection{%s}" % heading)


class LaTeXArticle(object):
    """Represents a LaTeX document of class article."""

    def __init__(self, name):
        raise Exception("TODO")


class FigureReport(LaTeXDoc):
    """A document whose contents is primarily multiple pgfplots. A generic
    preamble is provided, and a simple plot method is provided."""

    def __init__(self, name):
        """Loading, writing, and typesetting are done by different methods.

        Parameters
        ----------
        name : str
            Name of the entity.

        """
        super(FigureReport, self).__init__(name)
        self.next_is("""
        \\documentclass[letterpaper]{article}
        \\usepackage[left=0.5in,right=0.5in,top=0.5in,bottom=0.5in]{geometry}
        \\usepackage{pgfplots}
        \\usepackage{times}
        """)

    def front_matter(self, title, author):
        """Adds title page and table of contents pages.

        Parameters
        ----------
        title : str
            Title of document.
        author : str
            List of authors.

        """
        self.next_is("""
        \\begin{document}
        \\title{%s}
        \\author{%s}
        \\date{\\today}
        \\maketitle
        \\newpage
        \\tableofcontents
        \\newpage
        """ % (title, author))

    def simple_data_plot(self, options, legend_entries, x, y):
        """Creates a basic pgfplot in a tikzpicture. Any axis options can be
        provided, and any number of series can be plotted.

        Parameters
        ----------
        options : str
            The options provided to the axis.
        legend_entries : list of str's
            The names of the series in the plot.
        x : list of lists of floats
            Independent variable for each series.
        y : list of lists of floats
            Dependent variable for each series.

        """
        self.next_is("\\begin{tikzpicture}")
        self.next_is("\\begin{axis}[%s]" % options)
        # All plots.
        for i_series in range(len(x)):
            self.next_is("\\addplot+[very thick] coordinates {")
            for i_entry in range(len(x[i_series])):
                self.next_is("({0}, {1})".format(
                    x[i_series][i_entry], y[i_series][i_entry]))
            self.next_is("};")
        # Legend.
        self.next_is("\\legend{%s" % legend_entries[0])
        for i_entry in range(1, len(legend_entries)):
            self.next_is(",{0}".format(legend_entries[i_entry]))
        self.next_is("};")
        self.next_is("\\end{axis}")
        self.next_is("\\end{tikzpicture}")
