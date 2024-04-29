import matplotlib.pyplot as plt
import squarify

# Data provided
data_input = """
Finance Category,Investment (%)
Banking,20
Cryptocurrency,18
Stock Market,22
Real Estate,15
Hedge Funds,10
Private Equity,8
Venture Capital,4
Bonds,3
"""

# Parse the data into usable lists
lines = data_input.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # Column labels except the first
line_labels = [row.split(',')[0] for row in lines[1:]]  # Row labels except the first column
data = [float(row.split(',')[1]) for row in lines[1:]]  # Numerical data

# Color palette for the treemap
colors = plt.cm.Spectral_r([i/len(data) for i in range(len(data))])

# Plotting with squarify
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6)
plt.title('Portfolio Diversification in Business and Finance in 2023', fontsize=18)
plt.axis('off')  # Disable axes

# Make the image layout fit perfectly before saving
plt.tight_layout()

# Save the figure to the specified path, ensuring directory exists
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/139.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current figure state to prevent overlap in future plots
plt.clf()
