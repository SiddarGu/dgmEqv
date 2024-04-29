import plotly.express as px
import pandas as pd
import os

# Data provided
data_str = """Category,Policy Spending (%)
Healthcare,25
Education,20
Defense,15
Social Security,15
Infrastructure,10
Energy,5
Science & Research,5
Environment,3
Agriculture,2"""

# Processing the string into a DataFrame
data = pd.DataFrame([x.split(',') for x in data_str.split('\n')])
data.columns = data.iloc[0]
data = data[1:]
data['Policy Spending (%)'] = pd.to_numeric(data['Policy Spending (%)'])

# Creating a treemap
fig = px.treemap(data, path=['Category'], values='Policy Spending (%)',
                 title='Allocation of Government Spending on Public Policy Categories')

# Customizing the treemap's appearance
fig.update_traces(textinfo='label+value+percent entry')
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1108.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clearing the current image state (not explicitly required when using Plotly)
