#!/usr/bin/env python

import popfill.loader
import popfill.kernel


mask_file = "data/mask_clip_simple.tif"
population_file = "data/pop_clip_simple.tif"

loader = popfill.loader.PopulationLoader()
mask, population = loader.load(mask_file, population_file)

kernel = popfill.kernel.Basic(mask.data, population.data)
new_counts = kernel.fill()

print(new_counts)
