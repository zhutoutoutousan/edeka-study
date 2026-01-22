"""
Master script to run all research and generate figures for the book
"""

import sys
import os
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent
sys.path.insert(0, str(scripts_dir))

# Import modules
import importlib.util

def import_module_from_file(module_name, file_path):
    """Import a module from a file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Import modules
research_module = import_module_from_file("research_data_collection", 
                                         scripts_dir / "06_research_data_collection.py")
figure_module = import_module_from_file("figure_integration", 
                                       scripts_dir / "07_figure_integration.py")

EdekaResearchCollector = research_module.EdekaResearchCollector
generate_latex_figure_includes = figure_module.generate_latex_figure_includes

def main():
    """Run all research and figure generation"""
    print("=" * 80)
    print("EDEKA RESEARCH DATA COLLECTION AND FIGURE GENERATION")
    print("=" * 80)
    print()
    
    # Step 1: Generate all figures
    print("STEP 1: Generating research figures...")
    print("-" * 80)
    collector = EdekaResearchCollector()
    collector.generate_all_figures()
    
    print("\n" + "=" * 80)
    
    # Step 2: Generate LaTeX integration code
    print("\nSTEP 2: Generating LaTeX integration code...")
    print("-" * 80)
    generate_latex_figure_includes()
    
    print("\n" + "=" * 80)
    print("RESEARCH COMPLETE!")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Review figures in results/figures/")
    print("2. Copy figures to book/figures/ directory")
    print("3. Use the LaTeX code from results/figures_latex_code.tex")
    print("4. Include figures in your chapters using \\includegraphics{}")

if __name__ == "__main__":
    main()
