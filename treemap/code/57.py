import plotly.express as px
import os

# Given data
data_labels = ['Category', 'Usage Share (%)']
line_labels = ['Social Networking', 'Online Shopping', 'Information Search', 'Entertainment', 'Online Education', 'Email Communication', 'Web Development', 'Cloud Services']
data = [30, 20, 15, 15, 10, 5, 3, 2]

# Convert the data into a data frame for Plotly
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create the treemap
fig = px.treemap(df, path=['Category'], values='Usage Share (%)', title='Web Usage Distribution Across Different Online Activities')

# Enhancing the treemap for better visualization
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880"],
    title_font_size=24,
)

# Save the figure to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)  # Create directory if it doesn't exist
fig.write_image(f"{save_path}/1018.png")

# Clear the current image state (if necessary in the given environment)
fig.data = []
