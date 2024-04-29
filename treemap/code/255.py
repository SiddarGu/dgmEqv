import plotly.express as px
import os

# Data
data = {'Healthcare Sector': ['Hospital Care', 'Physician and Clinical Services', 'Prescription Drugs', 
                              'Dental Services', 'Nursing Home Care', 'Home Healthcare', 
                              'Medical Equipment', 'Administrative Costs', 'Public Health Activities'],
        'Expenditure Share (%)': [38, 24, 15, 7, 6, 4, 3, 2, 1]}

# Transform data
data_labels = ['Expenditure Share (%)']  # Column labels without the first one
line_labels = data['Healthcare Sector']  # Row labels without the first one
data_values = data['Expenditure Share (%)']  # Numerical array

# Create a treemap using Plotly
fig = px.treemap(
    data_frame=data,
    path=[px.Constant('Healthcare Expenditures'), 'Healthcare Sector'],
    values='Expenditure Share (%)',
    title='Distribution of Healthcare Expenditures Across Sectors',
)

# Improve figure aesthetics
fig.update_traces(textinfo='label+value', textfont_size=12, marker=dict(line=dict(width=0.5)))
fig.update_layout(title_text='Distribution of Healthcare Expenditures Across Sectors', title_x=0.5)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1005.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current image state (in case of interactive session, e.g., jupyter notebook)
fig.data = []
