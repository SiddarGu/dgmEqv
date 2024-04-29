import plotly.express as px
import os

# Data
data_str = """Financial Sector,Investment Distribution (%)
Banking,25
Insurance,20
Investment Funds,15
Real Estate,10
Private Equity,10
Venture Capital,7
Bonds,5
Cryptocurrency,5
Stock Market,3"""

# Split the string lines and commas to create a list of lists
data_rows = [row.split(',') for row in data_str.split('\n')]

# Extract the labels and data
data_labels = data_rows[0][1:]  # The first row excluding the first column
line_labels = [row[0] for row in data_rows[1:]]  # The first column of each row excluding the header
data = [float(row[1]) for row in data_rows[1:]]  # The data in the second column

# Create a DataFrame suitable for a treemap
import pandas as pd
df = pd.DataFrame({'Category': line_labels, 'Value': data})

# Plot the treemap using Plotly
fig = px.treemap(df, path=['Category'], values='Value', title='Portfolio Spread Across Financial Sectors in Current Fiscal Year')

# Customize the layout
fig.update_layout(
    treemapcolorway=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A','#19D3F3','#FF6692','#B6E880','#FF97FF','#FECB52'],
    margin=dict(t=50, l=25, r=25, b=25)
)

# Ensure the directory where the image will be saved exists
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it does not exist

# Save the figure
fig.write_image(f"{output_dir}/219.png")

# Clear the current image state if needed (this isn't usually necessary for Plotly)
# No command is necessary here
