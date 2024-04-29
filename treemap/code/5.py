import plotly.express as px
import os

# Transforming given data into three variables
data_labels = ['Expenditure (%)']
line_labels = ['Legislative', 'Judicial', 'Executive', 'Law Enforcement']
data = [25, 35, 15, 25]

# Preparing data for the treemap
df = {
    'Legal Branch': line_labels,
    'Expenditure (%)': data
}

# Create a DataFrame
df = pd.DataFrame(df)

# Create the treemap
fig = px.treemap(df, path=['Legal Branch'], values='Expenditure (%)',
                 title='Allocation of Expenditure Across Legal Branches')

# Update layout for better visual appearance
fig.update_layout(
    treemapcolorway=["#636efa", "#ef553b", "#00cc96", "#ab63fa"],
    margin=dict(l=10, r=10, b=10, t=10)
)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
if not os.path.exists(save_path):
    os.makedirs(save_path)
file_path = os.path.join(save_path, '1053.png')

fig.write_image(file_path)

# Clear the current figure (if using matplotlib, but for plotly this step is unnecessary)
# plt.clf() or plt.close() are used in matplotlib but not needed in plotly
