import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
df = pd.read_csv('C:/Users/jpw66/OneDrive/Desktop/Visualization-Lab/Software-Eng/Datasets/covidData.csv')
# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


# Preparing data
data = [
go.Scatter(x=df['Cases in Last 7 Days'],
y=df['Total Cases'],
text=df['State/Territory'],
mode='markers',
marker=dict(size=df['Cases in Last 7 Days'] /
1000,color=df['Total Cases'] / 1000, showscale=True))
]

# Preparing layout
layout = go.Layout(title='Corona Virus Confirmed Cases', xaxis_title="Cases in Last 7 Days", yaxis_title="Total Cases", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblecovid.html')