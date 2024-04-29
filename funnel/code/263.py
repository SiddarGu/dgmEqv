
import plotly.graph_objects as go
import plotly.io as pio

data = [
    dict(
        type="funnel",
        y=["Recruitment","Interview","Hiring","Onboarding","Training","Retention"],
        x=[1000,800,600,400,200,100],
        textinfo="value+percent initial",
        marker=dict(
            color="darkblue",
            line=dict(
                color="royalblue",
                width=3
            )
        )
    )
]

layout = dict(title="Optimizing Employee Management in Human Resources in 2020",
              height=800,
              font=dict(family="Verdana"),
              grid=dict(rows=1, columns=1)
              )

fig = go.Figure(data=data, layout=layout)

fig.update_layout(legend_orientation="h", legend=dict(x=0.2, y=1))

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/65.png")