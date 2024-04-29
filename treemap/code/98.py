import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_str = "Social Network,Usage Share (%)\nFacebook,25\nYouTube,20\nWhatsApp,15\nInstagram,15\nTwitter,10\nLinkedIn,5\nSnapchat,5\nPinterest,3\nReddit,2"

# Transforming data into three variables
lines = data_str.split("\n")
data_labels = [lines[0].split(",")[1]]  # Labels of each column except the first
line_labels = [line.split(",")[0] for line in lines[1:]]  # Labels of each row except the first
data = [int(line.split(",")[1]) for line in lines[1:]]  # numerical data array

# Preparing data for treemap
df_treemap = {
    'labels': line_labels,
    'values': data,
}

# Plotting with Plotly
fig = px.treemap(df_treemap, path=['labels'], values='values', title='Social Media Usage Distribution Across Platforms in 2023')

# Customizing for clarity and aesthetics
fig.update_traces(textinfo="label+percent entry")  # Ensure all characters show without being overwritten
fig.update_layout(title_font_size=24)

# Define the absolute path for the saved image
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/98.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Making sure the directory exists

# Save the figure
fig.write_image(save_path)

# Clear the current image state to prevent pollution of further graphing
fig = None
