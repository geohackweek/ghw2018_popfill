#!/usr/bin/env python

import popfill.loader
import popfill.kernel


mask_file = "data/mask_clip_simple.tif"
population_file = "data/pop_clip_simple.tif"

loader = popfill.loader.PopulationLoader()
mask, population = loader.load(mask_file, population_file)

kernel = popfill.kernel.Basic()
new_counts = kernel.fill(mask.data, population.data)

print(new_counts)
