"""
Financial Analysis for Edeka
Analyzes financial metrics, profitability, and financial health
Note: Edeka is not publicly traded, so data availability is limited
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class EdekaFinancialAnalyzer:
    """Financial analyzer for Edeka"""
    
    def __init__(self):
        self.results_dir = "results"
        
    def get_financial_data(self):
        """Get financial data (placeholder - actual data from annual reports)"""
        # This would typically come from annual reports or financial databases
        financial_data = {
            'Year': [2019, 2020, 2021, 2022, 2023],
            'Revenue_Billion_EUR': [58.5, 59.8, 61.2, 62.5, 63.8],  # Estimated
            'Employees': [370000, 375000, 378000, 380000, 382000],  # Estimated
            'Stores': [10800, 10900, 11000, 11050, 11100]  # Estimated
        }
        return pd.DataFrame(financial_data)
    
    def calculate_financial_metrics(self, df):
        """Calculate key financial metrics"""
        metrics = {}
        
        # Revenue per employee
        df['Revenue_Per_Employee'] = (df['Revenue_Billion_EUR'] * 1000) / df['Employees']
        
        # Revenue per store
        df['Revenue_Per_Store_Million'] = (df['Revenue_Billion_EUR'] * 1000) / df['Stores']
        
        # Growth rates
        df['Revenue_Growth_Percent'] = df['Revenue_Billion_EUR'].pct_change() * 100
        df['Employee_Growth_Percent'] = df['Employees'].pct_change() * 100
        
        return df
    
    def analyze_financial_trends(self):
        """Analyze financial trends over time"""
        df = self.get_financial_data()
        df = self.calculate_financial_metrics(df)
        
        print("=" * 60)
        print("EDEKA FINANCIAL ANALYSIS")
        print("=" * 60)
        
        print("\nKey Metrics (Latest Year):")
        latest = df.iloc[-1]
        print(f"Revenue: {latest['Revenue_Billion_EUR']:.2f} Billion EUR")
        print(f"Employees: {latest['Employees']:,}")
        print(f"Stores: {latest['Stores']:,}")
        print(f"Revenue per Employee: {latest['Revenue_Per_Employee']:.2f} Million EUR")
        print(f"Revenue per Store: {latest['Revenue_Per_Store_Million']:.2f} Million EUR")
        
        print("\nGrowth Trends:")
        avg_revenue_growth = df['Revenue_Growth_Percent'].mean()
        print(f"Average Revenue Growth: {avg_revenue_growth:.2f}%")
        
        # Create visualizations
        self.plot_revenue_trend(df)
        self.plot_efficiency_metrics(df)
        
        return df
    
    def plot_revenue_trend(self, df):
        """Plot revenue trend over time"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        ax.plot(df['Year'], df['Revenue_Billion_EUR'], 
               marker='o', linewidth=2, markersize=8, color='#FF6B6B')
        ax.fill_between(df['Year'], df['Revenue_Billion_EUR'], alpha=0.3, color='#FF6B6B')
        
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Revenue (Billion EUR)', fontsize=12)
        ax.set_title('Edeka Revenue Trend', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        
        # Add value labels
        for x, y in zip(df['Year'], df['Revenue_Billion_EUR']):
            ax.text(x, y, f'{y:.1f}', ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(f'{self.results_dir}/revenue_trend.png', dpi=300, bbox_inches='tight')
        print(f"\nSaved: {self.results_dir}/revenue_trend.png")
        plt.close()
    
    def plot_efficiency_metrics(self, df):
        """Plot efficiency metrics"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Revenue per employee
        ax1.plot(df['Year'], df['Revenue_Per_Employee'], 
                marker='s', linewidth=2, markersize=8, color='#4ECDC4')
        ax1.set_xlabel('Year', fontsize=11)
        ax1.set_ylabel('Revenue per Employee (Million EUR)', fontsize=11)
        ax1.set_title('Revenue per Employee', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Revenue per store
        ax2.plot(df['Year'], df['Revenue_Per_Store_Million'], 
                marker='^', linewidth=2, markersize=8, color='#45B7D1')
        ax2.set_xlabel('Year', fontsize=11)
        ax2.set_ylabel('Revenue per Store (Million EUR)', fontsize=11)
        ax2.set_title('Revenue per Store', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{self.results_dir}/efficiency_metrics.png', dpi=300, bbox_inches='tight')
        print(f"Saved: {self.results_dir}/efficiency_metrics.png")
        plt.close()
    
    def generate_report(self):
        """Generate financial analysis report"""
        df = self.analyze_financial_trends()
        df.to_csv(f'{self.results_dir}/financial_data.csv', index=False)
        print(f"\nSaved data: {self.results_dir}/financial_data.csv")
        return df

if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    
    analyzer = EdekaFinancialAnalyzer()
    analyzer.generate_report()
