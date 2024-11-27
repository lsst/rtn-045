import numpy as np
import matplotlib.pyplot as plt
from lsst.utils.plotting import get_multiband_plot_colors, get_multiband_plot_symbols, get_multiband_plot_linestyles

# Generate data
x = np.linspace(0, 10, 100)
colors_white = get_multiband_plot_colors()
colors_black = get_multiband_plot_colors(dark_background=True)
symbols = get_multiband_plot_symbols()
line_styles = get_multiband_plot_linestyles()

# Create shared axis plots
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# Plot on white background
axes[0].set_facecolor('white')
for filter_name in colors_white.keys():
    y = np.sin(x + list(colors_white.keys()).index(filter_name)) + list(colors_white.keys()).index(filter_name)
    axes[0].plot(
        x, y,
        label=f"{filter_name}",
        color=colors_white[filter_name],
        linestyle=line_styles[filter_name],
        marker=symbols[filter_name],
        markevery=10
    )
axes[0].set_title("Demo Plot (White Background)")
axes[0].set_xlabel("X-axis")
axes[0].set_ylabel("Y-axis")
axes[0].legend(title="Filters", loc='upper left')
axes[0].grid(True, alpha=0.3)

# Plot on black background
axes[1].set_facecolor('black')
for filter_name in colors_black.keys():
    y = np.sin(x + list(colors_black.keys()).index(filter_name)) + list(colors_black.keys()).index(filter_name)
    axes[1].plot(
        x, y,
        label=f"{filter_name}",
        color=colors_black[filter_name],
        linestyle=line_styles[filter_name],
        marker=symbols[filter_name],
        markevery=10
    )
axes[1].set_title("Demo Plot (Black Background)", color='white')
axes[1].set_xlabel("X-axis", color='white')
axes[1].set_ylabel("Y-axis", color='white')
axes[1].legend(title="Filters", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=6, frameon=False, fontsize=10)
axes[1].grid(True, alpha=0.3, color='white')
axes[1].tick_params(colors='white')

plt.tight_layout()
plt.show()
