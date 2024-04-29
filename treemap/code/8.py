# Import the necessary libraries
import plotly.express as px
import plotly.graph_objects as go

# Transform the provided data
data_labels = ['Research Funding (%)']
line_labels = ['Space Exploration', 'Biotechnology', 'Renewable Energy', 'Artificial Intelligence', 
               'Materials Science', 'Electronics', 'Earth Sciences', 'Mechanical Engineering']
data = [22, 18, 15, 14, 11, 10, 8, 2]

# Prepare the dataframe for the plotly treemap
import pandas as pd
df = pd.DataFrame(zip(line_labels, data), columns=['Field', 'Funding'])

# Create a treemap using plotly
fig = px.treemap(df, path=['Field'], values='Funding', title='Allocation of Research Funding Across Scientific and Engineering Fields')

# Update treemap looks here if needed (colors, rounded corners, etc.)
fig.update_traces(textinfo='label+value', textfont_size=14)

# Save the figure as an image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/8.png'
fig.write_image(save_path)

# To clear the current image state, if you were using matplotlib you would use:
# plt.clf()
# Since we are using plotly, the figure object is not stateful in the same way, so you do not need to clear it explicitly.
