import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
csv_data = """
Industry,Market Share (%)
Banking,22
Insurance,19
Investment,18
Real Estate,14
Retail,9
Technology,8
Manufacturing,6
Agriculture,4
"""

# Transform given data into three variables
lines = csv_data.strip().split('\n')

# Extracting data labels (column labels)
data_labels = lines[0].split(',')

# Extract line labels (row labels) and data
line_labels = []
data = []
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Prepare the dataframe for Plotly
df = pd.DataFrame({data_labels[0]: line_labels, data_labels[1]: data})

# Create the treemap
fig = px.treemap(df, path=[px.Constant("all"), 'Industry'], values='Market Share (%)',
                 title='Market Share Distribution Across Financial and Business Industries')

# Customize the figure as fancy as possible
fig.update_traces(textinfo="label+percent entry", 
                  marker=dict(colors=px.colors.qualitative.Pastel),
                  textfont_size=16)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)  # Create directories if they don't exist
file_name = os.path.join(save_path, '117.png')
fig.write_image(file_name)

# Show the figure
fig.show()

# Clear the current image state if necessary (in case of using matplotlib)
plt.close('all')  # This isn't necessary for Plotly, but here for completeness
