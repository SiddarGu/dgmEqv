import plotly.express as px
import os

# Given data in CSV-like format
data_str = """Discipline,Research Funding (%)
Psychology,18
Sociology,15
Anthropology,12
Linguistics,11
Philosophy,10
History,10
Political Science,9
Geography,8
Cultural Studies,7"""

# Split the data into lines and then into labels and values
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Transformed data
disciplines = {'labels':line_labels, 'values': data}

# Create treemap figure
fig = px.treemap(
    disciplines, 
    path=[px.Constant('Research Funding (%)'), 'labels'], 
    values='values',
    title='Allocation of Research Funding in Social Sciences and Humanities'
)

# Customize treemap configuration
fig.update_traces(textinfo="label+value", textfont=dict(size=12))
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# The path where the image will be saved
output_directory = "/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/"
output_filename = "1039.png"
output_path = os.path.join(output_directory, output_filename)

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Save the figure
fig.write_image(output_path)

# It's not necessary to clear the image state as it is saved and the code ends here.
# However, in a persistent environment like Jupyter you might use fig.show() to display the figure.
