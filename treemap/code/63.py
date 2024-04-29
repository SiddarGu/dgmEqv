# Import necessary libraries
import plotly.express as px
import pandas as pd

# Parse the provided data
raw_data = """Environmental Aspect,Resource Allocation (%)
Renewable Energy,30
Conservation Efforts,25
Pollution Control,20
Sustainable Agriculture,15
Eco-friendly Transport,10"""

# Split the data into lines and process it into a DataFrame
lines = raw_data.split('\n')
data_labels = lines[0].split(',')
line_labels = []
values = []

for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    values.append(int(parts[1]))

# Create a DataFrame
df = pd.DataFrame({
    data_labels[0]: line_labels,
    data_labels[1]: values
})

# Use Plotly to create a treemap
fig = px.treemap(df, path=[data_labels[0]], values=data_labels[1],
                 title='Allocation of Resources Towards Environmental and Sustainability Initiatives')

# Update layout for better readability
fig.update_layout(
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"],
    margin=dict(t=50, l=25, r=25, b=25)
)

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/63.png")

# Clear the current image state by closing the figure if you are using matplotlib (not needed for plotly)
# plt.close(fig) - This line would be required if we were using matplotlib to handle multiple plots
