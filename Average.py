import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import csv
import pandas as pd 
df = pd.read_csv('newdata.csv')
data = df['average'].tolist()
#mean = statistics.mean(data)
#standarddiviation = statistics.stdev(data)
#print(mean,standarddiviation)
#fig = ff.create_distplot([data],['temp'],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = 'lines',name = 'mean'))
#fig.show()
#dataSet = []
#for i in range(0,100):
    #randomIndex = random.randint(0,len(data))
    #value = data[randomIndex]
    #dataSet.append(value)
#sampleMean = statistics.mean(dataSet)
#sampleStandarddiviation = statistics.stdev(dataSet)
#print(sampleMean,sampleStandarddiviation)
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,100):
        randomIndex = random.randint(0,len(data))
        #print(randomIndex)
        value = data[randomIndex]
        dataSet.append(value)
    sampleMean = statistics.mean(dataSet)
    return sampleMean
def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    print(mean)
    fig = ff.create_distplot([df],['average'],show_hist = False)
    fig.show()
def setup():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)
setup()
def standarddiviation():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    sd = statistics.stdev(meanList)
    print(sd)
standarddiviation()


