# -*- coding: utf-8 -*-
"""
@Time : 2025 1月 02 17:36
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
import streamlit as st

st.set_page_config(
    layout="wide",
)

pages = {
    'Home': [
        st.Page('st_pages/home.py', title='首页', icon='🏠')
    ],
    'Bills': [
        st.Page('st_pages/bills.py', title='账单', icon='🏠')
    ]
}

pg = st.navigation(pages, expanded=False)
pg.run()