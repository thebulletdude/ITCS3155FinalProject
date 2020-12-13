import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/covidData.csv')

app = dash.Dash()

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Cases data', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart can be modified to look at total cases, total deaths, and cases in the last 7 days.'),
    dcc.Graph(id='graph1'),
 html.Div('Please select a choice', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-continent',
        options=[
            {'label': 'Total Cases', 'value': 'Total Cases'},
            {'label': 'Total Deaths', 'value': 'Total Deaths'},
            {'label': 'Cases in Last 7 Days', 'value': 'Cases in Last 7 Days'},
        ],
        value='Total Cases'
    )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_type):

    filtered_df = df1[df1['State/Territory'] != 'United States of America']
    filtered_df = filtered_df.sort_values(by=[selected_type], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=filtered_df['State/Territory'], y=filtered_df[selected_type])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title=selected_type + " in top 20 States",
                                                                   xaxis={'title': 'States'},
                                                                   yaxis={'title': selected_type})}



if __name__ == '__main__':
    app.run_server()

