import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Expenditure (%)']
line_labels = ['Legislative', 'Judicial', 'Executive', 'Law Enforcement']
data = [25, 35, 15, 25]

# Constructing a DataFrame (if needed) for better compatibility with plotly
import pandas as pd
df = pd.DataFrame({
    'Legal Branch': line_labels,
    'Expenditure (%)': data
})

# Draw the treemap
fig = px.treemap(df, path=['Legal Branch'], values='Expenditure (%)', 
                 title='Allocation of Expenditure Across Legal Branches')

# Customizing the treemap to make it fancy as per requirements
fig.update_traces(textinfo='label+percent entry', 
                  marker=dict(colors=px.colors.qualitative.Pastel,
                              line=dict(color='#FFFFFF', width=2)))

# Add unique customization such as rounded corners if desired
# This can be done by introducing custom shapes or using the plotly API

# Remove the unnecessary axis grids, as it's a treemap
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25), 
                  plot_bgcolor='rgba(0,0,0,0)')

# Ensure the string in 'Legal Branch' is not too long to be displayed properly
fig.update_traces(
    texttemplate="<b>%{label}</b><br>%{percentParent}",
    textposition='middle center'
)

# Resize the image by tight_layout() before savefig(), if using matplotlib
# (not needed with Plotly)

# Ensure the save path directory exists
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/"
os.makedirs(save_dir, exist_ok=True)

# Save the image
fig.write_image(save_dir + "1104.png")

# Clear the current image state at the end of the code (relevant to matplotlib)
# For plotly, there is no persisted state so nothing to clear but closing the figure if open
fig.show()  # To visualize the generated treemap in the notebook or script output
