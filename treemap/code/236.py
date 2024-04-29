import plotly.express as px
import os

# Construct the data variables
data_labels = ['Research Funding (%)']
line_labels = ['Physics', 'Biotechnology', 'Computer Science', 'Mechanical Engineering',
               'Chemical Engineering', 'Environmental Science', 'Electrical Engineering',
               'Materials Science']
data = [22, 18, 17, 14, 12, 9, 5, 3]

# Convert the data to a format suitable for a treemap
df = {
    'Fields': line_labels,
    'Funding': data
}

# Create treemap
fig = px.treemap(
    df, 
    path=['Fields'], 
    values='Funding',
    title='Allocation of Research Funds Across Science and Engineering Fields'
)

# Customize the figure to make it fancy as requested
fig.update_traces(textinfo="label+value", 
                  textfont_size=15, 
                  marker=dict(colors=px.colors.qualitative.Pastel, 
                              line=dict(color='#FFFFFF', width=2)))
fig.update_layout(title_font_size=24)

# Define the path to save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/236.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the image
fig.write_image(save_path)

# Clear the current image state if using matplotlib (not needed in plotly)
# plt.clf()

# Since we are not using matplotlib, no need to clear the image state (plotly does not require this)
# and no figsize, tight_layout(), or savefig() code is needed since fig.write_image() handles this.
