import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['R&D Investment (%)']
line_labels = [
    'Artificial Intelligence',
    'Biotechnology',
    'Materials Science',
    'Renewable Energy',
    'Aerospace',
    'Robotics',
    'Chemical Engineering',
    'Environmental Science'
]
data = [17, 16, 15, 14, 13, 10, 8, 7]

# Format the data for the treemap
df = []
for label, value in zip(line_labels, data):
    df.append({'category': label, 'value': value})

# Convert to a DataFrame
df = pd.DataFrame(df)

# Create a treemap
fig = px.treemap(df, path=['category'], values='value', 
                 title='Proportion of R&D Investment Across Science and Engineering Fields')

fig.update_traces(textinfo='label+percent entry', textfont_size=12, marker=dict(line=dict(width=0.5)))

# Define the absolute path for the image
output_directory = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
output_filename = '1040.png'
output_path = os.path.join(output_directory, output_filename)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Save the figure
fig.write_image(output_path)

# Clear current image state if using pyplot (not needed for plotly)
# plt.clf()
