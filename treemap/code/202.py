import plotly.express as px

# Given data in string format, parsing it to get the structured data
raw_data = """Humanities Discipline,Research Funding (%)
History,20
Philosophy,18
Languages,16
Arts & Literature,14
Anthropology,12
Sociology,10
Psychology,6
Religious Studies,4"""

# Split the data by lines and then by commas
lines = raw_data.split('\n')
data_labels = lines[0].split(',')  # Column labels
line_labels = [row.split(',')[0] for row in lines[1:]]  # Row labels
data = [row.split(',')[1] for row in lines[1:]]  # The data

# Convert data to float for plotting
data = [float(d) for d in data]

# Now we'll create a structured dictionary that holds the parsed data
structured_data = {
    'labels': line_labels,
    'values': data
}

# Create a treemap using plotly
fig = px.treemap(
    structured_data,
    path=['labels'],
    values='values',
    title='Research Funding Distribution Across Humanities Disciplines',
)

# Enhance the treemap with fancy visual elements
fig.update_traces(textinfo="label+value",
                  textfont_size=16,
                  marker=dict(colors=px.colors.qualitative.Pastel,
                              line=dict(width=1)))

# Save the figure to the specified path
fig.write_image('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/202.png')

# Clear the current image state, this is handled by writing the figure to an image file
# Plotly does not maintain state like matplotlib, so there is no need to explicitly clear state after saving.
