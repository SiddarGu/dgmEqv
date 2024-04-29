import plotly.express as px
import pandas as pd
import os

# Given data
data = {
    "Manufacturing Component": [
        "Raw Materials", "Assembly Lines", "Quality Control", "Packaging", "Storage", 
        "Distribution", "Research and Development", "Maintenance", "Waste Management"
    ],
    "Production Share (%)": [30, 20, 15, 10, 8, 7, 5, 3, 2]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Draw the treemap using `plotly.express`
fig = px.treemap(
    df,
    path=['Manufacturing Component'],
    values='Production Share (%)',
    title='Proportional Breakdown of Manufacturing and Production Phases'
)

# Update layout for aesthetic enhancements
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the absolute path for saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
file_name = '53.png'

# Ensure the directory exists
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(os.path.join(save_path, file_name))

# Clear the current image state if necessary (only needed for certain backends like matplotlib)
# fig.clf() or plt.clf() (if you were using matplotlib)
