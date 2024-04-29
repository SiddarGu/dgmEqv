import plotly.express as px
import plotly.graph_objects as go
import os

# Provided data
data_labels = ["Dairy Products", "Bakery and Snack Foods", "Beverages", 
               "Meat and Poultry", "Seafood", "Confectionery", 
               "Grains and Cereals", "Frozen Foods"]
line_labels = ["Market Share (%)"]
data = [[22, 17, 20, 18, 8, 7, 5, 3]]

# Transform data into the right format for a treemap
df = {"Category": data_labels, "Market Share (%)": data[0]}

# Create a treemap
fig = px.treemap(df, path=['Category'], values='Market Share (%)', 
                 title='Market Share Distribution Within the Food and Beverage Industry')

# Customize figure
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", 
                                   "#FFA15A", "#19D3F3", "#FF6692", "#B6E880"],
                  title_font_size=24)

# The path where the image will be saved
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1019.png'

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear figure to avoid residual plots in the current session
fig.data = []
