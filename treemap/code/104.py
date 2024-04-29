import plotly.express as px
import plotly.graph_objects as go

# Data provided
data_string = """Transportation Mode,Logistics Market Share (%)
Road Freight,40
Maritime Transport,25
Air Freight,15
Rail Transport,10
Pipeline Transport,5
Intermodal Transport,3
Courier Services,2"""

# Parsing the data into lists
lines = data_string.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # Skip the first column which is 'Transportation Mode'
line_labels = [line.split(',')[0] for line in lines[1:]]
data_values = [float(line.split(',')[1]) for line in lines[1:]]

# Creating a dataframe
import pandas as pd
df = pd.DataFrame({
    'Transportation Mode': line_labels,
    'Logistics Market Share (%)': data_values
})

# Create treemap using plotly
fig = px.treemap(df, path=['Transportation Mode'], values='Logistics Market Share (%)',
                 title='Logistics Market Share by Transportation Mode', width=1000, height=500
)

# Set fancy attributes for treemap
fig.update_traces(textinfo="label+value", textfont_size=20, marker=dict(colors=px.colors.qualitative.Pastel))

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/104.png")

# Clear figure - This is done by freeing the memory of fig
fig = None
