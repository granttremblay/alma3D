import numpy as np
from spectral_cube import read
from yt.mods import ColorTransferFunction, write_bitmap
import astropy.units as u


cube = read('cube.fits', format='fits')
ytcube = cube[:,100:-100,100:-100].to_yt()
ds = ytcube.dataset

# Set the number of levels, the minimum and maximum level and the width
# of the isocontours
n_v = 10
vmin = 0.05
vmax = 4.0
dv = 0.02

# Set up color transfer function
transfer = ColorTransferFunction((vmin, vmax))
transfer.add_layers(n_v, dv, colormap='RdBu_r')



images = ytcube.quick_render_movie('quickmovie')

ytc.quick_isocontour(level=0.0007, title="Abell 2597 in CO(2-1)")
