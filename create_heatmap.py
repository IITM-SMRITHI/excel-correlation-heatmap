#!/usr/bin/env python3
"""
Create a heatmap PNG from correlation matrix CSV.
This script reads correlation.csv and generates heatmap.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import base64

def create_heatmap():
    """Generate heatmap from correlation matrix."""
    
    # Read the correlation matrix
    df = pd.read_csv('correlation.csv', index_col=0)
    
    # Create figure with specific size for 512x512 output
    fig, ax = plt.subplots(figsize=(8, 8), dpi=64)
    
    # Create heatmap with Red-White-Green color scheme
    sns.heatmap(
        df, 
        annot=True, 
        fmt='.2f', 
        cmap='RdYlGn',  # Red-Yellow-Green colormap
        center=0,
        cbar_kws={'label': 'Correlation'},
        ax=ax,
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        linecolor='gray'
    )
    
    plt.title('Supply Chain Metrics - Correlation Matrix', fontsize=12, fontweight='bold')
    plt.xlabel('Metrics', fontsize=10)
    plt.ylabel('Metrics', fontsize=10)
    plt.tight_layout()
    
    # Save as PNG with 512x512 dimensions
    plt.savefig('heatmap.png', dpi=64, bbox_inches='tight', format='png')
    print('Heatmap saved as heatmap.png')
    plt.close()

if __name__ == '__main__':
    try:
        create_heatmap()
        print('Success! heatmap.png created (512x512 pixels approx)')
    except Exception as e:
        print(f'Error: {e}')
        import traceback
        traceback.print_exc()
