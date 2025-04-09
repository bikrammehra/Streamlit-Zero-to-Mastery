import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("Stock Market Dashboard")

ticker = st.text_input("Enter stock ticker (eg. AAPL, MSFT):", "AAPL")
stock_data = yf.Ticker(ticker)
hist = stock_data.history(period="1mo")

fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=hist.index,
    open=hist["Open"],
    high=hist["High"],
    low=hist["Low"],
    close=hist["Close"],
    name="Candlestick",
))

st.plotly_chart(fig)