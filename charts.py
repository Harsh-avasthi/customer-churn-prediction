import plotly.graph_objects as go


def probability_gauge(probability):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=probability * 100,

        title={"text": "Churn Probability"},

        gauge={

            "axis": {"range": [0, 100]},

            "bar": {"color": "#2563EB"},

            "steps": [

                {"range": [0, 30], "color": "#22C55E"},

                {"range": [30, 70], "color": "#F59E0B"},

                {"range": [70, 100], "color": "#EF4444"}

            ]

        }

    ))

    fig.update_layout(height=350)

    return fig