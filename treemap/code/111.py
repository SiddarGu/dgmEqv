import plotly.express as px
import os

# Data provided
data = [
    ["Facebook", 27],
    ["YouTube", 20],
    ["WhatsApp", 15],
    ["Instagram", 14],
    ["WeChat", 10],
    ["TikTok", 7],
    ["Twitter", 4],
    ["LinkedIn", 2],
    ["Snapchat", 1]
]

# Split the data into labels and values
data_labels = [row[0] for row in data]
usage_share = [row[1] for row in data]

# Constructing a dataframe for the treemap
import pandas as pd
df = pd.DataFrame({'Platform': data_labels, 'Usage Share (%)': usage_share})

# Create and style the treemap
fig = px.treemap(df, path=['Platform'], values='Usage Share (%)', title='Percentage Usage Share of Social Media and Web Platforms in 2023')

# Update layout for clearer text display
fig.update_layout(treemapcolorway = ["#636EFA","#EF553B","#00CC96","#AB63FA","#FFA15A","#19D3F3","#FF6692","#B6E880","#FF97FF"],
                  margin=dict(t=50, l=25, r=25, b=25))

# Define path for saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/111.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Print out the path to the saved image for confirmation
print(f"Image saved to: {save_path}")
