# /// script
# dependencies = [
#     "marimo",
#     "plotly==5.24.1",
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
    import plotly.graph_objects as go

    return mo, np, go


@app.cell
def __():
    # Source: https://buffalodyl.com/STRK.html
    # https://x.com/BuffaloDylBTC/status/1898194173016060089/photo/1
    return


@app.cell
def __(mo):
    # Create interactive sliders for current and projected values
    current_ust_slider = mo.ui.slider(
        start=0.005,
        stop=0.10,
        step=0.001,
        value=0.043,
        label="Current 10Y UST Yield:",
        show_value=True,
    )

    current_mstr_slider = mo.ui.slider(
        start=100,
        stop=4000,
        step=5,
        value=165,
        label="Current MSTR Price ($):",
        show_value=True,
    )

    current_strk_slider = mo.ui.slider(
        start=50,
        stop=300,
        step=1,
        value=84,
        label="Current STRK Price ($):",
        show_value=True,
    )

    projected_ust_slider = mo.ui.slider(
        start=0.005,
        stop=0.10,
        step=0.001,
        value=0.035,
        label="Projected 10Y UST Yield:",
        show_value=True,
    )

    projected_mstr_slider = mo.ui.slider(
        start=100,
        stop=4000,
        step=5,
        value=500,
        label="Projected MSTR Price ($):",
        show_value=True,
    )
    return (
        current_mstr_slider,
        current_strk_slider,
        current_ust_slider,
        projected_mstr_slider,
        projected_ust_slider,
    )


@app.cell
def __(
    current_mstr_slider,
    current_strk_slider,
    current_ust_slider,
    projected_mstr_slider,
    projected_ust_slider,
    mo,
):
    # Display sliders
    mo.vstack(
        [
            mo.md("## STRK Price Model - Interactive Controls"),
            mo.md("### Current Market Conditions"),
            current_ust_slider,
            current_mstr_slider,
            current_strk_slider,
            mo.md("### Projected Scenario"),
            projected_ust_slider,
            projected_mstr_slider,
        ]
    )
    return


@app.cell
def __(
    current_mstr_slider,
    current_strk_slider,
    current_ust_slider,
    projected_mstr_slider,
    projected_ust_slider,
):
    # Get current values from sliders
    current_ust = current_ust_slider.value
    current_mstr = current_mstr_slider.value
    current_strk = current_strk_slider.value

    # Get projected values from sliders
    projected_ust = projected_ust_slider.value
    projected_mstr = projected_mstr_slider.value
    return current_mstr, current_strk, current_ust, projected_mstr, projected_ust


@app.cell
def __(current_mstr, current_strk, current_ust, projected_mstr, projected_ust, go, np):
    # Define ranges for the surface with finer granularity for UST
    x = np.linspace(0.01, 0.10, 100)  # 10Y UST (1% to 10%) with 1% granularity
    y = np.linspace(100, 4000, 50)  # MSTR price (100 to 4000)
    X, Y = np.meshgrid(x, y)

    # Calculate Z (STRK price)
    Z_straight = 8 / (X + 0.0423)  # Straight value: $8 / (yield + risk premium)
    Z_conversion = Y / 10  # Conversion value: MSTR price / 10
    Z = np.maximum(Z_straight, Z_conversion)  # STRK price is the max of the two

    # Calculate model STRK at current point on surface
    current_model_strk = 8 / (current_ust + 0.0423)

    # Calculate model STRK at projected point on surface
    projected_model_strk = 8 / (projected_ust + 0.0423)
    projected_conversion = projected_mstr / 10
    projected_model_strk = max(projected_model_strk, projected_conversion)

    # Create 3D surface plot with Plotly
    fig = go.Figure()

    # Add main surface
    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale="RdBu_r",
            name="STRK Model Price",
            showscale=True,
            colorbar=dict(
                title="STRK Price ($)",
                len=0.7,
            ),
            opacity=0.9,
        )
    )

    # Add current STRK price (actual market price) - RED CIRCLE
    fig.add_trace(
        go.Scatter3d(
            x=[current_ust],
            y=[current_mstr],
            z=[current_strk],
            mode="markers",
            marker=dict(
                size=10, color="red", symbol="circle", line=dict(color="black", width=2)
            ),
            name=f"Current STRK: ${current_strk:.2f}",
            showlegend=True,
        )
    )

    # Add current model prediction point - GREEN CIRCLE
    fig.add_trace(
        go.Scatter3d(
            x=[current_ust],
            y=[current_mstr],
            z=[current_model_strk],
            mode="markers",
            marker=dict(
                size=10,
                color="green",
                symbol="circle",
                line=dict(color="black", width=2),
            ),
            name=f"Current Model: ${current_model_strk:.2f}",
            showlegend=True,
        )
    )

    # Add projected model prediction point - BLUE CIRCLE
    fig.add_trace(
        go.Scatter3d(
            x=[projected_ust],
            y=[projected_mstr],
            z=[projected_model_strk],
            mode="markers",
            marker=dict(
                size=10,
                color="blue",
                symbol="circle",
                line=dict(color="black", width=2),
            ),
            name=f"Projected Model: ${projected_model_strk:.2f}",
            showlegend=True,
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="STRK Price vs. 10-Year Yield and MSTR Price", font=dict(size=20)
        ),
        scene=dict(
            xaxis=dict(
                title="10Y UST Yield",
                tickformat=".0%",
                range=[0.01, 0.10],  # Explicitly set range to show full 1-10%
                tickmode="linear",
                tick0=0.01,
                dtick=0.01,  # Tick every 1%
            ),
            yaxis=dict(
                title="MSTR Price ($)",
            ),
            zaxis=dict(
                title="STRK Price ($)",
            ),
            camera=dict(eye=dict(x=1.5, y=-1.5, z=1.2)),
        ),
        width=900,
        height=700,
        margin=dict(l=0, r=0, t=80, b=0),
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor="rgba(255, 255, 255, 0.8)",
            bordercolor="black",
            borderwidth=1,
        ),
    )

    fig
    return (
        X,
        Y,
        Z,
        Z_conversion,
        Z_straight,
        current_model_strk,
        fig,
        projected_conversion,
        projected_model_strk,
        x,
        y,
    )


@app.cell
def __(
    current_mstr,
    current_strk,
    current_ust,
    current_model_strk,
    projected_mstr,
    projected_ust,
    projected_model_strk,
    mo,
):
    # Display current statistics
    current_difference = current_strk - current_model_strk
    current_percentage_diff = (current_difference / current_model_strk) * 100

    mo.vstack(
        [
            mo.md("## Current Analysis"),
            mo.md(f"""
        **Current Market Inputs:**
        - 10Y UST Yield: {current_ust:.3%}
        - MSTR Price: ${current_mstr:.2f}
        - Current STRK Price: ${current_strk:.2f}
        
        **Current Model Output:**
        - Model STRK Price: ${current_model_strk:.2f}
        - Difference: ${current_difference:.2f} ({current_percentage_diff:+.2f}%)
        - {"✅ **Undervalued**" if current_difference < 0 else "⚠️ **Overvalued**" if current_difference > 0 else "⚖️ **Fair Value**"}
        
        ---
        
        **Projected Scenario:**
        - Projected 10Y UST Yield: {projected_ust:.3%}
        - Projected MSTR Price: ${projected_mstr:.2f}
        - Projected Model STRK Price: ${projected_model_strk:.2f}
        
        **Legend:**
        - 🔴 Red Circle = Current STRK Price (Market)
        - 🟢 Green Circle = Current Model Prediction
        - 🔵 Blue Circle = Projected Model Prediction
        """),
        ]
    )
    return current_difference, current_percentage_diff


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
