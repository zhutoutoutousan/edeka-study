"""
Competitive Analysis for Edeka
Analyzes competitive landscape and positioning
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CompetitiveAnalyzer:
    """Analyzer for competitive landscape"""
    
    def __init__(self):
        self.results_dir = "results"
        
    def get_competitor_data(self):
        """Get competitor data"""
        competitors = {
            'Company': ['Edeka', 'Rewe', 'Aldi', 'Lidl', 'Kaufland'],
            'Market_Share': [26.0, 15.0, 12.0, 10.0, 8.0],
            'Revenue_Billion': [60, 35, 28, 24, 18],
            'Stores': [11000, 6500, 4500, 3200, 1300],
            'Strategy': ['Differentiation', 'Differentiation', 'Price Leadership', 
                       'Price Leadership', 'Hypermarket'],
            'Private_Label_Share': [35, 30, 90, 85, 25]  # Estimated percentage
        }
        return pd.DataFrame(competitors)
    
    def analyze_competitive_positioning(self):
        """Analyze competitive positioning"""
        df = self.get_competitor_data()
        
        print("=" * 60)
        print("COMPETITIVE ANALYSIS")
        print("=" * 60)
        
        # Market concentration
        top3_share = df.nlargest(3, 'Market_Share')['Market_Share'].sum()
        print(f"\nTop 3 Market Share: {top3_share:.1f}%")
        print(f"Market Concentration (HHI): {self.calculate_hhi(df):.0f}")
        
        # Edeka's position
        edeka = df[df['Company'] == 'Edeka'].iloc[0]
        print(f"\nEdeka Position:")
        print(f"  Market Share: {edeka['Market_Share']:.1f}% (Leader)")
        print(f"  Revenue: {edeka['Revenue_Billion']:.1f} Billion EUR")
        print(f"  Strategy: {edeka['Strategy']}")
        
        # Create visualizations
        self.plot_competitive_matrix(df)
        self.plot_market_share_comparison(df)
        
        return df
    
    def calculate_hhi(self, df):
        """Calculate Herfindahl-Hirschman Index"""
        return (df['Market_Share'] ** 2).sum()
    
    def plot_competitive_matrix(self, df):
        """Plot competitive positioning matrix"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create positioning based on market share and strategy
        for idx, row in df.iterrows():
            x = row['Market_Share']
            y = row['Private_Label_Share']
            ax.scatter(x, y, s=row['Revenue_Billion']*50, 
                     alpha=0.6, label=row['Company'])
            ax.annotate(row['Company'], (x, y), 
                       xytext=(5, 5), textcoords='offset points', fontsize=10)
        
        ax.set_xlabel('Market Share (%)', fontsize=12)
        ax.set_ylabel('Private Label Share (%)', fontsize=12)
        ax.set_title('Competitive Positioning Matrix', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{self.results_dir}/competitive_matrix.png', dpi=300, bbox_inches='tight')
        print(f"\nSaved: {self.results_dir}/competitive_matrix.png")
        plt.close()
    
    def plot_market_share_comparison(self, df):
        """Plot market share comparison"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        colors = ['#FF6B6B' if x == 'Edeka' else '#4ECDC4' for x in df['Company']]
        bars = ax.barh(df['Company'], df['Market_Share'], color=colors)
        
        ax.set_xlabel('Market Share (%)', fontsize=12)
        ax.set_ylabel('Company', fontsize=12)
        ax.set_title('Market Share Comparison', fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, (bar, share) in enumerate(zip(bars, df['Market_Share'])):
            ax.text(share, i, f' {share:.1f}%', 
                   va='center', fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f'{self.results_dir}/market_share_comparison.png', dpi=300, bbox_inches='tight')
        print(f"Saved: {self.results_dir}/market_share_comparison.png")
        plt.close()
    
    def generate_report(self):
        """Generate competitive analysis report"""
        df = self.analyze_competitive_positioning()
        df.to_csv(f'{self.results_dir}/competitive_data.csv', index=False)
        print(f"\nSaved data: {self.results_dir}/competitive_data.csv")
        return df

if __name__ == "__main__":
    import os
    os.makedirs("results", exist_ok=True)
    
    analyzer = CompetitiveAnalyzer()
    analyzer.generate_report()
