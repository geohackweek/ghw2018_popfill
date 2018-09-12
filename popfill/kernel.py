import rasterio
import rasterio.plot
# import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

%matplotlib inline

class Basic(object):

    def fill(this, mask, counts):
        return counts.copy()


# this function generates a boolean mask based on the population map
def pop2msk(pop):
    mask = (pop == pop )
    return mask;

# this function converts a tiff file to a numpy array
def tiff2np(pop_file):
    with rasterio.open(pop_file) as pop:

        print('population surface:')
        print(pop.profile)

        pop_crs = pop.crs
        pop_nodata = pop.nodata
        pop_profile = pop.profile.copy()
        pop_aff = pop.transform

        pop_np = pop.read(1)
        pop_np[pop_np == pop_nodata] = np.NaN;

        return pop_np;

# converts the ocean / land tiff to a boolean mask
def oceanmask(mask_file):
    mask_crs = mask.crs
    mask_nodata = mask.nodata
    mask_profile = mask.profile.copy()
    mask_aff = mask.transform
    # note the origin is slightly different beetween pop and mask
    mask_np = mask.read(1)
    mask_np[mask_np == mask_nodata] = 0

    mask_np = mask_np.astype(bool)

