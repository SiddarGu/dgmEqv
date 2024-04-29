import plotly.express as px

# Given data
data_labels = ['Usage (%)']
line_labels = ['Oil', 'Natural Gas', 'Coal', 'Nuclear', 'Renewables', 'Hydroelectricity', 'Wind', 'Solar']
data = [40, 25, 15, 10, 5, 3, 1, 1]

# Transforming the data
df = {'Energy Type': line_labels, 'Usage': data}

# Create a Pandas DataFrame
df = pd.DataFrame(df)

# Create the treemap
fig = px.treemap(df, path=['Energy Type'], values='Usage',
                 title="Percentage Breakdown of Energy Source Usage in Utilities Sector")

# Customize the treemap if necessary (feel free to adjust these settings)
fig.update_traces(textinfo='label+percent entry')
fig.update_layout(
    treemapcolorway = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880"],
    margin=dict(t=50, l=25, r=25, b=25)
)

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/161.png")

# Clear the current image state if needed (usually not necessary with plotly)
fig.data = []
