# Options Pricing Heatmap

This project provides an interactive tool to visualize European call and put option prices using the Black-Scholes model. It generates a heatmap that shows how the option price changes with variations in the underlying asset's spot price and volatility.

## Features

*   **Interactive Heatmap:** Visualizes option prices for a range of spot prices and volatilities.
*   **Real-time Updates:** All parameters can be adjusted in real-time.
*   **Customizable Parameters:**
    *   **Base Spot (S):** The initial price of the underlying asset.
    *   **Strike (K):** The strike price of the option.
    *   **Time (T):** Time to maturity in years.
    *   **Base Vol (sd):** The initial volatility of the underlying asset.
    *   **Rate (R):** The risk-free interest rate.
*   **Option Type:** Switch between calculating prices for 'Call' and 'Put' options.
*   **Adjustable Ranges:** Use sliders to control the range of spot prices and volatilities displayed on the heatmap axes.

## Files

*   `black_scholes.py`: Contains the Python implementation of the Black-Scholes formulas for calculating the price of European call and put options.
*   `interactiveoptionprice.py`: The main script that uses `matplotlib` and `seaborn` to create the interactive heatmap and user interface controls.

## Requirements

To run this project, you need to have the following Python libraries installed:

*   `numpy`
*   `seaborn`
*   `matplotlib`
*   `scipy`

You can install them using pip:
```bash
pip install numpy seaborn matplotlib scipy
```

## Usage

To start the application, run the following command in your terminal:

```bash
python interactiveoptionprice.py
```

## How to Use the Interface

1.  **Heatmap:** The central part of the window displays the heatmap. The y-axis represents the spot price, the x-axis represents volatility, and the color of each cell indicates the option price. The exact price is also annotated in each cell.
2.  **Parameter Textboxes:** At the bottom, there are text boxes to set the core parameters for the Black-Scholes model (`S`, `K`, `T`, `sd`, `R`). After typing a new value, press Enter to update the heatmap.
3.  **Range Sliders:** Use the sliders to adjust the upper and lower deviation from the base spot price and volatility. This changes the ranges of the axes on the heatmap.
4.  **Option Type Radio Buttons:** On the bottom right, you can select either 'Call' or 'Put' to switch the pricing model. The heatmap will update accordingly.
