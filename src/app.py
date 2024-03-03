import pandas as pd
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

server = app.server

# Layout
app.layout = dbc.Container(children=[
    dbc.Row(
        children=[
            dbc.Nav(children=[
                html.H3('Notificação de síndrome gripal no Brasil', className='mx-4 p-2')
            ], 
            class_name='mt-4 border border-1 border-light')
        ]
    ),
    dbc.Row(
        children=[
            dbc.Col(
                html.P(
                    children="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
                    className='mt-4'
                )
            )
        ]
    ),
    dbc.Row(
        children=[
            dbc.Col(
                children=['Button controls and cards here'],
                md=4,
                sm=12
            ),
            dbc.Col(
                children='Graph here',
                md=8,
                sm=12
            )
        ],
        class_name='mt-3'
    )
])

if __name__ == '__main__':
    app.run(debug=True)