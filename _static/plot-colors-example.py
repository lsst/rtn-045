import numpy as np
import matplotlib.pyplot as plt

# Define palettes, from RTN-045.
# Module works with LSST Science Pipelines version >= daily 2024_12_02
try: 
    from lsst.utils.plotting import get_multiband_plot_colors, get_multiband_plot_symbols, get_multiband_plot_linestyles
    colors_white = get_multiband_plot_colors()
    colors_black = get_multiband_plot_colors(dark_background=True)
    symbols = get_multiband_plot_symbols()
    line_styles = get_multiband_plot_linestyles()
except ImportError:
    print("LSST plotting utilities not available; defining styles directly.")
    colors_white = {
        'u': '#0c71ff', 'g': '#49be61', 'r': '#c61c00', 
        'i': '#ffc200', 'z': '#f341a2', 'y': '#5d0000'
    }
    colors_black = {
        'u': '#3eb7ff', 'g': '#30c39f', 'r': '#ff7e00', 
        'i': '#2af5ff', 'z': '#a7f9c1', 'y': '#fdc900'
    }
    symbols = {
        'u': 'o', 'g': '^', 'r': 'v', 'i': 's', 
        'z': '*', 'y': 'p'
    }
    line_styles = {
        'u': '--', 'g': ':', 'r': '-', 'i': '-.', 
        'z': (0, (3, 5, 1, 5, 1, 5)), 'y': (0, (3, 1, 1, 1))
    }

# Generate data
x = np.linspace(0, 10, 100)

# Generate overlapping histogram data
filters = list(colors_white.keys())
overlap_hist_data = {f: np.random.normal(loc=i, scale=1.5, size=1000) for i, f in enumerate(filters)}

# Font size parameters
font_size = 16  # Axis labels and titles
legend_font_size = 14  # Legend
marker_size = 10  # Marker size

# Create shared axis plots
fig, axes = plt.subplots(2, 2, figsize=(16, 12), sharey=False, gridspec_kw={'height_ratios': [1, 1]})

# First row: Line plots
# White background
axes[0, 0].set_facecolor('white')
for filter_name in colors_white.keys():
    y = np.sin(x + filters.index(filter_name)) + filters.index(filter_name)
    axes[0, 0].plot(
        x, y,
        label=f"{filter_name}",
        color=colors_white[filter_name],
        linestyle=line_styles[filter_name],
        marker=symbols[filter_name],
        markevery=10,
        markersize=marker_size  # Increase marker size
    )
axes[0, 0].set_title("Line Plot (White Background)", fontsize=font_size)
axes[0, 0].set_xlabel("X-axis", fontsize=font_size)
axes[0, 0].set_ylabel("Y-axis", fontsize=font_size)
axes[0, 0].set_xlim([-2, 11])
axes[0, 0].legend(title="Filters", loc='upper left', fontsize=legend_font_size, title_fontsize=legend_font_size)
axes[0, 0].grid(True, alpha=0.3)

# Black background
axes[0, 1].set_facecolor('black')
for filter_name in colors_black.keys():
    y = np.sin(x + filters.index(filter_name)) + filters.index(filter_name)
    axes[0, 1].plot(
        x, y,
        label=f"{filter_name}",
        color=colors_black[filter_name],
        linestyle=line_styles[filter_name],
        marker=symbols[filter_name],
        markevery=10,
        markersize=marker_size  # Increase marker size
    )
axes[0, 1].set_title("Line Plot (Black Background)", color='white', fontsize=font_size)
axes[0, 1].set_xlabel("X-axis", color='white', fontsize=font_size)
axes[0, 1].set_ylabel("Y-axis", color='white', fontsize=font_size)
axes[0, 1].legend(title="Filters", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=6, frameon=False, fontsize=legend_font_size, title_fontsize=legend_font_size)
axes[0, 1].grid(True, alpha=0.3, color='white')
axes[0, 1].tick_params(colors='white')

# Second row: Overlapping histograms
# White background
axes[1, 0].set_facecolor('white')
for filter_name in colors_white.keys():
    axes[1, 0].hist(
        overlap_hist_data[filter_name], bins=30, density=True,
        histtype='step', linewidth=2,
        color=colors_white[filter_name],
        linestyle=line_styles[filter_name],
        label=f"{filter_name}"
    )
axes[1, 0].set_title("Overlapping Histograms (White Background)", fontsize=font_size)
axes[1, 0].set_xlabel("Value", fontsize=font_size)
axes[1, 0].set_ylabel("Density", fontsize=font_size)
axes[1, 0].legend(title="Filters", loc='upper left', fontsize=legend_font_size, title_fontsize=legend_font_size)

# Black background
axes[1, 1].set_facecolor('black')
for filter_name in colors_black.keys():
    axes[1, 1].hist(
        overlap_hist_data[filter_name], bins=30, density=True,
        histtype='step', linewidth=2,
        color=colors_black[filter_name],
        linestyle=line_styles[filter_name],
        label=f"{filter_name}"
    )
axes[1, 1].set_title("Overlapping Histograms (Black Background)", color='white', fontsize=font_size)
axes[1, 1].set_xlabel("Value", color='white', fontsize=font_size)
axes[1, 1].set_ylabel("Density", color='white', fontsize=font_size)
axes[1, 1].legend(title="Filters", loc='upper left', fontsize=legend_font_size, title_fontsize=legend_font_size)
axes[1, 1].tick_params(colors='white')

plt.tight_layout()
plt.savefig("example-plots-colors-symbols-lines.png", dpi=300, bbox_inches='tight')
plt.show()
