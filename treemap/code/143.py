import plotly.express as px
import os

# Given data (assuming the '/n' is actually intended to mean a newline '\n')
data_str = """Discipline,Research Funding (%)
Biology,18
Computer Science,17
Engineering,20
Physics,15
Chemistry,12
Medicine,10
Environmental Science,5
Astronomy,3"""

# Transforming given data string into variables data_labels, data, line_labels
lines = data_str.split("\n")
header = lines.pop(0).split(",")  # Removing header
data_labels = [header[1]]  # second column label
line_labels = [line.split(",")[0] for line in lines]  # first column values
data = [{"Discipline": line.split(",")[0], "Research Funding (%)": float(line.split(",")[1])} for line in lines]  # numerical data for treemap

# Create the treemap
fig = px.treemap(
    data,
    path=['Discipline'],  # Define hierarchy
    values='Research Funding (%)',  # Define sizes of rectangles
    title='Percentage Distribution of Research Funding Across Science and Engineering Disciplines'
)

# Enhance the layout as per the instructions
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),  # smaller margin
    treemapcolorway=["blue", "green", "red", "orange", "cyan", "purple", "yellow", "pink"],  # custom color scheme
    font=dict(size=12)  # font size
)

# Save the image in the specified path - Make directories if they don't exist
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1128.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current image state at the end of the code.
fig.data = []
