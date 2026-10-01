from pathlib import Path


def print_duplicate_count(df):
    """Print and return the total number of duplicate rows.

    Args:
        df (pandas.DataFrame): The DataFrame to check for duplicate rows.

    Returns:
        int: The total number of duplicate rows.
    """
    duplicate_count = df.duplicated().sum()
    print("Total number of duplicate rows:", duplicate_count)
    return duplicate_count


def save_fig(plt, filename):
    """Save a Matplotlib figure as a high-resolution PNG image.

    Creates the ``report`` directory if it does not already exist.

    Args:
        fig (matplotlib.figure.Figure): The Matplotlib figure to save.
        filename (str): Output filename without the ``.png`` extension.
    """
    Path("figures").mkdir(exist_ok=True)
    plt.savefig(f"figures/{filename}.png", dpi=300, bbox_inches="tight")
