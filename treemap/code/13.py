import plotly.express as px
import plotly.graph_objects as go
import os

# Given raw data
raw_data = """Product Category,Online Sales (%)
Electronics,25
Clothing,20
Home & Garden,15
Health & Beauty,12
Food & Beverages,10
Books & Media,8
Sports & Outdoors,5
Toys & Hobbies,3
Office Supplies,2"""

# Parse the raw_data and split by new lines and commas
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create a DataFrame for the treemap
import pandas as pd

df = pd.DataFrame({
    'Category': line_labels,
    'Sales (%)': data
})

# Create the treemap
fig = px.treemap(df, path=['Category'], values='Sales (%)', title='E-commerce Sales Distribution by Product Category in 2023')

# Update layout to make it fancy
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880", "#FF97FF"],
)

# Make sure the save path directory exists
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the image
fig.write_image(f"{save_path}/13.png")
