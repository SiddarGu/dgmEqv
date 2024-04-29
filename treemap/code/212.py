import os
import plotly.express as px

# Given data, transformed into respective variables
data_labels = ["Policy Spending (%)"]
line_labels = [
    "Healthcare", "Education", "Defense", "Social Security",
    "Infrastructure", "Energy", "Science & Research", "Environment", "Agriculture"
]
data = [25, 20, 15, 15, 10, 5, 5, 3, 2]

# Prepare the data for plotting
df = {
    'Category': line_labels,
    'Spending': data
}

# Create a treemap
fig = px.treemap(
    df,
    path=['Category'],
    values='Spending',
    title='Allocation of Government Spending on Public Policy Categories',
    color='Spending',  # Column with numerical data to define the color
    color_continuous_scale='RdBu',  # Custom color scale for aesthetics
)

# Adjust layout for a fancy look
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),  # Tight layout
)
fig.update_traces(
    textinfo="label+value",  # Show both label and value on the map
    textfont=dict(size=18),  # Custom font size
)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1106.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Create directories if they don't exist
fig.write_image(save_path)

# Clear the figure to avoid state issues, not necessary in plotly as it does not maintain state like matplotlib
# fig = None
