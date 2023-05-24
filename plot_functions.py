import matplotlib.pyplot as plt
from typing import List, Optional, Tuple


def show_available_plot_styles():
    """
    Function to display the available plot styles in Matplotlib.
    """
    available_styles = plt.style.available
    
    print("Available Plot Styles:")
    for style in available_styles:
        print(style)


def plot_histogram(data: List[float], 
                   bins: int =25, 
                   color: str = 'blue', 
                   edgecolor: str = 'black', 
                   alpha: float = 0.7,
                   xlabel: str = '', ylabel: str = '', 
                   title: str = '', 
                   grid: bool= False, 
                   xlim: Optional[Tuple[float,float]]=None, 
                   ylim: Optional[Tuple[float, float]]=None,
                   figsize: Tuple[float,float]=(8, 6), 
                   legend: bool = False) -> None:
    """
    Function to create a customizable histogram using Matplotlib.
    
    Parameters:
    - data: The data array or list to create the histogram from.
    - bins: The number of bins for the histogram.
    - color: The color of the bars in the histogram.
    - edgecolor: The color of the edges of the bars.
    - alpha: The transparency of the bars.
    - xlabel: The label for the x-axis.
    - ylabel: The label for the y-axis.
    - title: The title of the histogram plot.
    - grid: Whether to display grid lines (True or False).
    - xlim: The x-axis limits as a tuple (xmin, xmax).
    - ylim: The y-axis limits as a tuple (ymin, ymax).
    - figsize: The figure size as a tuple (width, height).
    - legend: Whether to display the legend (True or False).
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.hist(data, bins=bins, color=color, edgecolor=edgecolor, alpha=alpha)
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)
    
    if grid:
        ax.grid(True)
    
    if legend:
        ax.legend()
    
    plt.show()


