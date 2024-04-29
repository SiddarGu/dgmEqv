import plotly.express as px
import os
import pandas as pd

# Given data in tabular form
data_str = """Product Category,Online Sales (%)
Electronics,25
Fashion & Apparel,20
Home & Garden,15
Health & Beauty,10
Food & Beverage,10
Books & Media,8
Sports & Outdoors,7
Toys & Games,5"""

# Convert the string data to a pandas DataFrame
data = pd.DataFrame([x.split(',') for x in data_str.split('\n')])
data.columns = data.iloc[0]
data = data[1:]
data['Online Sales (%)'] = pd.to_numeric(data['Online Sales (%)'])

# Extract line_labels, data_labels, and data
line_labels = data['Product Category'].tolist()
data_labels = ["Online Sales (%)"]
data_values = data['Online Sales (%)'].tolist()

# Create treemap figure
fig = px.treemap(
    data,
    path=[px.Constant("E-commerce Sales"), 'Product Category'],
    values='Online Sales (%)',
    title='E-commerce Sales Distribution Across Retail Categories in 2023'
)

# Update the layout for better visuals
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
)

# Save image to the specified path
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_dir, exist_ok=True)  # make sure the directory exists
fig.write_image(save_dir + "40.png")

# No need to clear the state, as each Plotly figure is independent of the others
