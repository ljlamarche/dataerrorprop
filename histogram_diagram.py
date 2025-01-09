# histogram_diagram.py
# script to create a diagram of how error-weighted histograms are constructed.

import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    g = np.exp(-(x-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return g

mu1 = -0.6
sig1 = 0.2
mu2 = 1.2
sig2 = 0.8

x = np.arange(-5., 5., 0.01)
y1 = gaussian(x, mu1, sig1)
y2 = gaussian(x, mu2, sig2)
bin_edges = np.arange(-5., 6., 1.)

# Calculate histogram
h1 = np.diff(erf((bin_edges-mu1)/(np.sqrt(2)*sig1)))/2.
h2 = np.diff(erf((bin_edges-mu2)/(np.sqrt(2)*sig2)))/2.

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)
ax.grid()
ax.plot(x, y1, color='blue')
ax.plot(x, y2, color='red')
ax.text(0.35, 0.8, rf'$\mu$ = {mu1}'+'\n'+rf'$\sigma$ = {sig1}', color='blue', transform=ax.transAxes)
ax.text(0.5, 0.3, rf'$\mu$ = {mu2}'+'\n'+rf'$\sigma$ = {sig2}', color='red', transform=ax.transAxes)

bei = 4
ax.fill_between(x, y1, where=((x>=bin_edges[bei])&(x<bin_edges[bei+1])), color='blue', alpha=0.3, zorder=1)
ax.fill_between(x, y2, where=((x>=bin_edges[bei])&(x<bin_edges[bei+1])), color='red', alpha=0.3, zorder=1)
tb = ax.text(0.1, 0.4, rf'$x_0$ = {bin_edges[bei]}'+'\n'+rf'$x_1$ = {bin_edges[bei+1]}', transform=ax.transAxes)
bb = tb.get_window_extent(renderer=fig.canvas.get_renderer()).transformed(ax.transAxes.inverted())
tb = ax.text(0.1, bb.y0, f'A = {h1[bei]:.3g}', color='blue', va='top', transform=ax.transAxes)
bb = tb.get_window_extent(renderer=fig.canvas.get_renderer()).transformed(ax.transAxes.inverted())
ax.text(0.1, bb.y0, f'A = {h2[bei]:.3g}', color='red', va='top', transform=ax.transAxes)


bei = 6
ax.fill_between(x, y1, where=((x>=bin_edges[bei])&(x<bin_edges[bei+1])), color='blue', alpha=0.3, zorder=1)
ax.fill_between(x, y2, where=((x>=bin_edges[bei])&(x<bin_edges[bei+1])), color='red', alpha=0.3, zorder=1)
tb = ax.text(0.65, 0.25, rf'$x_0$ = {bin_edges[bei]}'+'\n'+rf'$x_1$ = {bin_edges[bei+1]}', transform=ax.transAxes)
bb = tb.get_window_extent(renderer=fig.canvas.get_renderer()).transformed(ax.transAxes.inverted())
tb = ax.text(0.65, bb.y0, f'A = {h1[bei]:.3g}', color='blue', va='top', transform=ax.transAxes)
bb = tb.get_window_extent(renderer=fig.canvas.get_renderer()).transformed(ax.transAxes.inverted())
ax.text(0.65, bb.y0, f'A = {h2[bei]:.3g}', color='red', va='top', transform=ax.transAxes)

ax.stairs(h1, bin_edges, color='blue', linewidth=1, zorder=3)
ax.stairs(h2, bin_edges, color='red', linewidth=1, zorder=3)
ax.stairs(h1+h2, bin_edges, color='darkgrey', linewidth=4, zorder=2)

ax.set_xlim([-3., 5.])
ax.set_xlabel('x')

plt.savefig('histogram_diagram.png')
plt.show()
