import plotly.express as px
import os

data = {
    'Product Category': ['Packaged Foods', 'Beverages', 'Fresh Produce', 'Dairy Products', 
                         'Confectionery', 'Meat & Poultry', 'Seafood', 'Baked Goods'],
    'Market Share (%)': [30, 25, 15, 10, 8, 7, 3, 2]
}

data_labels = ['Product Category']
line_labels = [label for label in data['Product Category']]
data_values = data['Market Share (%)']

fig = px.treemap(
    names=line_labels,
    parents=[""] * len(data_values), # Root level
    values=data_values,
    title='Market Share Distribution in the Food and Beverage Industry'
)

fig.update_traces(textinfo="label+percent entry")
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
)

save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/231.png'
# Make sure that the directory exists, if not, create it
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the current image state if needed (useful in interactive environments like Jupyter Notebooks)
fig.show()
