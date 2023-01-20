# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:40:24 2023

@author: lalit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# =============================================================================
# dataFormation is a class used to extract data from csv file and return data
# =============================================================================
class dataFormation:
    '''
    this class is used to data filter reading the csv file name and return the
    data frames
    '''
    def __init__(self, fileName):
        '''
        this menthod is used to data filter and and assign values to object
        
        Parameters
        ----------
        fileName : CSV file
            fileName is used for data extraction and further which is used for
            setting the data as columns(as countries and years).

        Returns
        -------
        None.

        '''
        dataBank = pd.read_csv(fileName) # readign the data file
        # dropping the na values
        dataBank = dataBank.dropna(axis = 'columns', how = 'all')
        # setting the values to drop
        toDrop = ['Country Code', 'Indicator Name', 'Indicator Code']
        dataBank = dataBank.drop(toDrop, axis = 1) # dropping the values
        # setting the dataFrame values to a variable(years as columns)
        self.dataYears = dataBank
        # data frame transpose to get years as columns 
        dataBank_t = pd.DataFrame.transpose(dataBank)
        # changing the country name to year
        dataBank_t = dataBank_t.rename(index = {"Country Name":"Year"})
        dataBank_t = dataBank_t.reset_index() # resetting the index
        dataBank_t.columns = dataBank_t.iloc[0] # setting columns names
        dataBank_t = dataBank_t.iloc[1:] # removing the duplicate row
        # setting the dataFrame values to a variable(counties as columns)
        self.dataCountries =  dataBank_t
        
    # method to retun data with columns as country names
    def data_countries(self):
        '''
        this method is used to return data frame

        Returns
        -------
        Data Frame
            returning data frame with coloumns as countries.

        '''
        return self.dataCountries
    
    # method to retun data with columns as years
    def data_years(self):
        '''
        this method is used to return data frame 

        Returns
        -------
        data Frame
            returning data frame with coloumns as years.

        '''
        return self.dataYears
    
# scatter plot to show the data
def scatterPlot(xAxis, yAxis, db, cluster, title):
    '''
    this method is used to plot the scatter plot

    Parameters
    ----------
    xAxis : string
        X-axis label.
    yAxis : string
        Y-axis label.
    db : data frame
        preprocessed data frame which is used for plotting the data.
    cluster : list
        filtered data from the data frame.
    title : string
        title for the plot.

    Returns
    -------
    None.

    '''
    print(db['2000'])
    sb.scatterplot(x = db[xAxis],
                   y = db[yAxis], 
                   # hue = cluster, 
                   palette = sb.color_palette("hls", as_cmap=True),
                   data = db,
                   legend="full")
    plt.xlabel(xAxis, fontsize = 17)
    plt.ylabel(yAxis, fontsize = 17)
    plt.title(title, fontsize = 24)
    
    return

# invoking 
data_power = dataFormation("Electric power consumption.csv")

# scatter plot start
plt.figure(figsize=(10,6))

# =============================================================================
# invoking scatter plot method to plot the clusters
# plotting among change price and change in next week price
# =============================================================================
# dataToPass = data_power.data_countries()

scatterPlot('2002',
            '2007',
            # dataToPass,
            data_power.data_years(),
            'all_clusters',
            "Basic K-means clustering without outliers")

plt.show()

# print(dataBank)

# print(dataBank_t)