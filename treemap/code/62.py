import plotly.express as px
import plotly.graph_objects as go
import os

# Data transformation
data_labels = ['Sales Volume (%)']
line_labels = ['Single-Family Homes', 'Apartments', 'Townhouses', 'Condominiums', 'Duplexes', 
               'Vacation Homes', 'Luxury Estates', 'Manufactured Homes']
data = [30, 25, 15, 10, 7, 5, 5, 3]

# Create a DataFrame for the plot
import pandas as pd
df = pd.DataFrame({'Category': line_labels, 'Sales Volume (%)': data})

# Create the treemap
fig = px.treemap(df, path=['Category'], values='Sales Volume (%)',
                 title='Real Estate Sales Distribution by Housing Type')

# Customize the layout
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure to the specified path, ensuring the directories exist
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_dir, exist_ok=True)
fig.write_image(f"{save_dir}/62.png")

# Clear the current image state by closing the figure
fig.show()
