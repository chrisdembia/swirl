"""Tests LateXDoc."""

import os
import unittest

class TestBasics(unittest.TestCase):
    """Basic tests."""

    def tearDown(self):
        # Use os.remove or os.unlink. Issue is regular expressions.
        os.system('rm -f *.tex *.pdf')

    def test_basics(self):
        """Tests initialization, writing, typesetting."""

        doc = LateXDoc('testdoc')
        doc.nextIs('\documentclass[letterpaper]{article}')
        doc.nextIs('\begin{document}')
        doc.nextIs('Hello world!')
        doc.nextIs('\end{document}')
        doc.write('', doc.name)
        self.assertEquals(open(doc.name).readlines(),
                """\documentclass[letterpaper]{article}
                \begin{document}
                Hello world!
                \end{document}
                """)
        # Check that no pdf has been created.
        doc.write('', doc.name, typeset_pdf=True)
        # Check that a pdf is generated.


