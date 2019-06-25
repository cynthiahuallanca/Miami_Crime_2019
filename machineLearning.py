import pandas as pd
# import matplotlib.pylab as plt
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.stattools import adfuller

def chart_by_weekday():
    # Read the dataset cleaned
    csv_path = 'Resources/jailbook_cleaned.csv'                    
    df = pd.read_csv(csv_path).copy()
    
    df[['Booking_Date']] = df[['Booking_Date']].apply(pd.to_datetime) ##Datetime

    df['Date'] = df['Booking_Date'].dt.date #Convert to date
    df['Time'] = df['Booking_Date'].dt.time 
    df[['Date']] = df[['Date']].apply(pd.to_datetime)

    df = df.reset_index(drop=True)

    # Extracting week number and day
    df['weekno'] = [df['Booking_Date'][i].isocalendar()[1] for i in range(len(df))]
    df['day']=[df['Booking_Date'][i].weekday() for i in range(len(df))]

    #Grouping
    groups = df.groupby('Date').agg('count')
    groupsWeekday = df.groupby('day').agg('count')
    groupsWeek = df.groupby('weekno').agg('count')
    groupsTime = df.groupby('Booking_Date').agg('count')
    # groupsHour = pittdf.groupby('Hour').agg('count')
    groups1 = groups[['Crime_Family1']]

    #Below is a plot for total crimes, for each day of the week. 

    fig, ax = plt.subplots(figsize = (30,10))
    fig.canvas.draw()
    labels = ['0','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    ax.set_xticklabels(labels)
    plt.title("Day of the Week Vs No. of Crimes")
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Crimes')
    plt.bar(groupsWeekday.index, groupsWeekday.Crime_Family1,width=0.2,color='c',align='center');
    plt.savefig("static/images/crimesByWeekdays.png")
#    plt.show()
    print('weekdays - done')
    return groups1

# check stationarity

def stationarity_test(timeseries,values):
    
    #Determing the rolling statistics for a month for the data 
    rollingmean = timeseries.rolling(window=30,center=True).mean()
    rollingstd = timeseries.rolling(window=30,center=True).std()
    plt.figure(figsize=(20,6))
    #Plotting the rolling statistics
    orig = plt.plot(timeseries, color='c',label='Original')
    mean = plt.plot(rollingmean, color='red', label='Rolling Mean')
    std = plt.plot(rollingstd, color='black', label = 'Rolling Std')

    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation for the Time Series')
    plt.savefig("static/images/stationarity_test.png")
 #   plt.show(block=True)
    
    #Performing the Dickey-Fuller test:
    print('Results of the Dickey-Fuller Test:')
    dftest = adfuller(values, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistics','P-value','No. of Lags Used','Number of Observations Used'])
    
    df_results =[]
    df_results.append('Results of the Dickey-Fuller Test:')
    
    f_number = round(dftest[0], 6)
    result_string = f'Test Statistics : {f_number}'
    df_results.append(result_string)
    
    f_number = round(dftest[1], 6)
#    f_number'{:.10f}'.format(1e-10)
    a_number = '{:.6f}'.format(f_number)
    print('a_number', a_number)
    result_string = f'P-value : {a_number}'
    df_results.append(result_string)
    
    f_number = round(dftest[2], 6)
    result_string = f'No. of Lags Used: {f_number}'
    df_results.append(result_string)
    
    f_number = round(dftest[3], 6)
    result_string = f'No. of Observations Used: {f_number}'
    df_results.append(result_string)

    for key,value in dftest[4].items():
        key_string = "Critical Value (" + key + ")"
        f_number =  round(value, 6)
        result_string = f'{key_string} : {f_number}'
        df_results.append(result_string)
    print('results - done')
    
    
#    for key,value in dftest[4].items():
#        dfoutput['Critical Value (%s)'%key] = value
#    print(dfoutput)
    with open('Resources/stationarity.txt', 'w') as f:
        i = 0
        for line in df_results:
            f.write(line + "\n")
            i+=1

# The Dickey Fuller test code has been referenced from https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/

def two_plots():
    groups1 = chart_by_weekday()
    stationarity_test(groups1,groups1.Crime_Family1)
    print('done')
















