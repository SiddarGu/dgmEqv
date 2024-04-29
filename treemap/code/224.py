import plotly.express as px
import plotly.graph_objects as go
import os

# Given data, transformed into separate variables for labels and numerical data
data_labels = ["Frequency (%)"]
line_labels = ["Contract Disputes", "Employment Litigation", "Personal Injury Claims",
               "Intellectual Property Rights", "Real Estate Litigation",
               "Consumer Protection Cases", "Antitrust Actions",
               "Immigration Appeals", "Environmental Compliance"]
data = [20, 18, 17, 15, 10, 8, 5, 4, 3]

# Creating a DataFrame for plotting
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Legal Issue', 'Frequency'])

# Creating treemap
fig = px.treemap(df, path=['Legal Issue'], values='Frequency', title='Proportional Analysis of Legal Issues Handled in 2023')

# Customizations for a fancy look
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(uniformtext=dict(minsize=10))

# Ensure the save directory exists
save_directory = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Save the figure
fig.write_image(os.path.join(save_directory, "224.png"))

# Clear current image state if using matplotlib (not required for plotly)
# plt.clf()
