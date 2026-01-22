"""
Example usage of the research data collection script
This demonstrates how to use the generated figures in your book
"""

from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.research_data_collection import EdekaResearchCollector

def example_usage():
    """Example of how to use the research collector"""
    
    print("Example: Generating Research Figures for Edeka Book")
    print("=" * 60)
    
    # Initialize collector
    collector = EdekaResearchCollector()
    
    # Generate all figures
    collector.generate_all_figures()
    
    # Access generated data
    market_data = collector.get_market_share_data()
    financial_data = collector.get_financial_trends()
    
    print("\n" + "=" * 60)
    print("Sample Data:")
    print("=" * 60)
    print("\nMarket Share Data:")
    print(market_data.head())
    
    print("\nFinancial Trends:")
    print(financial_data)
    
    print("\n" + "=" * 60)
    print("Figures generated in: results/figures/")
    print("Data exported to: data/")
    print("=" * 60)

if __name__ == "__main__":
    example_usage()
