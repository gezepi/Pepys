from PySide2 import QtWidgets, QtGui, QtCore
import regex
from MarkdownRegex import regexPatterns


class MarkdownSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    """Syntax highlighter for markdown file"""

    # Plaintext format options and regex
    text_formatter = QtGui.QTextCharFormat()
    text_formatter.setFontItalic(False)
    text_formatter.setFontWeight(QtGui.QFont.Normal)
    text_formatter.setFontStrikeOut(False)

    # Header format options and regex
    atx_header_pattern = regex.compile(regexPatterns['ATX_HEADER'], regex.MULTILINE)
    setext_header_pattern = regex.compile(regexPatterns['SETEXT_HEADER'], regex.MULTILINE)
    setext_underline_pattern = regex.compile(regexPatterns['SETEXT_UNDERLINE'], regex.MULTILINE)
    header_formatter = QtGui.QTextCharFormat()
    header_formatter.setFontWeight(QtGui.QFont.Bold)

    # Emphasis format options and regex
    emphasis_pattern = regex.compile(regexPatterns['EMPHASIS'], regex.MULTILINE)
    emphasis_formatter = QtGui.QTextCharFormat()
    emphasis_formatter.setFontItalic(True)

    # Strong emphasis format options and regex
    strong_emphasis_pattern = regex.compile(regexPatterns['STRONG_EMPHASIS'], regex.MULTILINE)
    strong_emphasis_formatter = QtGui.QTextCharFormat()
    strong_emphasis_formatter.setFontWeight(QtGui.QFont.Bold)
    strong_emphasis_formatter.setFontItalic(False)

    # Very strong emphasis options and regex
    very_strong_emphasis_pattern = regex.compile(regexPatterns['VERY_STRONG_EMPHASIS'], regex.MULTILINE)
    very_strong_emphasis_formatter = QtGui.QTextCharFormat()
    very_strong_emphasis_formatter.setFontWeight(QtGui.QFont.Bold)
    very_strong_emphasis_formatter.setFontItalic(True)

    # Strikethrough emphasis options and regex
    strikethrough_pattern = regex.compile(regexPatterns['STRIKETHROUGH'], regex.MULTILINE)
    strikethrough_formatter = QtGui.QTextCharFormat()
    strikethrough_formatter.setFontStrikeOut(True)

    def __init__(self, text_edit:QtWidgets.QTextEdit) -> None:
        """Initialise syntax highlighter.

        :param text_edit: QTextEdit to apply formatting to
        """
        super().__init__(text_edit)

    def highlightBlock(self, text:str) -> None:
        """Overrides QSyntaxHighlighter method to provide custom formatting"""

        formatter = QtGui.QTextCharFormat()

        # Setext header match and format
        for match in regex.finditer(self.setext_header_pattern, text + "\n" + self.currentBlock().next().text()):
            formatter.setFontWeight(QtGui.QFont.Bold)
            self.setFormat(match.start(), len(match.group()), formatter)

        # Setext underline match and format
        for match in regex.finditer(self.setext_underline_pattern, text):
            formatter.setFontWeight(QtGui.QFont.Bold)
            self.setFormat(match.start(), len(match.group()), formatter)

        # Atx header match and format
        for match in regex.finditer(self.atx_header_pattern, text):
            formatter.setFontWeight(QtGui.QFont.Bold)
            self.setFormat(match.start(), len(match.group()), formatter)

        # Emphasis match and format
        for match in regex.finditer(self.emphasis_pattern, text):
            formatter.setFontItalic(True)
            self.setFormat(match.start(), len(match.group()), formatter)

        # Strong emphasis match and format
        for match in regex.finditer(self.strong_emphasis_pattern, text):
            formatter.setFontWeight(QtGui.QFont.Bold)
            self.setFormat(match.start(), len(match.group()), formatter)

        # Very strong emphasis match and format
        for match in regex.finditer(self.very_strong_emphasis_pattern, text):
            formatter.setFontItalic(True)
            formatter.setFontWeight(QtGui.QFont.Bold)
            self.setFormat(match.start(), len(match.group()), formatter)

        # Strikethrough match and format
        for match in regex.finditer(self.strikethrough_pattern, text):
            formatter.setFontStrikeOut(True)
            self.setFormat(match.start(), len(match.group()), formatter)





