# ghw2018_popfill

**Purpose**: The goal of this project is to come up with an intelligent interpolation method that deals with raster counts data. Our example utilizes Worldpop raster data (population counts per pixel). Interpolation of counts data requires a conservation of total numbers across the entire raster, requiring an alternative approach to classic methods (kriging etc).

In our example, a subset of worldpop data does not quite define land/sea in the same way as a standard land/sea mask. The goal is to treat 4 different interactions between these surfaces in the following way:

**Data in Worldpop, NA in mask**: Redistribute counts from a given Worldpop pixel to other data pixels as defined by the mask.

**NA in Worldpop, data in mask**: Subtract counts from neighboring Worldpop data pixels to fill missing pixel in WorldPop.

**Data in Worldpop, data in mask**: Do not alter counts, unless adding/subtracting values to fulfill needs for a neighboring pixel

**NA in WorldPop, NA in mask**: No change

Counts will be altered by [math stuff]...

The end product will be a Worldpop raster in the same format/resolution as the original but with the values shifted to match the coverage of the mask file, while still allowing the population data to add up to the same total

**Description of subtasks**:
Convert input raster data to numpy array, and save raster metadata for use at the end.
Use Kernel [more math stuff..]
Convert updated numpy array to raster tif with the same metadata as before
Visualization of changes:
Figure depicting 4 classes of change (see above)
Figure showing final pop surface
Figure showing change in values from old to new (mostly flat, except for change areas)

**Description of scripts**: tbd 
