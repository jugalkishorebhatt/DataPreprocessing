# !/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

'''
Annotation -> Nudge

Juxtaposing -> Combining multiple graphs for comparison
'''

'''
 One/Two Categorical Data Viz
 
 One Categorical
 Bar Chart
 Pie Chart
 Dot Plot
 Stacked Dot Plot
 
 Two Categorical 
 Stacked Bar Chart  - Fill
 Grouped Bar CHart - Dodge
 Balloon Plot
 Mosaic Plot
 
 Three Categorical 
 Facet charts similar to Two Categorical
'''

'''
One/Two Categorical/One Quantitative Data - Faceting can also be applied two include additional categorical value
Box Plot
Side by Side Box Plot
Line Graph
Density Graph
Violin Graph
Sankey Graph
Parallel Graph
'''

'''
One Quantitative 
Line Graph
Density Graph
Histogram
Scatter Plot - Jitter

Two Quantitative 
Scatter Plot
Heat Map
'''

"""
Created on December 10
@author Jugal
"""
class DataViz:
    "Contains list of functions for Data Viz"
    
    
    "Initializer"
    def __init__(self,data):
        self.data = data
        
    def __scatterMatrix(self):
        scatter_matrix(self.data,alpha=0.8,figsize=(26,26))
        plt.show()
    
    
    
    '''
    sns.displot(tips['total_bill'])
    sns.jointplot(x='total_bill',y='tip',data=tips)
    sns.pairplot(tips)
    sns.rugplot(tips['total_bill'])
    
    sns.barplot(x='sex',y='total_bill',data=tips)
    sns.countplot(x='sex',data=tips)
    sns.boxplot(x='sex',y='total_bill',data=tips)
    sns.violinplot(x='sex',y='total_bill',data=tips)
    sns.stripplot(x='sex',y='total_bill',data=tips)
    sns.swarmplot(x='sex',y='total_bill',data=tips)
    sns.facetplot(x='sex',y='total_bill',data=tips,kind='bar')
    
    sns.heatmap()
    sns.clustermap()
    
    g = sns.PairGrid(iris)
    g.map(plt.scatterplot)
    
    g = sns.FacetGrid(data=tips,col='time',row='smoker')
    g.map(sns.distplot,'total_bill')
    
    sns.lmplot(x='total_bill',y='tip',data=tips)
    '''