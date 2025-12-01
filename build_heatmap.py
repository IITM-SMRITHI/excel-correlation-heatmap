#!/usr/bin/env python3
import csv
from PIL import Image, ImageDraw
import colorsys

def read_correlation_matrix(filename):
    """Read correlation matrix from CSV."""
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Skip header
        for row in reader:
            data.append([float(x) for x in row[1:]])  # Skip first column (names)
    return data, headers[1:]

def value_to_color(value):
    """Convert correlation value (-1 to 1) to RGB color."""
    # Red (negative) to White (zero) to Green (positive)
    if value < 0:
        # Red to White
        t = -value  # 0 to 1
        r = 255
        g = int(255 * (1 - t))
        b = int(255 * (1 - t))
    else:
        # White to Green
        t = value  # 0 to 1
        r = int(255 * (1 - t))
        g = 255
        b = int(255 * (1 - t))
    return (r, g, b)

def create_heatmap_image(data, size=512, cell_size=None):
    """Create a heatmap image from correlation matrix."""
    n = len(data)
    if cell_size is None:
        cell_size = size // n
    
    # Create image
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw cells
    for i in range(n):
        for j in range(n):
            value = data[i][j]
            color = value_to_color(value)
            
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size - 1
            y1 = y0 + cell_size - 1
            
            draw.rectangle([x0, y0, x1, y1], fill=color)
            draw.rectangle([x0, y0, x1, y1], outline='gray')
    
    return img

if __name__ == '__main__':
    try:
        # Read correlation matrix
        data, labels = read_correlation_matrix('correlation.csv')
        
        # Create heatmap image (512x512)
        img = create_heatmap_image(data, size=512)
        
        # Save
        img.save('heatmap.png')
        print('Heatmap created: heatmap.png (512x512)')
    except Exception as e:
        print(f'Error: {e}')
        import traceback
        traceback.print_exc()
