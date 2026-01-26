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
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib import cm
    return cm, mo, np, plt


@app.cell
def __():
    # Source: https://buffalodyl.com/STRK.html
    # https://x.com/BuffaloDylBTC/status/1898194173016060089/photo/1
    return


@app.cell
def __(mo):
    # Create interactive sliders for current values
    current_ust_slider = mo.ui.slider(
        start=0.01,
        stop=0.10,
        step=0.001,
        value=0.043,
        label="10Y UST Yield:",
        show_value=True
    )
    
    current_mstr_slider = mo.ui.slider(
        start=100,
        stop=3000,
        step=5,
        value=165,
        label="MSTR Price ($):",
        show_value=True
    )
    
    current_strk_slider = mo.ui.slider(
        start=50,
        stop=300,
        step=1,
        value=84,
        label="Current STRK Price ($):",
        show_value=True
    )
    return current_mstr_slider, current_strk_slider, current_ust_slider


@app.cell
def __(current_mstr_slider, current_strk_slider, current_ust_slider, mo):
    # Display sliders
    mo.vstack([
        mo.md("## STRK Price Model - Interactive Controls"),
        mo.md("Adjust the current market conditions to see how STRK price relates to 10Y UST yield and MSTR price:"),
        current_ust_slider,
        current_mstr_slider,
        current_strk_slider,
    ])
    return


@app.cell
def __(current_mstr_slider, current_strk_slider, current_ust_slider):
    # Get current values from sliders
    current_ust = current_ust_slider.value
    current_mstr = current_mstr_slider.value
    current_strk = current_strk_slider.value
    return current_mstr, current_strk, current_ust


@app.cell
def __(cm, current_mstr, current_strk, current_ust, np, plt):
    # Define ranges for the surface
    x = np.linspace(0.01, 0.05, 100)  # 10Y UST (1% to 5%)
    y = np.linspace(200, 3000, 100)  # MSTR price (200 to 3000)
    X, Y = np.meshgrid(x, y)

    # Calculate Z (STRK price)
    Z_straight = 8 / (X + 0.0423)  # Straight value: $8 / (yield + risk premium)
    Z_conversion = Y / 10  # Conversion value: MSTR price / 10
    Z = np.maximum(Z_straight, Z_conversion)  # STRK price is the max of the two

    # Calculate model STRK at current point on surface
    surface_strk = 8 / (current_ust + 0.0423)

    # Create 3D plot using matplotlib without mpl_toolkits
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Add colored surface with gradient
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', 
                           alpha=0.8, linewidth=0, antialiased=True)
    
    # Add colorbar
    cbar = fig.colorbar(surf, ax=ax, label='STRK Price ($)', pad=0.1, shrink=0.7)

    # Add black wireframe on top of surface
    ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.3, alpha=0.3)

    # Add vertical line segment from surface to current STRK
    ax.plot([current_ust, current_ust], 
            [current_mstr, current_mstr], 
            [surface_strk, current_strk], 
            color='red', linewidth=4, label='Current vs Model')

    # Add point on surface (model price)
    ax.scatter([current_ust], [current_mstr], [surface_strk], 
              color='green', s=100, marker='D', 
              label=f'Model: ${surface_strk:.2f}', 
              edgecolors='black', linewidth=2, zorder=5)

    # Add current market point
    ax.scatter([current_ust], [current_mstr], [current_strk], 
              color='red', s=100, marker='o', 
              label=f'Current: ${current_strk:.2f}', 
              edgecolors='black', linewidth=2, zorder=5)

    # Customize labels and title
    ax.set_xlabel('10Y UST Yield', fontsize=11, labelpad=10)
    ax.set_ylabel('MSTR Price ($)', fontsize=11, labelpad=10)
    ax.set_zlabel('STRK Price ($)', fontsize=11, labelpad=10)
    ax.set_title('STRK Price vs. 10-Year Yield and MSTR Price', 
                fontsize=14, fontweight='bold', pad=20)

    # Format x-axis as percentage
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1%}'))

    # Add legend
    ax.legend(loc='upper left', fontsize=10)

    # Adjust view angle
    ax.view_init(elev=20, azim=-45)

    # Set axis limits for better view
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min(), y.max())

    # Adjust layout
    plt.tight_layout()

    # Return the figure for Marimo to display
    plt.gca()
    return X, Y, Z, Z_conversion, Z_straight, ax, cbar, fig, surf, surface_strk, x, y


@app.cell
def __(current_mstr, current_strk, current_ust, mo, surface_strk):
    # Display current statistics
    difference = current_strk - surface_strk
    percentage_diff = (difference / surface_strk) * 100
    
    mo.vstack([
        mo.md("## Current Analysis"),
        mo.md(f"""
        **Model Inputs:**
        - 10Y UST Yield: {current_ust:.3%}
        - MSTR Price: ${current_mstr:.2f}
        - Current STRK Price: ${current_strk:.2f}
        
        **Model Output:**
        - Model STRK Price: ${surface_strk:.2f}
        - Difference: ${difference:.2f} ({percentage_diff:+.2f}%)
        
        **Interpretation:**
        - {"✅ **Undervalued**" if difference < 0 else "⚠️ **Overvalued**" if difference > 0 else "⚖️ **Fair Value**"}
        - Red line shows deviation from model
        - Green diamond = Model price on surface
        - Red circle = Current market price
        """)
    ])
    return difference, percentage_diff


@app.cell
def __(mo):
    mo.md("""
    ### Model Explanation
    
    The STRK price model calculates fair value based on two components:
    
    1. **Straight Value**: $8 / (10Y UST + 0.0423 risk premium)
       - Higher yields → Lower STRK price
       - Represents bond-like valuation floor
    
    2. **Conversion Value**: MSTR Price / 10
       - Higher MSTR → Higher STRK price
       - Represents equity upside potential
    
    **Final STRK Price = Maximum of the two values**
    
    Use the sliders above to explore different scenarios and see how STRK should be priced under various market conditions.
    """)
    return


if __name__ == "__main__":
    app.run()
