import plotly.express as px

# Prepare the data
data_labels = ["Sales Share (%)"]
line_labels = ["Electronics", "Apparel", "Home & Garden", "Health & Beauty",
               "Food & Beverages", "Sports & Outdoors", "Toys & Hobbies", "Books", "Stationery"]
data = [25, 20, 15, 13, 12, 8, 4, 2, 1]

# Combine the data into a single structure suitable for Plotly
treemap_data = {
    'Product Category': line_labels,
    'Sales Share (%)': data
}

# Create the treemap
fig = px.treemap(
    treemap_data,
    path=['Product Category'],
    values='Sales Share (%)',
    title='Retail and E-commerce Sales Distribution by Product Category',
)

# Customize the layout and appearance
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

# Save the figure as a PNG
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/184.png'
fig.write_image(save_path)

# Clear the current image state, not necessary in the context of a script
