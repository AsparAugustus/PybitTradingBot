import seaborn as sns
import os
from functions import get_wallet_usdt_balance

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import random
import datetime

filename = 'equity_curve.csv'

def save_chart_data():
    # Check if the file exists
    if not os.path.exists(filename):

        timestamp = int(datetime.datetime.now().timestamp())
        date_time = datetime.datetime.now()

        # Create a new DataFrame with a date column and a number column
        df = pd.DataFrame({'timestamp': [timestamp],
                            'date_time': [date_time],
                        'equity': [get_wallet_usdt_balance()]})

        
    


        # # Convert the data to a Pandas DataFrame
        # df['dates'] = pd.to_datetime(df['dates'])
        # df = df.set_index('dates')

        # Save the DataFrame to the file
        df.to_csv(filename, index=False)

        
    else:
        # Load the existing DataFrame from the file
        df = pd.read_csv(filename)

        timestamp = int(datetime.datetime.now().timestamp())
        date_time = datetime.datetime.now()

        equity = get_wallet_usdt_balance()
        # equity = 333




        new_row = pd.DataFrame({'timestamp': [timestamp], 'date_time': [date_time], 'equity': [equity]})

        df = df.append(new_row, ignore_index=True)

        date_points = df['timestamp']
        equity_curve = df['equity']





        # Compute the moving average
        rolling_mean = df.rolling(window=10).mean()


        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(df['timestamp'], df['equity'])
        ax.plot(rolling_mean.index, rolling_mean['equity'], label='Moving Average (10 Days)', color='red')

        # Setting the style to dark grid
        plt.style.use("dark_background")

        plt.fill_between(date_points, equity_curve, equity_curve[0], where=(np.greater(equity_curve, equity_curve[0])), color="#00FF00", alpha=0.3)
        plt.fill_between(date_points, equity_curve, equity_curve[0], where=(np.less(equity_curve, equity_curve[0])), color="#FF0000", alpha=0.3)
        ax.axhline(y=equity_curve[0], color='gray', linestyle='--')
        ax.xaxis.set_major_locator(plt.MaxNLocator(20))
        ax.set_facecolor("black")
        plt.xticks(rotation=45)

        plt.title("Equity Curve", fontsize=20)
        plt.xlabel("Time")
        plt.ylabel("Wallet Balance")

        # plt.show()

        # Save the DataFrame to the file
        df.to_csv(filename, index=False)


def display_chart():

    # Load the existing DataFrame from the file
    df = pd.read_csv(filename)



    



    df['date_time'] = pd.to_datetime(df['date_time'])
    date_points = df['date_time']
    equity_curve = df['equity']

    # Compute the moving average
    rolling_mean = equity_curve.rolling(window=2).mean()

    fig, ax = plt.subplots(figsize=(40, 10))
    ax.plot(date_points, equity_curve)
    ax.plot(date_points, rolling_mean, label='Moving Average (2 Days)', color='red')



    # Setting the style to dark grid
    plt.style.use("dark_background")

    print(equity_curve[0], equity_curve[0], equity_curve[0])


    plt.fill_between(date_points, equity_curve, equity_curve[0], where=(np.greater(equity_curve, equity_curve[0])), color="#00FF00", alpha=0.3)
    plt.fill_between(date_points, equity_curve, equity_curve[0], where=(np.less(equity_curve, equity_curve[0])), color="#FF0000", alpha=0.3)
    ax.axhline(y=equity_curve[0], color='gray', linestyle='--')
    ax.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax.set_facecolor("black")
    plt.xticks(rotation=45)

    plt.title("Equity Curve", fontsize=20)
    plt.xlabel("Time")
    plt.ylabel("Wallet Balance")

    plt.show()






