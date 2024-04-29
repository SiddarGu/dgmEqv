import plotly.express as px
import os

# Data transformation
data_labels = ['Investment Allocation (%)']
line_labels = ['Banking', 'Insurance', 'Real Estate', 'Investment Funds', 'Private Equity', 'Stock Market', 'Venture Capital', 'Government Bonds']
data = [22, 18, 17, 16, 12, 8, 4, 3]

# Building a DataFrame for plotly
import pandas as pd

df = pd.DataFrame({
    'Finance Sector': line_labels,
    'Investment Allocation (%)': data
})

# Initialize figure using plotly express
fig = px.treemap(df, 
                 path=['Finance Sector'], 
                 values='Investment Allocation (%)',
                 title='Portfolio Distribution Across Finance Sectors')

# Fine-tuning appearance
fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/99.png'
save_dir = os.path.dirname(save_path)

# Ensure the directory exists
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

fig.write_image(save_path)

# Clearing figure (not needed for plotly, but included for completeness)
fig = None
