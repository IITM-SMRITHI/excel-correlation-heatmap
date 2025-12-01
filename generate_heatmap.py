import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create correlation matrix from CSV data
data = pd.read_csv('correlation.csv', index_col=0)

# Create heatmap with Red-White-Green color scheme
plt.figure(figsize=(8, 8), dpi=64)  # 512x512 pixels at 64 DPI
sns.heatmap(data, annot=True, fmt='.2f', cmap='RdYlGn', center=0,
            cbar_kws={'label': 'Correlation'}, vmin=-1, vmax=1,
            linewidths=0.5, linecolor='gray')
plt.title('Supply Chain Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=64, bbox_inches='tight')
print('Heatmap saved as heatmap.png')
