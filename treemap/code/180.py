import plotly.express as px
import os

# Transforming the given data into three variables
data_labels = ['Freight Volume (%)']
line_labels = ['Road', 'Rail', 'Air', 'Maritime', 'Pipeline', 'Intermodal']
data = [25, 20, 15, 28, 10, 2]

# Preparing the DataFrame for `plotly`
df = {
    'Transportation Mode': line_labels,
    'Freight Volume (%)': data
}

# Creating a treemap
fig = px.treemap(
    df,
    path=['Transportation Mode'],
    values='Freight Volume (%)',
    title='Freight Volume Distribution by Transportation Mode'
)

# Customizations for fancy appearance:
fig.update_traces(textinfo="label+percent entry", textfont_size=18)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/180.png'
# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the figure to prevent any further state changes
fig.data = []
