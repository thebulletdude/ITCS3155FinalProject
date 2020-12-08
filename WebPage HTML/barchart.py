import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/covidData.csv')

# Filtering US Cases
filtered_df = df[df['State/Territory'] != 'United States of America']

# Removing empty spaces from State column to avoid errors
filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
new_df = filtered_df.groupby(['State/Territory'])['Total Cases'].sum().reset_index()

# Sorting values and select first 20 states
new_df = new_df.sort_values(by=['Total Cases'], ascending=[False]).head(50)

# Preparing data
data = [go.Bar(x=new_df['State/Territory'], y=new_df['Total Cases'])]

# Preparing layout
layout = go.Layout(title='Corona Virus Confirmed Cases in The US by State', xaxis_title="States",
                   yaxis_title="Number of confirmed cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
