import plotly.express as px
import plotly.graph_objects as go

# Input data in multiline string format
input_data = """Legal Sector,Total Case Load (%)
Litigation,25
Contract Law,20
Real Estate Law,15
Employment Law,10
Intellectual Property Law,10
Bankruptcy Law,8
Antitrust Law,7
Environmental Law,5"""

# Parse input data
rows = input_data.split('\n')
data_labels = rows[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in rows[1:]]
data = [[int(row.split(',')[1])] for row in rows[1:]]

# Create a treemap
fig = px.treemap(
    names=line_labels, 
    values=[val[0] for val in data],
    parents=[""]*len(data),
    title='Proportional Case Load Across Legal Sectors'
)

# Customize the treemap
fig.update_traces(
    textinfo="label+value",
    textfont_size=18,
    marker=dict(colors=px.colors.qualitative.Plotly, 
    line=dict(width=1, color='white'))
)

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/136.png"
fig.write_image(save_path)

# Ensure that the current image state is cleared (not explicitly required in Plotly)
