import plotly.express as px

# Parsing the given data
raw_data = "Cereals,30/n Vegetables,22/n Fruits,18/n Meat,15/n Dairy,10/n Fishery,5"
parsed_data = [item.split(',') for item in raw_data.split('/n ')]
line_labels = [item[0] for item in parsed_data]  # Labels for each row
data = [float(item[1]) for item in parsed_data]  # Numeric data

# Preparing the data for the treemap
df = {
    'Crop Type': line_labels,
    'Production Share (%)': data
}

# Create a treemap
fig = px.treemap(df, path=['Crop Type'], values='Production Share (%)',
                 title='Global Agriculture: Production Share by Crop Type')

# Customize the layout
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/147.png")
