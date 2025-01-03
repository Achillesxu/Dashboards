# -*- coding: utf-8 -*-
"""
@Time : 2025 1月 02 17:40
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
import pandas as pd
import streamlit as st

from st_func.datas import SupaBaseData

sbd = SupaBaseData(
    st.secrets['supabase']['SUPABASE_URL'],
    st.secrets['supabase']['SUPABASE_KEY'])

account_list = sbd.select_account_list()
type_list = sbd.select_account_bill_types()


def get_bill_data(account: str, bill_type: str, ymd: str):
    data = sbd.select_account_bills(account, bill_type, ymd)
    return pd.DataFrame(data)


st.title('账单')

select_cols = st.columns(3)

with select_cols[0]:
    account_sel_opt = st.selectbox(
        '账户',
        account_list,
        index=1,
        key='account_sel_opt'
    )

with select_cols[1]:
    type_sel_opt = st.selectbox(
        '账单类型',
        type_list,
        index=1,
        key='type_sel_opt'
    )

with select_cols[2]:
    year_sel_opt = st.selectbox(
        '年份',
        ['2025', '2024', '2023'],
        index=1,
        key='year_sel_opt'
    )

df = get_bill_data(account_sel_opt, type_sel_opt, year_sel_opt)
if not df.empty:
    st.bar_chart(
        df,
        x='ymd',
        y=['fee', 'count'],
        x_label='年月日',
        y_label=['费用', '数量'],
        color = ["#FF0000", "#0000FF"],
        stack=False,
        height=500
    )
else:
    st.info('暂无数据')
