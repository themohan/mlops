import pandas as pd
import datetime
import streamlit as st
import yfinance as yf

st.write(
    """
    # STock Price Analyser
    Shown are the stock price of apple.
    """
)

ticker_symbol = "AAPL"

col1, col2 = st.columns(2)

## Start date of analysis
with col1:
    start_date = st.date_input("Input Starting Date",
                               datetime.date(2019, 1, 1))

## End date of analysis
with col2:
    end_date = st.date_input("Input Ending Date",
                               datetime.date(2019, 12, 31))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start=f"{start_date}", end=f"{end_date}")

st.dataframe(ticker_df)

## showcasing chart
st.write("""
## Daily Closing Price CHart
""")
st.line_chart(ticker_df.Volume)
