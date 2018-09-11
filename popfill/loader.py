import numpy as np

class DummyLoader(object):
    def __init__(this, size_x, size_y):
        this._size_x = size_x
        this._size_y = size_y

    def load(this, _=""):
        mask = np.random.randint(0, 2, (this._size_x, this._size_y))
        counts = np.random.randint(0, 100, (this._size_x, this._size_y))
        return mask, counts
