import plotly.express as px
import os

# Given data
data_labels = ['Budget Allocation (%)']
line_labels = ['Judiciary', 'Law Enforcement', 'Corrections', 'Legal Services', 'Law Education', 'Public Legal Awareness']
data = [35, 30, 15, 10, 5, 5]

# Creating a DataFrame for plotly
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Legal Branch','Budget Allocation (%)'])

# Create the treemap
fig = px.treemap(df, path=['Legal Branch'], values='Budget Allocation (%)',
                 title='Budget Distribution Among Legal Branches')

# Customize the chart to ensure text fits and the chart is intuitive
fig.update_traces(textinfo="label+value", textfont_size=10)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=50), title_font_size=24)

# Save figure to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/179.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current figure state
fig.data = []
