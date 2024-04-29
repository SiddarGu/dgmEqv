import plotly.express as px
import plotly.graph_objects as go
import os

# Define your data
data_labels = ['Production Volume (%)']
line_labels = ['Cereals', 'Vegetables', 'Fruits', 'Meat', 'Dairy', 'Fish', 'Oilseeds', 'Spices']
data = [25, 20, 20, 15, 10, 5, 3, 2]

# Construct a dataframe for ease of use with Plotly
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Product Group', 'Production Volume (%)'])

# Create a treemap chart
fig = px.treemap(df, path=['Product Group'], values='Production Volume (%)',
                 title='Proportional Distribution of Global Agriculture and Food Production')

# Customize the chart to make it fancy
# Colors can be a predefined scale or a custom set defined by colorscale parameter
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(font_size=10, title_font_size=18)

# Define the absolute path for the image to be saved
image_save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/105.png'

# Ensure directory exists
os.makedirs(os.path.dirname(image_save_path), exist_ok=True)

# Save figure
fig.write_image(image_save_path)

# Clear current image state, Plotly doesn't require clearing like matplotlib
print(f"Treemap saved successfully at {image_save_path}")
