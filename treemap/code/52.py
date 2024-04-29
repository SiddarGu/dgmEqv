import matplotlib.pyplot as plt
import squarify

# Given data in a string format, transform it into three variables.
data_str = "Category,Market Share (%)\nPackaged Foods,30\nBeverages,25\nFresh Produce,20\nMeat & Seafood,15\nDairy Products,10"

# Parsing the data string into line_labels, data_labels, and data.
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Plotting the treemap.
plt.figure(figsize=(12, 8))  # Making the figure larger to prevent content from being unreadable.
squarify.plot(sizes=data, label=line_labels, color=None, alpha=0.8, text_kwargs={'fontsize':10, 'wrap':True})

# Adding title and making it fancy.
plt.title('Market Share Distribution in the Food and Beverage Industry', fontsize=15)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# Saving the figure.
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/52.png'
plt.savefig(save_path, format='png')

# Clearing the current image state at the end of the code.
plt.clf()
plt.close()
