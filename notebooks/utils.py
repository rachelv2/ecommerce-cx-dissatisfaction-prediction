import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path

FIG_PATH = Path("../figures")
FIG_PATH.mkdir(exist_ok=True)

def save_fig(fig, name):
    fig.savefig(FIG_PATH / name, dpi=300, bbox_inches="tight")
    
# Style
ACCENT = "#111111"
DARK = "#1A1A1A"
MID = "#7A7A7A"
LIGHT = "#E5E5E5"
BG = "#FFFFFF"

mpl.rcParams.update({
    "figure.facecolor": BG,
    "axes.facecolor": BG,

    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans"],
    "font.size": 12,

    "axes.titlesize": 20,
    "axes.titleweight": "normal",
    "axes.labelsize": 13,

    "axes.labelcolor": DARK,
    "axes.titlecolor": DARK,

    "xtick.color": MID,
    "ytick.color": MID,

    "grid.color": LIGHT,
    "grid.linewidth": 0.6,

    "figure.figsize": (10, 6),
    "axes.titlepad": 24,
    "axes.labelpad": 12,
})

def create_figure(figsize=(10, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


def clean_axes(ax, grid_axis="y"):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    ax.grid(axis=grid_axis, color=LIGHT, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(length=0, pad=8)
    ax.margins(x=0.03, y=0.10)


def add_title(ax, title, subtitle=None):
    ax.set_title(title, loc="left", pad=24, fontsize=20, weight="normal", color=DARK)

    if subtitle:
        ax.text(
            0, 1.02, subtitle,
            transform=ax.transAxes,
            fontsize=11.5,
            color=MID,
            ha="left"
        )
