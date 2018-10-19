import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

x = np.linspace(-5, 5)
y = np.linspace(-5, 5)
yGrid, xGrid = np.meshgrid(x, y)

z = (np.sin(2/xGrid) + np.sin(2*xGrid) + np.cos(xGrid) + np.sin(20/yGrid))


data = [go.Surface(z=z)]
layout = go.Layout(
    title='POS Surface',
    scene=dict(
        xaxis=dict(
            nticks=11,
            # range=[-5, 5],
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            # range=[-5, 5],
            nticks=11,
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='POS Surface')