import threading
import time
from typing import Dict

from PySide2 import QtGui
from mopyx import action
from mopyx_pyside2 import ui_thread

from h2_player.ui.model import model as uimodel
from h2_player.ui import model


class RenderedSprite:
    def __init__(self, pixmap, offset_x: int, offset_y: int) -> None:
        self.pixmap = pixmap
        self.offset_x = offset_x
        self.offset_y = offset_y


cache: Dict[str, RenderedSprite] = dict()


@ui_thread
@action
def update_sprite_index():
    # we don't update unless we are reaching the fps
    waiting_time = 1000 / uimodel.fps
    current_time = time.time() * 1000

    if current_time - model.last_render_time < waiting_time:
        return

    model.last_render_time = current_time

    if uimodel.sprite_index < uimodel.sprite_start_index:
        uimodel.sprite_index = uimodel.sprite_start_index
        return

    uimodel.sprite_index += 1

    if uimodel.sprite_index > uimodel.sprite_end_index:
        uimodel.sprite_index = uimodel.sprite_start_index
        return


class FrameUpdateThread(threading.Thread):
    def run(self) -> None:
        while model.running:
            update_sprite_index()
            time.sleep(0.001)


def load_sprite() -> RenderedSprite:
    sprite_index = uimodel.sprite_index

    # FIXME: cycle back to the first sprite
    if uimodel.sprite_index == uimodel.sprite_end_index + 1:
        sprite_index = uimodel.sprite_start_index

    icon_path = f"/home/raptor/tmp/h2/dataset/{uimodel.icon_index}/{sprite_index}.png"

    if icon_path in cache:
        return cache[icon_path]

    pixmap = QtGui.QPixmap(icon_path)

    offsets_file = f"/home/raptor/tmp/h2/dataset/{uimodel.icon_index}/{sprite_index}.offsets"
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