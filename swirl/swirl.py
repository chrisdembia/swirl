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

    def nextIs(self, line):
        self._lines += [line]

    def write(self, path, filename, typeset_pdf=False):
        """Writes the stored file to path+filename.

        Parameters
        ----------
        path : str
            The path where the file is located.
        filename : str
            The name of the .TEX file, without the .TEX extension.
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


class LaTeXArticle(object):
    """Represents a LaTeX document of class article."""

    def __init__(self, name):
        raise Exception("TODO")

