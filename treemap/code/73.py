import matplotlib.pyplot as plt
import squarify

# Data
data_str = """Investment Banking,25
Asset Management,20
Retail Banking,15
Insurance,15
Private Equity,10
Fintech,8
Wealth Management,4
Cryptocurrency,3"""

# Transforming the data into required formats
data_lines = data_str.split('\n')
line_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]

# Drawing the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral(range(len(data)))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6)

plt.title('Market Share Distribution in the Financial Industry')
plt.axis('off')

# Resizing the image
plt.tight_layout()

# Saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1043.png'
plt.savefig(save_path, format='png')

# Clearing the current image state
plt.clf()
