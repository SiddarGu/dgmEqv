import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_str = """Product Type,Annual Sales ($ Billion)
Packaged Foods,63.4
Fresh Produce,38.2
Beverages,72.9
Meat and Poultry,55.3
Dairy Products,47.1
Confectionery,29.8
Bakery Products,33.7
Seafood Products,22.6"""

# Convert the string data into a pandas DataFrame
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data_values = [float(line.split(',')[1]) for line in data_lines[1:]]
data = pd.DataFrame(data_values, index=line_labels, columns=data_labels)

# Create a figure and a histogram
plt.figure(figsize=(12, 6))
ax = plt.subplot()
data.plot(kind='bar', ax=ax, legend=True, grid=True, color=['#619CFF', '#F8766D', '#00BA38'])

# Set title and labels
plt.title('Annual Sales in the Food and Beverage Industry by Product Type')
plt.xlabel('Product Type')
plt.xticks(rotation=30, ha='right', wrap=True)
plt.ylabel('Annual Sales ($ Billion)')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/609.png')

# Clear the current image state
plt.clf()
