# Sea Level Predictor

This is the boilerplate for the Sea Level Predictor project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor

This project analyzes the global average sea level change since 1880 and predicts future sea level rise through 2050 using linear regression.

## Features

- Imports and analyzes data from `epa-sea-level.csv`
- Creates a scatter plot of sea level rise over time
- Plots two lines of best fit:
  - One using all available data (1880–most recent year)
  - One using data from 2000–most recent year
- Predicts sea level rise through the year 2050
- Saves the resulting plot as `sea_level_plot.png`

## Usage

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the analysis and generate the plot:**
   ```
   python main.py
   ```

3. **Run the unit tests:**
   ```
   python -m unittest test_module.py
   ```

## Project Structure

- `sea_level_predictor.py` – Main analysis and plotting code
- `epa-sea-level.csv` – Data file
- `main.py` – Entrypoint for running the project and tests
- `test_module.py` – Unit tests
- `requirements.txt` – Python dependencies

## Data Source

Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

## Learn More

- [Python for Everybody Video Course](https://www.youtube.com/watch?v=8DvywoWv6fI)
- [How to Analyze Data with Python Pandas](https://www.youtube.com/watch?v=vmEHCJofslg)
- [freeCodeCamp Sea Level Predictor Project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor)