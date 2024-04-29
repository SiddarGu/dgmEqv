import plotly.express as px
import os

# Provided data
data_str = """Field,Research Funding (%)
Biology,19
Computer Science,17
Engineering,20
Physics,14
Chemistry,10
Environmental Science,8
Mathematics,7
Materials Science,3
Astronomy,2"""

# Parsing the data to obtain data_labels, data, and line_labels
lines = data_str.strip().split('\n')
data_labels = [lines[0].split(',')[0]]  # 'Field'
line_labels = [line.split(',')[0] for line in lines[1:]] # All the fields excluding 'Field'
data = [float(line.split(',')[1]) for line in lines[1:]] # Percentage values

# Create a DataFrame to represent the data
import pandas as pd
df = pd.DataFrame({
    'Field': line_labels,
    'Research Funding (%)': data
})

# Create a treemap using plotly
fig = px.treemap(
    df,
    path=['Field'],
    values='Research Funding (%)',
    title= 'Allocation of Research Funds Across Science and Engineering Fields'
)

# To ensure that labels are clear and not overlapping, adjust text options
fig.update_traces(textinfo='label+value', textfont_size=20)

# Save the figure to the specified directory
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist
fig.write_image(f"{save_dir}/227.png")

# Clear the current figure (not inherently necessary when using plotly)
fig = None
