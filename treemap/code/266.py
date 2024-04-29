import plotly.express as px
import plotly.graph_objects as go

# Data parsing
data_str = """Policy Area,Budget Allocation (%)
Health and Human Services,25
National Defense,20
Education,15
Social Security,15
Infrastructure,10
Environmental Protection,5
Law Enforcement,5
Science and Technology,3
Agriculture,2"""

# Splitting into rows and then into labels and data
rows = data_str.strip().split('\n')
data_labels = rows[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in rows[1:]]
data = [{
    'Policy Area': line.split(',')[0],
    'Budget Allocation (%)': float(line.split(',')[1])} for line in rows[1:]]

# Create a treemap using plotly
fig = px.treemap(
    data,
    path=['Policy Area'],
    values='Budget Allocation (%)',
    title='Allocation of Government Budget by Policy Area in 2023',
)

# Remove backgrounds and grids for a cleaner look
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    paper_bgcolor='white',  # Background color outside the plot
    plot_bgcolor='white',  # Plot background color
)

# Save figure
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1049.png'
fig.write_image(output_path)

# Clear the current image state, although it is not necessary in plotly
fig = None
