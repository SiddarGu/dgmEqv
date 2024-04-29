import plotly.express as px
import os

# Given data
raw_data = """
Product Category,Sales Share (%)
Carbonated Drinks,22
Alcoholic Beverages,20
Bottled Water,17
Snack Foods,16
Tea and Coffee,10
Dairy Products,8
Organic Foods,5
Baby Food,2
"""

# Parsing the data to extract line_labels, data_labels, and data
lines = raw_data.strip().split('\n')
data_labels = [lines[0].split(',')[0]]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [[int(line.split(',')[1])] for line in lines[1:]]

# Create a DataFrame for the treemap
import pandas as pd
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Reset index to turn the line_labels into a column in the DataFrame
df.reset_index(inplace=True)
df.columns = ['Product Category', 'Sales Share (%)']

# Create a treemap
fig = px.treemap(df, path=['Product Category'], values='Sales Share (%)',
                 title='Market Sales Distribution in the Food and Beverage Industry')

# Set figure layout
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

# Set directory to save the image
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save the figure
fig.write_image(f"{save_dir}195.png")

# Clear the current image state if needed
fig = None
