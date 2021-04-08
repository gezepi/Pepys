from __future__ import annotations
from PySide2 import QtCore, QtWidgets, QtGui
from ColorParser import *
import AbstractPane
import typing
if typing.TYPE_CHECKING:
    from AppContext import AppContext

import regex


class ViewPane(QtWidgets.QTextBrowser):
    """Pane for viewing rendered markdown in."""

    def __init__(self, ctx: AppContext) -> None:
        """Initialise ViewPane.

        :param ctx: current ApplicationContext
        """

        super().__init__()
        self.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)
        #self.setStyleSheet(parse_stylesheet(ctx.get_resource("PaneStyle.qss"), ctx.get_resource("colors.json"), ctx.get_resource("config.json")))
        self.setVerticalScrollBarPolicy(self.verticalScrollBarPolicy().ScrollBarAlwaysOn)

        self.setOpenExternalLinks(True)


        self.setReadOnly(True)

        #stylesheet = parse_stylesheet(ctx.get_resource("ViewPaneStyle.qss"), ctx.get_resource("colors.json"), ctx.get_resource("config.json"))

        #self.setStyleSheet(self.styleSheet() + stylesheet)

        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.horizontalScrollBar().setEnabled(False)
        self.setTextInteractionFlags(QtGui.Qt.TextBrowserInteraction)

    def update_size(self, new_frame_width: int) -> None:

        # Increase width of scroll bar left border to create a margin 25% width of the main window.
        margin_scale = 1 / 4
        scroll_bar_width = 4
        self.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            f"width: {new_frame_width * margin_scale + scroll_bar_width};"
            f"border-left-width: {str(new_frame_width * margin_scale - scroll_bar_width)}px ;"
            "}")

        # Increase left border of the QTextEdit pane to create a left margin 25% width of the main window
        self.setStyleSheet(self.styleSheet() +
                           "QTextEdit { "
                           f"border-left-width: {new_frame_width * margin_scale} px;"
                           "}")

        # TODO: Make resizing large images less laggy
        html = regex.sub(r'(?<=<img[^>]*)(width="[\d.]+")', f'width="{self.width() * 0.5}" ',
                         self.toHtml())
        self.setHtml(html)

        # TODO: Make resizing large images less laggy
        html = regex.sub(r'(?<=<img[^>]*)(width="[\d.]+")', f'width="{self.width() * 0.5}" ',
                         self.toHtml())
        self.setHtml(html)

    def enterEvent(self, event: QtCore.QEvent) -> None:
        """"Override base QTextEdit method, called when mouse is over TextEdit

        :param event: the QEvent that caused the invocation
        """

        self.verticalScrollBar().setVisible(True)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        """"Override base QTextEdit method, called when mouse leaves TextEdit

        :param event: the QEvent that caused the invocation
        """

        self.verticalScrollBar().setVisible(False)





