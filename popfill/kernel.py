import numpy as np

class Basic(object):

    def __init__(this, mask, counts):
        this._mask = mask
        this._counts = counts

    def _dst_mask(this):
        return this._mask

    def _src_mask(this):
        return this._counts == this._counts

    def to_remove(this):
        return this._src_mask() & ~this._dst_mask()

    def to_add(this):
        return this._dst_mask() & ~this._src_mask()

    def fill(this):
        to_remove = this.to_remove()
        to_add = this.to_add()

        volume_to_move = this._counts[to_remove].sum()

        new_counts = this._counts.copy()
        new_counts[to_add] += volume_to_move / np.sum(to_add)
        new_counts[to_remove] = 0

        return new_counts
