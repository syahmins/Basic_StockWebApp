# stock market dashboard to show some chart and data
# code tutorial video: https://www.youtube.com/watch?v=eNDADqa9858

# import the libraries
import streamlit as st
import pandas as pd
from PIL import Image

# title and image
st.write("""
# Stock Web market Application
**Visually** show data on a stock. Date range from late May 2020 to late May 2021
""")

# if you want to put a logo or banner the put it here and uncomment this two lines.
# image = Image.open("/home/syahmin/Documents/code/kursus/stock_web_app/data/logo.png")
# st.image(image, use_column_width=True)

# sidebar header
st.sidebar.header('Indikator Pencarian')


# function to get user input
def get_input():
    start_date = st.sidebar.text_input("Tanggal Awal", "2020-05-20")
    end_date = st.sidebar.text_input("Tanggal Akhir", "2021-05-20")
    stock_symbol = st.sidebar.text_input("Kode Saham", "ACES")
    return start_date, end_date, stock_symbol


# function to get the data from csv
# this part have a big chance to get it directly from Yahoo Finance
# df --> data frame
def get_data(symbol, start, end):
    if symbol.upper() == 'ACES':
        df = pd.read_csv("/home/syahmin/Documents/code/kursus/stock_web_app/data/ACES.JK.csv")
    elif symbol.upper() == 'CLEO':
        df = pd.read_csv("/home/syahmin/Documents/code/kursus/stock_web_app/data/CLEO.JK.csv")
    elif symbol.upper() == 'ERAA':
        df = pd.read_csv("/home/syahmin/Documents/code/kursus/stock_web_app/data/ERAA.JK.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

    # get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # set start and end index rows to 0
    start_row = 0
    end_row = 0

    # start the date from the top of data set and go down to see if the users start date is less than or
    # equal to the date in the data set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):  # df at Date column at i
            start_row = i
            break

    # start the date from the bottom of data set and go up to see if the users end date is greater than or
    # equal to the date in the data set
    for j in range(0, len(df)):
        if end <= pd.to_datetime(df['Date'][len(df) - 1 - j]):  # df at Date column will track from the very bottom row
            end_row = len(df) - 1 - j
            break

    # set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    # return the data set at the location from start_row to the end_row and take all the columns (symbol ":")
    return df.iloc[start_row:end_row + 1, :]


# get the input
start, end, symbol = get_input()

# get the data
df = get_data(symbol, start, end)

# display the Close Price in line chart
st.header(symbol + " Close Price\n")
st.line_chart(df['Close'])

# display the Volume in line chart
st.header(symbol + " Volume\n")
st.line_chart(df['Volume'])

# get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
