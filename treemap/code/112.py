import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ["Revenue Share (%)"]
line_labels = ["Professional Sports", "Movies", "Music Industry", "Streaming Services", "Video Gaming", "Live Events", "Broadcasting", "Publishing"]
data = [35, 25, 15, 10, 7, 5, 2, 1]

# Create a DataFrame for the treemap
import pandas as pd
df = pd.DataFrame({
    'Category': line_labels,
    'Revenue Share': data
})

# Plot using plotly
fig = px.treemap(df, path=['Category'], values='Revenue Share', title='Revenue Distribution in the Sports and Entertainment Industry')

# Customization: set color scheme, increase font size if needed, manage label wrapping/rotation
fig.update_traces(
    textinfo="label+percent entry", 
    marker=dict(colors=px.colors.sequential.RdBu, line=dict(width=1)),
)
fig.update_layout(
    # uniformtext=dict(minsize=10, mode='hide'),
    title_font_size=24
)

# Specify the saving directory
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/"
# Ensure the saving directory exists
os.makedirs(save_dir, exist_ok=True)
# Save the figure
fig.write_image(f"{save_dir}/112.png")

# If there was a need to clear the figure (e.g. using matplotlib), we'd call plt.clf() to clear the figure.
# However, in Plotly, the figure object is not stateful like it is in matplotlib, so there is no need
# for such a step in this context.
