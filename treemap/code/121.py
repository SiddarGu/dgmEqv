import plotly.express as px

# Given data transformed into variables
data_labels = ["Expenditure (%)"]
line_labels = ["Judiciary", "Law Enforcement", "Public Defense", "Prosecution", "Legal Aid", "Corrections", "Regulatory Compliance"]
data = [35, 30, 15, 10, 5, 3, 2]

# Constructing a DataFrame from the provided data
import pandas as pd
df = pd.DataFrame({'Legal Branch': line_labels, 'Expenditure': data})

# Create treemap using Plotly
fig = px.treemap(df, path=['Legal Branch'], values='Expenditure', title='Allocation of Legal Expenditures Across Branches')

# Customize the layout to ensure text does not overlap and is clear
fig.update_traces(textinfo="label+value", textfont_size=12)
fig.update_layout(treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692"],
                  margin = dict(t=0, l=0, r=0, b=0))

# Save the figure to the specified path with a clear image state
absolute_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
fig.write_image(absolute_path + "121.png")

# Clear current image state by closing all figures
import plotly.io as pio
pio.templates.default = "none"
