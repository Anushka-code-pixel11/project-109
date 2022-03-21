import csv
import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import statistics as str

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data)
median = str.median(data)
mode = str.mode(data)
standard_deviation = str.stdev(data)

first_standardDeviation_start, first_standardDeviation_end = mean - standard_deviation,mean + standard_deviation
second_standardDeviation_start, second_standardDeviation_end = mean - (2*standard_deviation),mean + (2*standard_deviation)
third_standardDeviation_start, third_standardDeviation_end = mean - (3*standard_deviation),mean + (3*standard_deviation)

fig = ff.create_distplot([df["reading score"].tolist()],["reading score"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.21], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [first_standardDeviation_start,first_standardDeviation_start],y = [0,0.21], mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [first_standardDeviation_end,first_standardDeviation_end],y = [0,0.21], mode = "lines", name = "Standard Deviation 1"))

fig.add_trace(go.Scatter(x = [second_standardDeviation_start,second_standardDeviation_start],y = [0,0.21], mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [second_standardDeviation_end,second_standardDeviation_end],y = [0,0.21], mode = "lines", name = "Standard Deviation 2"))

fig.show()

