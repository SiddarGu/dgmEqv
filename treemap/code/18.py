import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Energy Source,Usage (%)
Solar,30
Wind,25
Hydropower,18
Geothermal,12
Biomass,10
Nuclear,5
"""

# Transform the data into variables
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [int(line.split(',')[1]) for line in lines[1:]]

# Plotting the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral(range(len(data)))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)
plt.title('Renewable Energy Usage in Sustainable Development 2023')

# Wrap the text if the labels are too long
for label in plt.gca().texts:
    text = label.get_text()
    if len(text) > 10:
        label.set_text('\n'.join(text.strip().split()))
    label.set_fontsize(10)

# Adjust the layout to fit everything, and then save the image
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/18.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
