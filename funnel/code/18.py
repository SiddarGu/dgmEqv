
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = ['Research', 'Enquiry', 'Booking', 'Departure', 'Arrival']
values = [120, 90, 60, 30, 15]

fig = make_subplots(
        rows=1, cols=1,
        specs=[[{"type": "funnel"}]],
        subplot_titles=["Growth of Tourism in Hospitality Sector in 2021"],
        )

fig.add_trace(go.Funnel(
        y=labels, 
        x=values,
        textinfo="value"
        ),
        1, 1)

fig.update_layout(
        height=800,
        width=800,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
        )

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/15.png")