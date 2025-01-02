# -*- coding: utf-8 -*-
"""
@Time : 2025 1月 02 17:36
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
import streamlit as st
pages = {
    'Home': [
        st.Page('pages/home.py', title='首页', icon='🏠')
    ],
    'PowerBills': [
        st.Page('pages/power_bills.py', title='莱州电费', icon='🏠')
    ]
}

pg = st.navigation(pages, expanded=False)
pg.run()