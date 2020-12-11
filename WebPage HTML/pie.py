import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
import dash


# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/covidData.csv')

app = dash.Dash()

filtered_df = df1[df1['State/Territory'] != 'United States of America']
new_df = filtered_df.sort_values(by=['Total Cases'], ascending=[False]).head(20)

pie_chart = px.pie(
        data_frame=new_df,
        values='Total Cases',
        names='State/Territory',
        title = "Top 20 Cases by State")

# Plot the figure and saving in a html file
pyo.plot(pie_chart, filename='piechart.html')



