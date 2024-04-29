import plotly.express as px
import os

# Data preparation
raw_data = """Housing Type,Sales Volume (%)
Single-Family Homes,35
Condominiums,25
Townhouses,15
Multi-Family Buildings,10
Manufactured Homes,5
Vacation Homes,5
Co-ops,3
Luxury Residences,2"""

# Parse the given data into lists
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create a data frame for plotting
import pandas as pd
df = pd.DataFrame({'Housing Type': line_labels, 'Sales Volume (%)': data})

# Plot the treemap
fig = px.treemap(df, path=['Housing Type'], values='Sales Volume (%)',
                 title='Sales Distribution Across Housing Types in the Real Estate Market')

# Make the treemap more visually appealing
fig.update_traces(textinfo="label+value", textfont=dict(size=18))
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png'
os.makedirs(save_path, exist_ok=True)
fig.write_image(f"{save_path}/1049.png")

# Clear the figure
fig.data = []
