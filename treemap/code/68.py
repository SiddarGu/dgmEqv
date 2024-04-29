import plotly.express as px
import plotly.graph_objects as go

# Define the data
data_str = """Real Estate Segment,Market Share (%)
Single-Family Homes,30
Apartments,25
Condominiums,20
Commercial Properties,15
Rental Markets,10"""

# Parse the data
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Transform into a suitable structure for the treemap
df = pd.DataFrame({
    'segment': line_labels,
    'market_share': data
})

# Create the treemap
fig = px.treemap(df, path=['segment'], values='market_share',
                 title='Real Estate Market Composition by Housing Segment')

# Customizing the treemap for aesthetics
fig.update_traces(textinfo='label+percent entry', marker=dict(line=dict(width=1)))
fig.update_layout(uniformtext=dict(minsize=10), title_font_size=24)

# Save the figure to the specified file
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/68.png")

# Clear the current image state (not needed as it is being saved to a file)
