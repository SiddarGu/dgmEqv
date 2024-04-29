import plotly.express as px
import pandas as pd

# Data given
data_str = """Product Category,Online Sales (%)
Electronics,25
Clothing and Apparel,20
Home and Garden,15
Health and Beauty,15
Books and Media,10
Toys and Games,5
Food and Beverage,5
Sports and Outdoor,3
Automotive,2"""

# Parse data_str into a DataFrame
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')
rows = [line.split(',') for line in data_lines[1:]]
line_labels = [row[0] for row in rows]
data = [row[1] for row in rows]

# Convert data to DataFrame for Plotly
df = pd.DataFrame({
    data_labels[0]: line_labels,
    data_labels[1]: list(map(int, data))
})

# Plotting the treemap using Plotly
fig = px.treemap(df, path=[px.Constant('E-commerce Sales Distribution'), data_labels[0]],
                 values=data_labels[1],
                 title='E-commerce Sales Distribution Across Product Categories in 2023')

fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save figure to the specific path
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/146.png")

# If necessary, clear the figure after saving (not always required with Plotly)
fig.data = []
