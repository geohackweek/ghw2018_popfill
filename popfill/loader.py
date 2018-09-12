from collections import namedtuple

import numpy as np
import rasterio

NPRaster = namedtuple('NPRaster', ['data', 'profile'])

class PopulationLoader(object):

    def read_file(this, file_path):
        with rasterio.open(file_path) as mask:
            profile = mask.profile.copy()
            data = mask.read(1)
        return profile, data

    def load(this, mask_path, pop_path):
        mask_profile, mask_np = this.read_file(mask_path)
        mask_np[mask_np == mask_profile['nodata']] = 0

        mask_np = mask_np.astype(bool)
        mask = NPRaster(mask_np, mask_profile)

        pop_profile, pop_np = this.read_file(pop_path)
        pop_np[pop_np == pop_profile['nodata']] = np.NaN;
        pop = NPRaster(pop_np, pop_profile)

        return mask, pop
