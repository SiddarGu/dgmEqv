import plotly.express as px
import os

# Convert the given data into the required format
data_labels = ['Banking', 'Insurance', 'Investments', 'Real Estate', 'Fintech']
line_labels = ["Market Share (%)"]
data = [30, 20, 25, 15, 10]

# Create a DataFrame for the treemap data
import pandas as pd
df = pd.DataFrame(list(zip(data_labels, data)), columns=['Financial Sector', 'Market Share (%)'])

# Create the treemap
fig = px.treemap(df, path=['Financial Sector'], values='Market Share (%)',
                 title='Market Share Distribution Among Financial Sectors in 2023')

# Customizations
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Ensure the directory exists
image_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(image_dir, exist_ok=True)

# Save the figure
fig.write_image(os.path.join(image_dir, "38.png"))

# Clear the figure (unused in plotly, added for the completeness of the instructions)
fig = None
