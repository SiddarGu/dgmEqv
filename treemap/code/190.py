import plotly.express as px
import plotly.graph_objects as go
import os

# Break data into variables
data_labels = ['Freight Volume (%)']
line_labels = ['Road', 'Rail', 'Air', 'Maritime', 'Pipeline', 'Intermodal']
data = [40, 20, 15, 14, 6, 5]

# Combine line labels and data into a single DataFrame for Plotly
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Transportation Type', 'Freight Volume (%)'])

# Draw treemap
fig = px.treemap(df, path=['Transportation Type'], values='Freight Volume (%)',
                 title='Freight Volume Distribution Across Transportation Modes')

# Make the image fancy by setting color and other layout properties
fig.update_traces(textinfo="label+value", textfont_size=12)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Set the absolute path for the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/190.png'

# Ensure directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the current image state (Not needed in Plotly as each fig is independent)
