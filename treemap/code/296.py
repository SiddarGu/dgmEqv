import matplotlib.pyplot as plt
import squarify

# Parsing the provided data
data_str = """Industry,Market Share (%)
Banking,25
Insurance,20
Real Estate,15
Investment,10
Manufacturing,10
Retail,8
Information Technology,7
Healthcare,5"""

# Splitting the data into lines and extracting labels and numerical values
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # Exclude 'Industry' label
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)
plt.title('Market Share Distribution Across Business and Finance Sectors')

# Improving layout and saving the figure
plt.axis('off')
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1046.png'
plt.savefig(save_path, format='png')
plt.clf()  # Clear the current figure
