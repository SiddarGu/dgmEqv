import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from io import StringIO

# Given data in CSV format
data_str = """Produce Type,Production Share (%)
Cereals,22
Vegetables,18
Fruits,20
Meat,17
Dairy,15
Fisheries,5
Sugarcane,3"""

# Convert string data to a pandas DataFrame
data_io = StringIO(data_str)
df = pd.read_csv(data_io)

# Create the treemap
fig = px.treemap(df, path=['Produce Type'], values='Production Share (%)',
                 title='Global Agriculture: Food Production Share by Produce Type',
                 color='Production Share (%)', color_continuous_scale='RdYlGn')

# Update layout for better appearance
fig.update_traces(textinfo='label+percent entry')
fig.update_layout(coloraxis_colorbar=dict(title="Share (%)"))

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/187.png")

# Clear the current image state
fig.data = []
