
# coding: utf-8

import rasterio
import numpy as np
'''A function to read raster data for mask and counts and convert to Numpy array'''

def raster2np(mask_path, pop_path):
    with rasterio.open(mask_path) as mask:

        mask_profile = mask.profile.copy()
        mask_np = mask.read(1)
    mask_np[mask_np == mask.nodata] = 0
    mask_np = mask_np.astype(bool)

    with rasterio.open(pop_path) as pop:
        pop_profile = pop.profile.copy()
        pop_np = pop.read(1)
    pop_np[pop_np == pop.nodata] = np.NaN;

    raster_info = zip(mask_profile, pop_profile)

    return mask_np, pop_np, raster_info
