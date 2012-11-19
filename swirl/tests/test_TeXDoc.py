"""Tests LateXDoc."""

import os
import unittest

import swirl

class TestBasics(unittest.TestCase):
    """Basic tests."""

    def tearDown(self):
        # Use os.remove or os.unlink. Issue is regular expressions.
        os.system('rm -f *.aux *.log *.tex *.pdf')

    def test_basics(self):
        """Tests initialization, writing, typesetting."""

        doc = swirl.LaTeXDoc('testdoc')
        doc.nextIs('\\documentclass[letterpaper]{article}')
        doc.nextIs('\\begin{document}')
        doc.nextIs('Hello world!')
        doc.nextIs('\\end{document}')
        doc.write('', doc.name)
        self.assertTrue(os.path.isfile(doc.name + '.tex'))
        self.assertEquals(open(doc.name + '.tex').readlines(),
                ["\\documentclass[letterpaper]{article}\n",
                "\\begin{document}\n",
                "Hello world!\n",
                "\\end{document}\n"])
        # Check that no pdf has been created.
        self.assertFalse(os.path.isfile(doc.name + '.pdf'))
        doc.write('', doc.name, typeset_pdf=True)
        # Check that a pdf is generated.
        self.assertTrue(os.path.isfile(doc.name + '.pdf'))

    def test_foreign_path(self):
        """Tests writing/typesetting to paths other than the cwd."""
        # TODO doens't work currently because of how typeset is implemented.

    def test_default_preamble(self):
        """Tests that the default preamble is added to the file correctly."""
        # TODO


if __name__ == '__main__':
    unittest.main()
