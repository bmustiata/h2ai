import PySide2
from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow
from mopyx import render, action

from h2_player import animation
from h2_player.ui.generated.main_window import Ui_MainWindow
from h2_player.ui.model import model as uimodel
from h2_player.ui import model


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.render_icon()
        self.render_active_frame()

        self.icon_index_spinbox.valueChanged.connect(self.change_icon_index)
        self.sprite_start_spinbox.valueChanged.connect(self.change_start_frame)
        self.sprite_end_spinbox.valueChanged.connect(self.change_end_frame)
        self.fps_spinbox.valueChanged.connect(self.change_fps)

    def closeEvents(self, event: PySide2.QtGui.QCloseEvent):
        model.running = False

    @action
    def change_icon_index(self, value):
        uimodel.icon_index = int(self.icon_index_spinbox.text())

    @action
    def change_start_frame(self, value):
        uimodel.sprite_start_index = int(self.sprite_start_spinbox.text())
        uimodel.sprite_index = int(self.sprite_start_spinbox.text())

    @action
    def change_end_frame(self, value):
        uimodel.sprite_end_index = int(self.sprite_end_spinbox.text())

    @action
    def change_fps(self, value):
        uimodel.fps = self.fps_spinbox.value()

    @render
    def render_icon(self) -> None:
        rendered_sprite = animation.load_sprite()

        self.icon_label.setGeometry(
            128 + rendered_sprite.offset_x,
            256 + rendered_sprite.offset_y,
            rendered_sprite.pixmap.width(),
            rendered_sprite.pixmap.height()
        )

        self.icon_label.setPixmap(rendered_sprite.pixmap)

    @render
    def render_active_frame(self) -> None:
        self.current_frame_label.setText(f"{uimodel.sprite_index}")
