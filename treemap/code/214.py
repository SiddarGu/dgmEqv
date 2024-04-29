import plotly.express as px
import os

# Define the data
data_labels = ["Product Type", "Production Volume (%)"]
line_labels = ["Electronics", "Automobiles", "Pharmaceuticals", "Heavy Machinery",
               "Food & Beverages", "Textiles", "Plastics", "Paper Products"]
data = [22, 20, 18, 15, 10, 8, 4, 3]

# Transform data into a dictionary for easier processing with Plotly
data_dict = {"Product Type": line_labels, "Production Volume (%)": data}

# Create a DataFrame from the dictionary
import pandas as pd
df = pd.DataFrame(data_dict)

# Create the treemap
fig = px.treemap(df, path=["Product Type"], values="Production Volume (%)",
                 title='Proportional Distribution of Manufacturing Production Volume by Product Type',
                 color="Production Volume (%)",
                 color_continuous_scale='RdBu',
                 range_color=[0, max(data)])

# Customize figure layout
fig.update_layout(margin=dict(l=10, r=10, t=30, b=10))

# Define the file path
file_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/214.png'
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Save the figure
fig.write_image(file_path)

# Clear the current image state to prevent interference with other plots (if necessary)
fig.data = []
