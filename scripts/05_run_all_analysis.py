"""
Master script to run all analysis scripts
"""

import os
import sys
import importlib.util
from datetime import datetime

# Helper function to import modules with numeric names
def import_module_from_file(module_name, file_path):
    """Import a module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Import all analyzers dynamically
market_module = import_module_from_file("market_analysis", 
                                       os.path.join(script_dir, "01_market_data_analysis.py"))
financial_module = import_module_from_file("financial_analysis", 
                                          os.path.join(script_dir, "02_financial_analysis.py"))
competitive_module = import_module_from_file("competitive_analysis", 
                                             os.path.join(script_dir, "03_competitive_analysis.py"))
scraper_module = import_module_from_file("web_scraper", 
                                         os.path.join(script_dir, "04_web_scraper.py"))

EdekaMarketAnalyzer = market_module.EdekaMarketAnalyzer
EdekaFinancialAnalyzer = financial_module.EdekaFinancialAnalyzer
CompetitiveAnalyzer = competitive_module.CompetitiveAnalyzer
EdekaWebScraper = scraper_module.EdekaWebScraper

def run_all_analyses():
    """Run all analysis scripts"""
    print("=" * 80)
    print("COMPREHENSIVE EDEKA ANALYSIS")
    print("=" * 80)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Create results directory
    os.makedirs("results", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    results = {}
    
    try:
        # 1. Market Analysis
        print("\n" + "=" * 80)
        print("1. MARKET DATA ANALYSIS")
        print("=" * 80)
        market_analyzer = EdekaMarketAnalyzer()
        results['market'] = market_analyzer.generate_report()
        
    except Exception as e:
        print(f"Error in market analysis: {str(e)}")
        results['market'] = None
    
    try:
        # 2. Financial Analysis
        print("\n" + "=" * 80)
        print("2. FINANCIAL ANALYSIS")
        print("=" * 80)
        financial_analyzer = EdekaFinancialAnalyzer()
        results['financial'] = financial_analyzer.generate_report()
        
    except Exception as e:
        print(f"Error in financial analysis: {str(e)}")
        results['financial'] = None
    
    try:
        # 3. Competitive Analysis
        print("\n" + "=" * 80)
        print("3. COMPETITIVE ANALYSIS")
        print("=" * 80)
        competitive_analyzer = CompetitiveAnalyzer()
        results['competitive'] = competitive_analyzer.generate_report()
        
    except Exception as e:
        print(f"Error in competitive analysis: {str(e)}")
        results['competitive'] = None
    
    try:
        # 4. Web Scraping
        print("\n" + "=" * 80)
        print("4. WEB SCRAPING")
        print("=" * 80)
        scraper = EdekaWebScraper()
        scraper.run_scraping()
        results['scraping'] = "Completed"
        
    except Exception as e:
        print(f"Error in web scraping: {str(e)}")
        results['scraping'] = None
    
    # Summary
    print("\n" + "=" * 80)
    print("ANALYSIS SUMMARY")
    print("=" * 80)
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for analysis_type, result in results.items():
        status = "✓ Completed" if result is not None else "✗ Failed"
        print(f"{analysis_type.upper()}: {status}")
    
    print("\n" + "=" * 80)
    print("All results saved to 'results/' directory")
    print("=" * 80)

if __name__ == "__main__":
    run_all_analyses()
