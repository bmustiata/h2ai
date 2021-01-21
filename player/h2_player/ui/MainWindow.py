from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow
from mopyx import render, model, action

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

        self.icon_index_edit.editingFinished.connect(self.change_icon_index)
        self.sprite_start_spin.valueChanged.connect(self.change_start_frame)

    @action
    def change_icon_index(self):
        model.icon_index = int(self.icon_index_edit.text())

    @action
    def change_start_frame(self, value):
        model.sprite_index = int(self.sprite_start_spin.text())

    @render
    def render_icon(self) -> None:
        icon_path = f"/home/raptor/tmp/h2/dataset/{model.icon_index}/{model.sprite_index}.png"
        pixmap = QtGui.QPixmap(icon_path)

        offsets_file = f"/home/raptor/tmp/h2/dataset/{model.icon_index}/{model.sprite_index}.offsets"
        with open(offsets_file, "rt", encoding="utf-8") as f:
            sizes = f.readline()

        width, height, offset_x, offset_y = map(int, sizes.split(","))

        if width != pixmap.width():
            offset_x -= pixmap.width() - width

        if height != pixmap.height():
            offset_y -= pixmap.height() - height

        self.icon_label.setGeometry(
            128 + offset_x,
            256 + offset_y,
            pixmap.width(),
            pixmap.height()
        )

        self.icon_label.setPixmap(pixmap)  # FIXME
