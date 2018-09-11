#!/usr/bin/env python

import popfill.loader
import popfill.kernel

loader = popfill.loader.DummyLoader(3,3)
mask, counts = loader.load()

kernel = popfill.kernel.Basic()
new_counts = kernel.fill(mask, counts)

print(new_counts)
