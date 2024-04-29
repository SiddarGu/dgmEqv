import plotly.express as px
import os

# Given data
data_str = """Category, Revenue Share (%)
Professional Sports,35
Movies,25
Music Industry,15
Video Games,10
Television Programs,7
Live Performances,5
Amusement Parks,2
Sports Merchandising,1"""

# Processing the data
rows = data_str.split('\n')
data_labels = rows[0].split(', ')[1:]
line_labels = [row.split(',')[0] for row in rows[1:]]
data = [float(row.split(',')[1]) for row in rows[1:]]

# Create a DataFrame for Plotly
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Category', 'Revenue Share'])

# Draw treemap
fig = px.treemap(df, path=['Category'], values='Revenue Share', 
                 title='Revenue Distribution Across Sports and Entertainment Sectors')

# Update layout for fancy visuals
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    font=dict(size=16),
)

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/129.png'

# Create directory if not exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Clear the current image state (not applicable to plotly directly)
# fig.clf() - clf is matplotlib specific, not used in plotly
# fig.clear() - clear is matplotlib specific, not used in plotly

# Save the figure
fig.write_image(save_path)

# Show the figure, *optional*: this line can be removed if you don't want to display the image inline
fig.show()
