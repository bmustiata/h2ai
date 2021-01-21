from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow
from mopyx import render, model

from h2_player.ui.generated.main_window import Ui_MainWindow


@model
class ActiveModel:
    def __init__(self) -> None:
        self.icon_index = 75
        self.sprite_index = 1


model = ActiveModel()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.render_icon()

    @render
    def render_icon(self) -> None:
        icon_path = f"/home/raptor/tmp/h2/dataset/{model.icon_index}/{model.sprite_index}.png"
        pixmap = QtGui.QPixmap(icon_path)

        self.icon_label.setGeometry(
            128,
            128,
            pixmap.width(),
            pixmap.height()
        )

        self.icon_label.setPixmap(pixmap)  # FIXME
