import plotly.express as px
import os

# Given data
data_labels = ['Market Share (%)']
line_labels = ['Single-Family Homes', 'Apartments', 'Condominiums', 'Townhomes', 'Multi-Family Dwellings', 'Luxury Estates', 'Mobile Homes']
data = [40, 25, 15, 10, 5, 3, 2]

# Prepare DataFrame for Plotly
df = pd.DataFrame({
    'Housing Category': line_labels,
    'Market Share (%)': data
})

# Create Treemap
fig = px.treemap(df, path=['Housing Category'], values='Market Share (%)',
                 title='Real Estate Market Share by Housing Category in 2023')

# Improve treemap aesthetics
fig.update_traces(textinfo="label+percent entry", textfont_size=12)
# Wrap text for longer labels
fig.update_traces(textposition='middle center', texttemplate="%{label}<br>%{value}")

# Define the file path for saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/174.png'
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path))

# Save the figure
fig.write_image(save_path)

# Clear the figure (This is not strictly necessary as the figure is saved and the script ends here)
fig.data = []
