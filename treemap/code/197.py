import plotly.express as px
import os

# Create the data variables
data_labels = ["Transport Sector", "Fuel Usage (%)"]
line_labels = ["Road Transport", "Maritime Shipping", "Air Freight", "Rail Transport", "Logistics Services"]
data = [40, 25, 20, 10, 5]

# Prepare the data in a dictionary, which is a suitable format for creating the treemap
data_dict = {"Sector": line_labels, "Usage": data}

# Create a DataFrame
df = pd.DataFrame(data_dict)

# Create a treemap
fig = px.treemap(df, path=['Sector'], values='Usage',
                 title='Fuel Usage Distribution in Transportation and Logistics Sector')

# Set treemap layout properties (like colors, rounded corner, font size, etc.)
fig.update_layout(
    treemapcolorway=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'],
    font=dict(size=18),
)

# Save the figure to the specified location ensuring the directory exists
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)
fig.write_image(f"{save_path}/197.png")

# Clear current figure state to prevent reuse
fig = None
