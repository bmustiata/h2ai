import threading
import time
from typing import Dict

import PySide2
from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow
from mopyx import render, model, action
from mopyx_pyside2 import ui_thread

from h2_player.ui.generated.main_window import Ui_MainWindow


@model
class ActiveModel:
    def __init__(self) -> None:
        self.icon_index = 75
        self.sprite_index = 1
        self.sprite_start_index = 1
        self.sprite_end_index = 7
        self.fps = 5.0


model = ActiveModel()
running = True

last_render_time = 0


@ui_thread
@action
def update_sprite_index():
    global last_render_time

    # we don't update unless we are reaching the fps
    waiting_time = 1000 / model.fps
    current_time = time.time() * 1000

    if current_time - last_render_time < waiting_time:
        return

    last_render_time = current_time

    if model.sprite_index < model.sprite_start_index:
        model.sprite_index = model.sprite_start_index
        return

    model.sprite_index += 1

    if model.sprite_index > model.sprite_end_index:
        model.sprite_index = model.sprite_start_index
        return


class FrameUpdateThread(threading.Thread):
    def run(self) -> None:
        global running
        while running:
            update_sprite_index()
            time.sleep(0.001)


class RenderedSprite:
    def __init__(self, pixmap, offset_x: int, offset_y: int) -> None:
        self.pixmap = pixmap
        self.offset_x = offset_x
        self.offset_y = offset_y


cache: Dict[str, RenderedSprite] = dict()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.render_icon()

        self.icon_index_spinbox.valueChanged.connect(self.change_icon_index)
        self.sprite_start_spinbox.valueChanged.connect(self.change_start_frame)
        self.sprite_end_spinbox.valueChanged.connect(self.change_end_frame)
        self.fps_spinbox.valueChanged.connect(self.change_fps)

        FrameUpdateThread().start()

    def closeEvent(self, event: PySide2.QtGui.QCloseEvent):
        global running
        running = False

    @action
    def change_icon_index(self, value):
        model.icon_index = int(self.icon_index_spinbox.text())

    @action
    def change_start_frame(self, value):
        model.sprite_start_index = int(self.sprite_start_spinbox.text())
        model.sprite_index = int(self.sprite_start_spinbox.text())

    @action
    def change_end_frame(self, value):
        model.sprite_end_index = int(self.sprite_end_spinbox.text())

    @action
    def change_fps(self, value):
        model.fps = self.fps_spinbox.value()

    @render
    def render_icon(self) -> None:
        rendered_sprite = self.load_sprite()

        self.icon_label.setGeometry(
            128 + rendered_sprite.offset_x,
            256 + rendered_sprite.offset_y,
            rendered_sprite.pixmap.width(),
            rendered_sprite.pixmap.height()
        )

        self.icon_label.setPixmap(rendered_sprite.pixmap)

    def load_sprite(self) -> RenderedSprite:
        sprite_index = model.sprite_index

        # FIXME: cycle back to the first sprite
        if model.sprite_index == model.sprite_end_index + 1:
            sprite_index = model.sprite_start_index

        icon_path = f"/home/raptor/tmp/h2/dataset/{model.icon_index}/{sprite_index}.png"

        if icon_path in cache:
            return cache[icon_path]

        pixmap = QtGui.QPixmap(icon_path)

        offsets_file = f"/home/raptor/tmp/h2/dataset/{model.icon_index}/{sprite_index}.offsets"
        with open(offsets_file, "rt", encoding="utf-8") as f:
            sizes = f.readline()

        width, height, offset_x, offset_y = map(int, sizes.split(","))

        if width != pixmap.width():
            offset_x -= pixmap.width() - width

        if height != pixmap.height():
            offset_y -= pixmap.height() - height

        rendered_pixmap = RenderedSprite(
            pixmap=pixmap,
            offset_x=offset_x,
            offset_y=offset_y,
        )

        cache[icon_path] = rendered_pixmap

        return rendered_pixmap