import streamlit as st
import yfinance as yt
import random 
import time
import datetime 
import pytz
import logging

kolkata = pytz.timezone('Asia/Kolkata')
st.set_page_config(layout="wide")
st.sidebar.header("Analysis Selection")
nifty50,niftybank = yt.Ticker("^NSEI"),yt.Ticker("^NSEBANK")

try:
    # nifty_data_dict = get_nifty_base_data(['lastPrice','previousClose'])
    daily_change_50 = ((nifty50.get_fast_info()['lastPrice'] - nifty50.get_fast_info()['previousClose'])/nifty50.get_fast_info()['previousClose']) *100
    daily_change_bank = ((niftybank.get_fast_info()['lastPrice'] - niftybank.get_fast_info()['previousClose'])/niftybank.get_fast_info()['previousClose']) *100
    
    time_stamp = datetime.datetime.now(kolkata)
    st.write(f"Last Refresh Time : on {time_stamp.date()}  at {time_stamp.time()}")
    
    with st.container():
        col1,col2 = st.columns(2,border=True)
        if daily_change_50 >0 :
            col1.markdown(f"### :green[NIFTY 50 - {daily_change_50:.2f}%]",unsafe_allow_html=False)
        else:
            col1.markdown(f"### :red[NIFTY 50 - {daily_change_50:.2f}%]",unsafe_allow_html=False)
        if daily_change_bank > 0:
            col2.markdown(f"### :green[NIFTY BANK - {daily_change_bank:.2f}%]",unsafe_allow_html=False)
        else:
            col2.markdown(f"### :red[NIFTY BANK - {daily_change_bank:.2f}%]",unsafe_allow_html=False)

except Exception:
    logging.warning(f"Due to network error the loop has been elapsed : {datetime.datetime.now()}")
# container bodder -get indices list and get the price gap

async def get_nifty_base_data(info_list:list[str]) -> dict:
    # Complete
    return nifty_data_base


def streamlit_app_runner():
    change_sleep_time_begin=datetime.datetime(2025,1,1,15,30,00).time()
    change_sleep_time_end=datetime.datetime(2025,1,1,8,00,00).time()

    while True:#
        # if time beyond 3:30 PM refresh after 1hor till 8:00 am
        # last active date store in state -> if current date != last active date make some state change -> reduction in runs
        if datetime.datetime.now(kolkata).time() <= change_sleep_time_begin and datetime.datetime.now(kolkata).time() >= change_sleep_time_end:
            time.sleep(30)
        elif datetime.datetime.now(kolkata).time() > change_sleep_time_begin:
            time.sleep(60*60)
        st.rerun()

streamlit_app_runner()