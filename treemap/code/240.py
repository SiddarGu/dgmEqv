import plotly.express as px
import os

# Data formatted as given in the prompt
data_str = """Crop Type,Production Volume (%)
Cereals,30
Vegetables,20
Fruits,20
Meat,15
Dairy,10
Oils & Fats,3
Sugar Crops,2"""

# Process the string data
lines = data_str.split("\n")
data_labels = lines[0].split(",")[1:]  # Assumes only one label after 'Crop Type'
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [int(line.split(",")[1]) for line in lines[1:]]

# Create a DataFrame
import pandas as pd
df = pd.DataFrame({
    'Crop Type': line_labels,
    'Production Volume (%)': data
})

# Create a treemap using plotly
fig = px.treemap(df, path=['Crop Type'], values='Production Volume (%)',
                 title='Percentage Distribution of Global Agriculture Production by Crop Type')

# Enhance treemap appearance
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/240.png'
# Create directories if they don't exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# No current image state to clear when using plotly
