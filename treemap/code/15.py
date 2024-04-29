import plotly.express as px
import os

# Define the data
data = """Government Branch,Budget Share (%)
Executive,35
Legislative,20
Judicial,15
Defense,10
Education,9
Healthcare,4
Public Safety,4
Welfare,3"""

# Parse the data into a list of dictionaries for easy use with Plotly
parsed_data = []
data_lines = data.strip().split('\n')
headers = data_lines[0].split(',')
for line in data_lines[1:]:
    line_data = line.split(',')
    parsed_data.append({headers[0]: line_data[0], headers[1]: float(line_data[1])})

# Create a treemap figure with Plotly
fig = px.treemap(parsed_data, 
                 path=[headers[0]], 
                 values=headers[1],
                 title='Allocation of Government Budget Across Branches and Key Public Policy Areas')

# Update layout to ensure text fits well and image is fancy
fig.update_layout(
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA",
                      "#FFA15A", "#19D3F3", "#FF6692", "#B6E880"],
    margin=dict(t=50, l=25, r=25, b=25)
)

# Define the file path where the image will be saved
file_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/15.png'
# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Saving the figure
fig.write_image(file_path)

# Clear the current image state (although not typically required in a standalone script)
fig.data = []

