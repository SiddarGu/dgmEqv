import plotly.express as px
import os

# Input data
raw_data = """Property Type,Market Share (%)
Single-Family Homes,35
Apartments,25
Condominiums,15
Townhouses,10
Manufactured Housing,5
Multi-Family Units,5
Vacation Homes,3
Commercial Real Estate,2"""

# Parse the data into the required formats
rows = raw_data.split('\n')
data_labels = rows[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in rows[1:]]
data = [[float(row.split(',')[1])] for row in rows[1:]]

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Reset index to convert the index into a column
df = df.reset_index()
df.columns = ['Property Type', 'Market Share (%)']

# Generate a treemap
fig = px.treemap(df, path=['Property Type'], values='Market Share (%)', title='Housing Market Distribution by Property Type')

# Customize the layout to be more fancy, if desired
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    treemapcolorway=["#B8E986", "#8FBC94", "#F2D7D9", "#F2B9B9", "#F2E2E2", "#D3F2E2", "#58947C"],
    font=dict(size=18)
)

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1017.png'

# Create directories if they do not exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# If for some reason you need to clear the current image state (which is generally not needed with Plotly)
fig = None
