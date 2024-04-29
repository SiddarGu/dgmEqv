import plotly.express as px
import plotly.graph_objects as go
import os

# Given data in a structured format
data = [
    ["Health", 25],
    ["Education", 20],
    ["Environment", 15],
    ["Arts and Culture", 10],
    ["International Aid", 10],
    ["Human Services", 10],
    ["Public Benefit", 5],
    ["Animal Welfare", 3],
    ["Religion", 2]
]

data_labels = ["Charity Sector", "Donation Share (%)"]  # Headers: Labels for each column
line_labels = [row[0] for row in data]  # Extracting the first element of each row for line labels
shares = [row[1] for row in data]  # Extracting the second element of each row for the share values

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=data_labels)

# Create a treemap using plotly
fig = px.treemap(df, path=[px.Constant("Donations"), 'Charity Sector'], values='Donation Share (%)',
                 title='Proportional Distribution of Donations Among Charity Sectors')

# Update the layout for clarity, e.g. font size and wrapped labels
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(
    title_font_size=24,
    uniformtext=dict(minsize=10, mode='hide')
)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/183.png'
# Ensure directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# If you were to display the chart as well, otherwise this is not necessary
# fig.show()

# Clear the current image state to prevent interference with other plots (this code is relevant for matplotlib, not plotly)
# plt.clf()
