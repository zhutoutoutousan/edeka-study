"""
Market Data Analysis for Edeka
Analyzes market position, competitors, and industry trends
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json

# Set style for plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class EdekaMarketAnalyzer:
    """Analyzer for Edeka market data"""
    
    def __init__(self):
        self.data_dir = "data"
        self.results_dir = "results"
        
    def get_market_share_data(self):
        """Get market share data for German retail market"""
        # This is placeholder data - replace with actual data sources
        market_data = {
            'Company': ['Edeka', 'Rewe', 'Aldi', 'Lidl', 'Kaufland', 'Others'],
            'Market_Share_Percent': [26.0, 15.0, 12.0, 10.0, 8.0, 29.0],
            'Revenue_Billion_EUR': [60, 35, 28, 24, 18, 65],
            'Store_Count': [11000, 6500, 4500, 3200, 1300, 15000]
        }
        return pd.DataFrame(market_data)
    
    def analyze_market_position(self):
        """Analyze Edeka's market position"""
        df = self.get_market_share_data()
        
        # Calculate metrics
        total_market = df['Revenue_Billion_EUR'].sum()
        edeka_share = df[df['Company'] == 'Edeka']['Market_Share_Percent'].values[0]
        
        print("=" * 60)
        print("EDEKA MARKET POSITION ANALYSIS")
        print("=" * 60)
        print(f"\nTotal Market Size: {total_market:.1f} Billion EUR")
        print(f"Edeka Market Share: {edeka_share:.1f}%")
        print(f"Edeka Revenue: {df[df['Company'] == 'Edeka']['Revenue_Billion_EUR'].values[0]:.1f} Billion EUR")
        
        # Create visualizations
        self.plot_market_share(df)
        self.plot_revenue_comparison(df)
        
        return df
    
    def plot_market_share(self, df):
        """Plot market share pie chart"""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
        wedges, texts, autotexts = ax.pie(
            df['Market_Share_Percent'],
            labels=df['Company'],
            autopct='%1.1f%%',
            startangle=90,
            colors=colors
        )
        
        ax.set_title('German Food Retail Market Share', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.results_dir}/market_share_pie.png', dpi=300, bbox_inches='tight')
        print(f"\nSaved: {self.results_dir}/market_share_pie.png")
        plt.close()
    
    def plot_revenue_comparison(self, df):
        """Plot revenue comparison bar chart"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        bars = ax.bar(df['Company'], df['Revenue_Billion_EUR'], 
                     color=['#FF6B6B' if x == 'Edeka' else '#4ECDC4' for x in df['Company']])
        
        ax.set_xlabel('Company', fontsize=12)
        ax.set_ylabel('Revenue (Billion EUR)', fontsize=12)
        ax.set_title('Revenue Comparison: German Food Retail', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.0f}',
                   ha='center', va='bottom', fontsize=10)
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'{self.results_dir}/revenue_comparison.png', dpi=300, bbox_inches='tight')
        print(f"Saved: {self.results_dir}/revenue_comparison.png")
        plt.close()
    
    def calculate_growth_metrics(self):
        """Calculate growth metrics (placeholder - needs actual time series data)"""
        # This would require historical data
        print("\n" + "=" * 60)
        print("GROWTH METRICS")
        print("=" * 60)
        print("Note: Historical data needed for accurate growth calculations")
        print("This section requires time series data from annual reports")
    
    def generate_report(self):
        """Generate comprehensive market analysis report"""
        df = self.analyze_market_position()
        self.calculate_growth_metrics()
        
        # Save data to CSV
        df.to_csv(f'{self.results_dir}/market_data.csv', index=False)
        print(f"\nSaved data: {self.results_dir}/market_data.csv")
        
        return df

if __name__ == "__main__":
    import os
    
    # Create directories
    os.makedirs("data", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    
    analyzer = EdekaMarketAnalyzer()
    analyzer.generate_report()
