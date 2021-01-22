from mopyx import model


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
