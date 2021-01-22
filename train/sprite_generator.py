import numpy as np
from PIL import Image
from numpy import asarray
from keras.utils import Sequence


class MultipleInputGenerator(Sequence):
    """
    Generates frames
    """

    def __len__(self):
        return 1

    def __getitem__(self, index):
        X1_batch = load_frame_as_numpy_array(icon_index=215, sprite_index=1)
        X2_batch = load_frame_as_numpy_array(icon_index=215, sprite_index=3)
        Y_batch = load_frame_as_numpy_array(icon_index=215, sprite_index=2)

        X_batch = [X1_batch, X2_batch]

        return X_batch, Y_batch


def load_frame_as_numpy_array(*, icon_index: int, sprite_index: int):
    frame1 = Image.open(f"/home/raptor/tmp/h2/dataset/{icon_index}/{sprite_index}.png")
    frame1_data = np.asarray(frame1)
    f1 = np.zeros((128, 128, 4))
    f1[:frame1_data.shape[0], :frame1_data.shape[1]] = frame1_data / 255.0

    return f1


def test_image_load():
    load_frame_as_numpy_array(icon_index=215, sprite_index=1)


if __name__ == '__main__':
    test_image_load()
