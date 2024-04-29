import plotly.express as px
import os

# Transform the given data into three variables
data_labels = ['Social Media', 'Online Shopping', 'Email Communication', 'Streaming Services',
               'Online Gaming', 'Cloud Services', 'Distance Learning', 'Telecommuting']

data = [25, 20, 15, 15, 10, 8, 4, 3]

line_labels = ['Internet Usage (%)']

# Prepare the data for the treemap
df = []
for label, value in zip(data_labels, data):
    df.append({'Category': label, 'Internet Usage (%)': value})
df = pd.DataFrame(df)

# Create the treemap
fig = px.treemap(df, path=['Category'], values='Internet Usage (%)',
                 title='Distribution of Internet Usage Across Various Online Activities in 2023')

# Customize the treemap
fig.update_traces(textinfo="label+percent entry")

# Define the absolute path for the image saving location
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'

# Create the directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(os.path.join(save_path, '96.png'))

# No current image state to clear in plotly, but ensure no layout persistence between figures
fig.show()
