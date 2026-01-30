# Interactive STRK Price Model

Two versions of an interactive STRK price model using Marimo with adjustable sliders.

## Files

1. **STRKmodel_interactive.py** (RECOMMENDED)
   - Uses Plotly for interactive 3D visualization
   - Fully interactive plot (rotate, zoom, pan)
   - Better performance and user experience
   - No mpl_toolkits dependency issues

2. **STRKmodel_matplotlib.py** (FALLBACK)
   - Uses matplotlib with built-in 3D support
   - Static 3D view (fixed angle)
   - Works if Plotly has issues
   - Same slider functionality

## Installation

### Option 1: Using Plotly (Recommended)

```bash
pip install marimo plotly numpy
```

### Option 2: Using Matplotlib (Fallback)

```bash
pip install marimo matplotlib numpy
```

## Running the App

### Plotly Version (Recommended)

```bash
marimo edit STRKmodel_interactive.py
```

### Matplotlib Version

```bash
marimo edit STRKmodel_matplotlib.py
```

This will open the app in your browser with interactive controls.

## Features

### Interactive Sliders

Adjust these parameters in real-time:

1. **10Y UST Yield** (0.01 to 0.10)
   - Current default: 0.043 (4.3%)
   - Step: 0.001 (0.1%)

2. **MSTR Price** ($100 to $3000)
   - Current default: $165
   - Step: $5

3. **Current STRK Price** ($50 to $300)
   - Current default: $84
   - Step: $1

### Visualization

The 3D surface shows:
- **X-axis**: 10Y UST Yield
- **Y-axis**: MSTR Price
- **Z-axis**: STRK Model Price

**Visual Indicators:**
- **Surface**: STRK model price across all scenarios
- **Green marker**: Model-predicted STRK price at current inputs
- **Red marker**: Your inputted current STRK price
- **Red line**: Deviation from model (shows over/undervaluation)

### Analysis Panel

Real-time statistics showing:
- Model inputs (your slider values)
- Model-predicted STRK price
- Difference from current price
- Percentage over/undervaluation
- Interpretation (undervalued/overvalued/fair)

## Model Formula

**STRK Price = MAX(Straight Value, Conversion Value)**

Where:
- **Straight Value** = $8 / (10Y UST Yield + 0.0423)
  - Bond-like valuation floor
  - Inversely related to yields
  
- **Conversion Value** = MSTR Price / 10
  - Equity conversion upside
  - Directly related to MSTR price

## Use Cases

1. **Current Valuation**: See if STRK is fairly priced
2. **Scenario Analysis**: What if yields rise to 5%?
3. **MSTR Correlation**: How does MSTR price affect STRK?
4. **Risk Assessment**: Understand yield sensitivity

## Troubleshooting

### "No module named 'plotly'" error

Install Plotly:
```bash
pip install plotly
```

Or use the matplotlib version instead.

### "projection='3d' not recognized" error

This shouldn't happen with modern matplotlib, but if it does:
```bash
pip install --upgrade matplotlib
```

Or use the Plotly version which doesn't have this issue.

### Marimo not opening

Make sure Marimo is installed:
```bash
pip install marimo
marimo --version
```

## Differences Between Versions

| Feature | Plotly Version | Matplotlib Version |
|---------|----------------|-------------------|
| 3D Interaction | ✅ Full (rotate/zoom) | ❌ Static view |
| Performance | ✅ Better | ⚠️ Good |
| Visual Quality | ✅ Modern | ✅ Classic |
| Dependencies | plotly | matplotlib |
| 3D Library Issues | ✅ None | ⚠️ Possible |

**Recommendation**: Start with Plotly version. Only use matplotlib if you have dependency issues.

## Source

Original model by Buffalo Dylan:
- Website: https://buffalodyl.com/STRK.html
- Twitter: https://x.com/BuffaloDylBTC/status/1898194173016060089

## Tips

- **Rotate the plot** (Plotly only): Click and drag
- **Zoom**: Scroll wheel (Plotly) or fixed in matplotlib
- **Reset view**: Double-click the plot (Plotly only)
- **Explore scenarios**: Try extreme values to see model behavior
- **Compare quickly**: Adjust sliders to see immediate updates

## Example Scenarios to Try

1. **Bull Case**: MSTR = $2000, 10Y UST = 3%
2. **Bear Case**: MSTR = $200, 10Y UST = 6%
3. **Current Reality**: MSTR = $165, 10Y UST = 4.3%
4. **High Yield Stress**: Keep MSTR constant, raise yield to 8%

Enjoy exploring the STRK price model!
