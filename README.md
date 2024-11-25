# phbs-qps-2024
https://github.com/theater27/phbs-qps-2024
# US CPI Inflation Analysis

This project fetches and analyzes US Consumer Price Index (CPI) data to calculate quarterly inflation rates.

## Project Structure

```
.
├── data/               # Data storage (both raw and processed)
│   ├── raw/           # Original, immutable data
│   └── processed/     # Cleaned and processed data
├── notebooks/         # Jupyter notebooks for exploration and analysis
├── scripts/          # Standalone scripts
└── src/              # Source code modules
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/us-cpi-inflation.git
cd us-cpi-inflation
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Using the Script

Run the CPI inflation calculator:
```bash
python scripts/cpi_inflation.py
```

### Using the Notebook

1. Start Jupyter Lab:
```bash
jupyter lab
```

2. Navigate to `notebooks/cpi_analysis.ipynb`

## Data

- Input: CPI data from FRED (Federal Reserve Economic Data)
- Output: Quarterly inflation rates stored in CSV format

## Dependencies

- pandas
- pandas-datareader
- jupyter (for notebooks)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
