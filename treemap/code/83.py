import plotly.express as px
import os

# Given data, separated into labels and values
data_labels = ["Single-Family Homes", "Condominiums", "Townhouses", "Multi-Family Buildings", "Manufactured Homes",
               "Vacation Homes", "Co-ops", "Luxury Estates", "Foreclosures"]
data = [30, 25, 15, 10, 7, 5, 4, 3, 1]
line_labels = ["Market Share (%)"]

# Creating a DataFrame for the plot
import pandas as pd
df = pd.DataFrame(list(zip(data_labels, data)), columns=['Property Type', 'Market Share'])

# Create the treemap figure
fig = px.treemap(df, path=['Property Type'], values='Market Share', title='Market Share of Property Types within the Real Estate Market')

# Write code to automatically resize the image by tight_layout() before savefig()
# For plotly, it smartly handles the layout so no need to manually call tight_layout

# Define the save path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_path, exist_ok=True)
save_file = os.path.join(save_path, "83.png")

# Save the figure
fig.write_image(save_file)

# Clear the current image state at the end of the code
# For plotly, the figure state is contained within the figure variable and doesn't need to be explicitly cleared
