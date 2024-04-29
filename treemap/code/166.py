import plotly.express as px
import os

# Given data
data_str = """Art Style,Popularity (%)
Classicism,18
Modernism,22
Impressionism,15
Surrealism,14
Abstract,10
Street Art,7
Pop Art,6
Renaissance Art,5
Baroque,3"""

# Transforming the given data into variables
data_lines = data_str.split("\n")
data_labels = data_lines[0].split(",")  # ['Art Style', 'Popularity (%)']
line_labels = [line.split(",")[0] for line in data_lines[1:]]  # ['Classicism', 'Modernism', etc.]
data = [float(line.split(",")[1]) for line in data_lines[1:]]  # [18, 22, etc.]

# Preparing the dataframe
df = {data_labels[0]: line_labels, data_labels[1]: data}
df = pd.DataFrame(df)

# Draw treemap using plotly
fig = px.treemap(df, path=[px.Constant("Art Styles"), data_labels[0]], values=data_labels[1], title='Popularity Trends in Art Styles')

# Improve treemap aesthetics
fig.update_traces(textinfo="label+value", textfont=dict(size=18), hoverinfo="label+percent entry", marker=dict(line=dict(width=0)))
fig.update_layout(margin=dict(l=10, r=10, t=35, b=10))

# Ensure the paths for the directories exist
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, '166.png')

# Save the figure
fig.write_image(save_path)

# Clear the current image state (if using matplotlib, but it's not required for plotly)
# plt.clf() or plt.close() would be used in matplotlib, but not in plotly
