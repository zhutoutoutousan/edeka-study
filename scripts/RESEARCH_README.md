# Research Scripts for Edeka Book

## Overview

These scripts generate research data and publication-quality figures for the Edeka analysis book.

## Scripts

### 1. `06_research_data_collection.py`
Main research script that:
- Collects market data
- Generates financial trends
- Creates publication-quality figures (PNG and PDF)
- Exports data in CSV and LaTeX formats

**Generated Figures:**
- `market_share_pie.png/pdf` - Market share distribution pie chart
- `revenue_trend.png/pdf` - Revenue trend over time
- `efficiency_metrics.png/pdf` - Revenue per employee/store metrics
- `competitive_comparison.png/pdf` - Competitive comparison charts
- `store_distribution.png/pdf` - Store count comparison
- `growth_analysis.png/pdf` - Year-over-year growth rates

### 2. `07_figure_integration.py`
Generates LaTeX code for including figures in the book.

### 3. `08_run_research.py`
Master script that runs all research and figure generation.

## Usage

### Basic Usage

```bash
# Navigate to scripts directory
cd scripts

# Run research data collection
python 06_research_data_collection.py

# Generate LaTeX integration code
python 07_figure_integration.py

# Or run everything at once
python 08_run_research.py
```

### Output Structure

```
results/
├── figures/
│   ├── market_share_pie.png
│   ├── market_share_pie.pdf
│   ├── revenue_trend.png
│   ├── revenue_trend.pdf
│   ├── efficiency_metrics.png
│   ├── efficiency_metrics.pdf
│   ├── competitive_comparison.png
│   ├── competitive_comparison.pdf
│   ├── store_distribution.png
│   ├── store_distribution.pdf
│   ├── growth_analysis.png
│   └── growth_analysis.pdf
├── figures_latex_code.tex
data/
├── market_share_data.csv
├── market_share_data.tex
├── financial_trends.csv
└── financial_trends.tex
```

## Including Figures in LaTeX

### Step 1: Copy Figures
Copy figures from `results/figures/` to `book/figures/`:

```bash
mkdir -p book/figures
cp results/figures/*.png book/figures/
cp results/figures/*.pdf book/figures/
```

### Step 2: Use in Chapters

Add to your chapter files:

```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.9\textwidth]{figures/market_share_pie.png}
\caption{German Food Retail Market Share Distribution / 
         Marktanteilsverteilung im deutschen Lebensmitteleinzelhandel / 
         德国食品零售市场份额分布}
\label{fig:market_share_pie}
\end{figure}
```

Or use the generated LaTeX code from `results/figures_latex_code.tex`.

## Figure Specifications

All figures are generated with:
- **Resolution**: 300 DPI (publication quality)
- **Format**: PNG (for preview) and PDF (for LaTeX)
- **Size**: Optimized for book pages
- **Trilingual**: All labels in English, German, and Chinese
- **Style**: Professional, publication-ready

## Customization

### Modify Data Sources

Edit `06_research_data_collection.py` to:
- Add real data sources (APIs, web scraping)
- Update market share data
- Adjust financial trends
- Add more competitors

### Customize Figures

Modify figure generation functions to:
- Change colors
- Adjust sizes
- Add annotations
- Modify styles

## Data Sources

Currently uses estimated data based on:
- Industry reports
- Public financial data
- Market research estimates

**To add real data sources:**
1. Add API integrations (e.g., financial data APIs)
2. Implement web scraping (respect robots.txt)
3. Import from CSV/Excel files
4. Connect to databases

## Requirements

```bash
pip install -r requirements.txt
```

Required packages:
- pandas
- numpy
- matplotlib
- seaborn
- requests (for web scraping)
- beautifulsoup4 (for web scraping)

## Notes

- Figures are generated with trilingual labels
- All figures use consistent color schemes
- Data is exported in multiple formats for flexibility
- Scripts are designed to be easily extensible
