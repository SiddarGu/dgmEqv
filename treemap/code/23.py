import plotly.express as px
import plotly.graph_objects as go

# Provided data
data = """
Justice Branch,Percent of Budget (%)
Judiciary,30
Law Enforcement,25
Legal Services,20
Corrections,15
Legislative,5
Public Defense,3
Prosecution,2
"""

# Cleanning provided data and creating variables
lines = data.strip().split('\n')
line_labels = [line.split(',')[0] for line in lines[1:]]  # Labels from first column excluding header
data_labels = lines[0].split(',')[1:]  # Labels for the rest of the columns
data_values = [float(line.split(',')[1]) for line in lines[1:]]  # Actual data values

# Creating a dataframe
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data_values)), columns=['Justice Branch', 'Percentage'])

# Creating the treemap
fig = px.treemap(df, path=['Justice Branch'], values='Percentage',
                 title='Budget Distribution within the Justice System Components')

# Custom styling for the treemap
fig.update_traces(textinfo="label+value", textfont_size=20)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/23.png'
fig.write_image(save_path)

# Clear the current image state by closing the figure
fig.data = []
