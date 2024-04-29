import plotly.express as px
import pandas as pd
import os

# Given raw data as string, splitting by "\n" to separate the rows and by "," to separate the elements
raw_data = "Sustainability Topic,Percentage (%)\nRenewable Energy Sources,30\nEnergy Efficiency,25\nSustainable Agriculture,20\nWaste Management,15\nWater Conservation,10"

# Splitting to obtain the labels and data
split_data = [row.split(',') for row in raw_data.split('\n')]

# Extracting labels and data into separate variables
data_labels = split_data[0][1:]
line_labels = [row[0] for row in split_data[1:]]
data = [float(row[1]) for row in split_data[1:]]

# Prepare the DataFrame for Plotly
df = pd.DataFrame({
    'Sustainability Topic': line_labels,
    'Percentage': data
})

# Draw the treemap using Plotly Express
fig = px.treemap(df, path=['Sustainability Topic'], values='Percentage',
                 title='Proportions of Environmental and Sustainability Initiatives in 2023')

# Customize the layout
fig.update_layout(
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"],
    margin=dict(t=50, l=25, r=25, b=25)
)

# Creating directories if they do not exist
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)

# Save the figure
fig.write_image(f"{save_dir}/16.png")

# Clear the current image state (relevant for matplotlib, not necessary for plotly)
# plt.clf(), plt.cla(), plt.close() would be used with matplotlib

