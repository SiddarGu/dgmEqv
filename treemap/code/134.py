import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_str = """Biotechnology,22
Aerospace Engineering,18
Computer Science,17
Environmental Science,14
Materials Science,10
Electrical Engineering,9
Mechanical Engineering,5
Chemical Engineering,3
Civil Engineering,2"""

# Transforming data into variables
rows = data_str.split("\n")
data_labels = ["Field", "Research Funding (%)"]
line_labels = [row.split(",")[0] for row in rows]
data = [float(row.split(",")[1]) for row in rows]

# Creating a DataFrame
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Visualizing data using a treemap
fig = px.treemap(df, path=['Field'], values='Research Funding (%)',
                 title='Allocation of Research Funding in Science and Engineering Fields')

# Customizing for better appearance
fig.update_traces(textinfo='label+value+percent entry')
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/134.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current figure state
fig.data = []
