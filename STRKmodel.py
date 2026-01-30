# /// script
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.8",
#     "numpy==2.4.1",
# ]
# ///

import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    #Source: https://buffalodyl.com/STRK.html    https://x.com/BuffaloDylBTC/status/1898194173016060089/photo/1

    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Define ranges
    x = np.linspace(0, 0.05, 100)  # 10Y UST (0% to 5%)
    y = np.linspace(200, 3000, 100)  # MSTR price (200 to 3000)
    X, Y = np.meshgrid(x, y)

    # Calculate Z (STRK price)
    Z_straight = 8 / (X + 0.0423)  # Straight value: $8 / (yield + risk premium)
    Z_conversion = Y / 10  # Conversion value: MSTR price / 10
    Z = np.maximum(Z_straight, Z_conversion)  # STRK price is the max of the two

    # Current point
    current_ust = 0.043  # 10Y UST
    current_mstr = 165   # MSTR price
    current_strk = 84    # STRK price (your value)
    surface_strk = 8 / (current_ust + 0.0423)  # Model STRK at surface (~93.57)

    # Create 3D plot
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Add colored surface with gradient
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', zorder=1)
    cbar = fig.colorbar(surf, ax=ax, label='STRK Price ($)', pad=0.1)

    # Add black wireframe on top of surface
    ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.5, zorder=2)

    # Add vertical line segment from surface to current STRK
    ax.plot([current_ust, current_ust], [current_mstr, current_mstr], [surface_strk, current_strk],
            color='red', linewidth=4, zorder=3)

    # Customize labels and title
    ax.set_xlabel('10Y UST')
    ax.set_ylabel('MSTR Price ($)')
    ax.set_zlabel('STRK Price ($)')
    ax.set_title('STRK Price vs. 10-Year Yield and MSTR Price')

    # Adjust initial view: STRK on z, 10Y UST left, MSTR right
    ax.view_init(elev=20, azim=-45)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    plt.show()

    return


if __name__ == "__main__":
    app.run()
