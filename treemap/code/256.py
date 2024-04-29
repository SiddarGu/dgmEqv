import plotly.express as px
import os

# Given data in a formatted string (replaced /n with \n for proper line breaks)
raw_data = "Sector,Market Share (%)\nBanking,25\nInsurance,20\nInvestment,15\nReal Estate,10\nFintech,9\nRetail Trade,8\nManufacturing,7\nInformation Technology,4\nAgriculture,2"

# Split the data into lines and then split each line into its components
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]  # The column labels excluding the first column (Sector)
line_labels = [line.split(',')[0] for line in lines[1:]]  # The row labels excluding the first column
data = [float(line.split(',')[1]) for line in lines[1:]]  # The numerical data

# Create a DataFrame to use with Plotly
import pandas as pd
df = pd.DataFrame({
    'Sector': line_labels,
    'Market Share (%)': data
})

# Create a treemap with the Plotly express
fig = px.treemap(df, path=['Sector'], values='Market Share (%)', title='Market Share Distribution Across Business and Finance Sectors')

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1006.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Create the directory if it doesn't exist
fig.write_image(save_path)

# Clear the figure to avoid any state issues (not strictly necessary with Plotly express)
fig = None
