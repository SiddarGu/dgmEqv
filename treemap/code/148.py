import plotly.graph_objects as go
import os

# Raw data for visualization
raw_data = """Platform,Usage Share (%)
Facebook,27
YouTube,21
WhatsApp,18
Instagram,12
Twitter,9
TikTok,8
LinkedIn,3
Snapchat,2"""

# Since we only have a single column of numerical data, we will ignore data_labels and line_labels as there's no need for them.
data_labels = "Usage Share (%)"
line_labels = [line.split(',')[0] for line in raw_data.strip().split('\n')[1:]]
data = [int(line.split(',')[1]) for line in raw_data.strip().split('\n')[1:]]

# Create a treemap with plotly
fig = go.Figure(go.Treemap(
    labels=line_labels,
    values=data,
    parents=[""] * len(data),
    textinfo="label+value+percent parent",
))

fig.update_layout(
    margin=dict(t=0, l=0, r=0, b=0),
    title_text="Social Media Usage Distribution Across Platforms",
)

# Define the image save path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/148.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear current figure (relevant if using matplotlib)
# plt.clf() or plt.close() if matplotlib was used; with plotly, it's not required

