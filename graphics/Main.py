import pandas as pd
import matplotlib.dates as mdates
from matplotlib import pyplot as plt


def plot_data(x, y, title, ylabel, color, label):
    plt.figure(dpi=300, figsize=(12, 6))
    plt.plot(x, y, marker='x', linestyle='-', color=color, label=label)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


data = pd.read_csv('C:/Users/StanDo/PycharmProjects/python_app/project/graphics/docs/Date-3.csv')
data['DATE'] = pd.to_datetime(data['DATE'])

plot_data(data['DATE'], data['CO2'], 'CO2 level by date', 'CO2', 'pink', 'CO2')
plot_data(data['DATE'], data['HCHO'], 'HCHO level by date', 'HCHO', 'r', 'HCHO')
plot_data(data['DATE'], data['PM2.5'], 'PM2.5 level by date', 'PM2.5', 'g', 'PM2.5')
plot_data(data['DATE'], data['PM10'], 'PM10 level by date', 'PM10', 'blue', 'PM10')
plot_data(data['DATE'], data['TEMPERATURE'], 'TEMPERATURE level by date', 'TEMPERATURE', 'orange', 'TEMPERATURE')
plot_data(data['DATE'], data['HUMIDITY'], 'HUMIDITY level by date', 'HUMIDITY', 'black', 'HUMIDITY')
