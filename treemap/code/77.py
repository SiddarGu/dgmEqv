import plotly.express as px
import os

# Data setup
data_labels = ['Cereals', 'Vegetables', 'Fruits', 'Meat', 'Dairy', 'Fisheries', 'Oilseeds', 'Sugar Crops']
data = [25, 20, 20, 15, 10, 5, 3, 2]
line_labels = ['Production Share (%)']

# Create a DataFrame for plotly treemap
import pandas as pd
df = pd.DataFrame(list(zip(data_labels, data)), columns=['Agricultural Category', 'Production Share (%)'])

# Create treemap using plotly express
fig = px.treemap(df, path=['Agricultural Category'], values='Production Share (%)',
                 title='Proportion of Global Agriculture Production by Category')

# Customizing the treemap to make it fancy
fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

# Absolute path for the output image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/77.png'
# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save figure
fig.write_image(save_path)

# Clear the current image state if this is part of a stream of plotting commands
fig.data = []
