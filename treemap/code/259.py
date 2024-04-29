import plotly.graph_objects as go

# Given data string parsing into variables: data_labels, line_labels, and data
data_string = """Platform Category,Active Users (%)
Social Networking,35
Microblogging,20
Video Sharing,15
Online Forums,10
Messaging Apps,9
Content Communities,6
News Aggregates,5"""

# Parsing the data into lists
lines = data_string.split('\n')
data_labels = lines[0].split(',')[1:] # ['Active Users (%)']
line_labels = [line.split(',')[0] for line in lines[1:]] # ['Social Networking', 'Microblogging', ...]
data = [float(line.split(',')[1]) for line in lines[1:]] # [35, 20, ...]

# Creating the treemap figure
fig = go.Figure(go.Treemap(
    labels=line_labels,
    parents=['' for _ in line_labels],  # No parents since it's the first level of the tree
    values=data,
    textinfo='label+value+percent entry',
    outsidetextfont={'size': 20},  # Adjust the font size if the text is too long
))

# Update layout properties
fig.update_layout(
    title='Proportion of Active Users Across Web and Social Media Platforms',
    margin={'t': 50, 'l': 25, 'r': 25, 'b': 25}  # Adjusting margins if necessary
)

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1009.png'
fig.write_image(save_path, scale=2)

# Clearing the figure (not directly supported by Plotly, as figures are generally immutable)
# Instead, you can just reuse a new 'go.Figure()' when plotting another chart
