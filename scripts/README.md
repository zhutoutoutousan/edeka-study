# Edeka Analysis Scripts

This directory contains Python scripts for comprehensive data analysis of Edeka.

## Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Scripts

### 1. Market Data Analysis (`01_market_data_analysis.py`)
- Analyzes market position and market share
- Compares Edeka with competitors
- Generates market share and revenue comparison charts

### 2. Financial Analysis (`02_financial_analysis.py`)
- Analyzes financial trends
- Calculates efficiency metrics (revenue per employee, revenue per store)
- Generates financial trend visualizations

### 3. Competitive Analysis (`03_competitive_analysis.py`)
- Analyzes competitive landscape
- Creates competitive positioning matrices
- Calculates market concentration metrics

### 4. Web Scraper (`04_web_scraper.py`)
- Scrapes public information from Edeka website
- Searches for news articles
- Extracts financial information from public sources

### 5. Run All Analysis (`05_run_all_analysis.py`)
- Master script that runs all analysis scripts
- Generates comprehensive reports

## Usage

Run individual scripts:
```bash
python scripts/01_market_data_analysis.py
python scripts/02_financial_analysis.py
python scripts/03_competitive_analysis.py
python scripts/04_web_scraper.py
```

Or run all analyses:
```bash
python scripts/05_run_all_analysis.py
```

## Output

All results are saved in the `results/` directory:
- CSV files with data
- PNG files with visualizations
- JSON files with scraped data

## Note

- Some scripts use placeholder data that should be replaced with actual data sources
- Web scraping should be done responsibly and in compliance with website terms of service
- Edeka is not publicly traded, so financial data availability is limited
