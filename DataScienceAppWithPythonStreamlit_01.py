# Data Science Data Apps with Streamlit
# https://www.youtube.com/watch?v=JwSS70SZdyM&ab_channel=freeCodeCamp.org
# Also, markdown reference https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App

These are the stocks closing price and volume of Google!

""")

def main():
  # Define the ticker symbol
  ticker_symbol = 'GOOGL'
  # get data on this ticker
  ticker_data = yf.Ticker(ticker_symbol)
  # Get the historical prices for this symbol
  ticker_df = ticker_data.history(period='1d', start='2010-05-31', end='2022-05-31')

  st.write("""## Closing Price""")
  st.line_chart(ticker_df.Close)
  st.write("""## Volume""")
  st.line_chart(ticker_df.Volume)

  main
