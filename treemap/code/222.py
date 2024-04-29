import plotly.express as px
import os

# Given data
data_labels = ['Field of Study', 'Research Funding (%)']
line_labels = ['Psychology', 'Sociology', 'Anthropology', 'History',
               'Linguistics', 'Philosophy', 'Political Science', 'Economics', 'Geography']
data = [18, 16, 14, 12, 10, 10, 10, 5, 5]

# Transform data into a dictionary
data_dict = {data_labels[0]: line_labels, data_labels[1]: data}

# Convert dictionary to a DataFrame for use with plotly
import pandas as pd
df = pd.DataFrame(data_dict)

# Create the treemap
fig = px.treemap(df, path=[data_labels[0]], values=data_labels[1],
                 title='Allocation of Research Funding in Social Sciences and Humanities')

# Customizations
fig.update_traces(textinfo="label+value", textfont_size=12)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create directories if they do not exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(save_path + '222.png')

# Clear the current figure state
fig = None
