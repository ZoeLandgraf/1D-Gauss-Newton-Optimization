import plotly.graph_objects as go
import numpy as np

def animate_optimization(function, x, f_limits = (-15, 15)):

    function_x_points = np.linspace(f_limits[0], f_limits[1], len(x)*2)
    function_y_points = [function.F(x) for x in function_x_points]

    #plt limits:
    xm = np.maximum(-300,np.min(function_x_points)) - 5
    xM = np.minimum(700, np.max(function_x_points)) + 5
    ym = np.maximum(-300, np.min(function_y_points)) - 10
    yM = np.minimum(700, np.max(function_y_points)) + 10

    opt_x_points = x
    opt_y_points = [function.F(x) for x in opt_x_points]

    # Create figure
    fig = go.Figure(
        data=[go.Scatter(x=function_x_points, y=function_y_points,
                         mode="lines",
                         line=dict(width=2, color="blue")),
              go.Scatter(x=function_x_points, y=function_y_points,
                         mode="lines",
                         line=dict(width=2, color="blue"))],
        layout=go.Layout(
            xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title_text="Gauss Newton Optimization in 1D", hovermode="closest",
            updatemenus=[dict(type="buttons",
                              buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None])])]),
        frames=[go.Frame(
            data=[go.Scatter(
                x=[opt_x_points[k]],
                y=[opt_y_points[k]],
                mode="markers",
                marker=dict(color="red", size=10))])

            for k in range(len(x))]
    )

    fig.show()
