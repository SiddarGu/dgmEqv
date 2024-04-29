import plotly.express as px
import os

# Data transformation
data_labels = ['Renewable Energy', 'Water Conservation', 'Waste Management',
               'Sustainable Agriculture', 'Pollution Control', 'Wildlife Protection']
data = [35, 25, 15, 10, 10, 5]
line_labels = ['Resource Usage (%)']

# Creating a dataframe
import pandas as pd
df = pd.DataFrame({
    "Environmental Aspect": data_labels,
    "Resource Usage (%)": data
})

# Creating a treemap
fig = px.treemap(df, path=['Environmental Aspect'], values='Resource Usage (%)',
                 title='Resource Usage Share in Environment and Sustainability Initiatives')

# Customization as needed
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(uniformtext=dict(minsize=10))

# Save the figure
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_dir, exist_ok=True)
fig.write_image(os.path.join(save_dir, "95.png"))

# Clear the current image state - not necessary since Plotly does not keep state
