import plotly.express as px
import os

# Data
data_labels = ['Grant Funding (%)']
line_labels = [
    'Anthropology', 'Sociology', 'Psychology', 'History',
    'Linguistics', 'Political Science', 'Philosophy', 'Economics', 'Geography'
]
data = [18, 16, 15, 14, 12, 10, 7, 5, 3]

# Create DataFrame
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Research Area', 'Grant Funding (%)'])

# Draw Treemap
fig = px.treemap(df, path=['Research Area'], values='Grant Funding (%)',
                 title='Allocation of Research Grants in Social Sciences and Humanities for 2023')

# Customization to ensure legibility and aesthetics
fig.update_traces(textinfo="label+value", textfont_size=15)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create directories if they do not exist
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save figure
fig.write_image(f"{save_dir}/89.png")

# Clear current image state (for Jupyter Notebooks, for example)
# If using a regular script, then this is not necessary
fig.show()
