# -*- coding: utf-8 -*-
"""
@Time : 2025 1月 03 11:19
@Author : xushiyin
@Mobile : 18682193124
@desc :
"""
from supabase import create_client, Client
from loguru import logger


class SupaBaseData:  # noqa
    def __init__(self, sb_url, sb_key):
        self.supabase_url = sb_url
        self.supabase_key = sb_key
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)

    def select_account_list(self):
        resp = self.supabase.table('account').select("account_code").order("account_code", desc=True).execute()
        accounts = [a['account_code'] for a in resp.data]
        return accounts

    def select_account_bill_types(self):
        resp = self.supabase.table('bills').select("type").execute()
        types = list(set([d['type'] for d in resp.data]))
        return types

    def select_account_bills(self, account_code: str, bill_type: str, year: str):
        start_ymd = f'{year}-01-01'
        end_ymd = f'{year}-12-31'

        resp = self.supabase.table('bills').select("ymd, fee, count").match({
            "account_code": account_code,
            "type": bill_type
        }).gte('ymd', start_ymd).lte('ymd', end_ymd).order("ymd", desc=False).execute()
        return resp.data

    def insert_account_bill(self, bill_type: str, account_code: str, ymd: str, fee: float, count: float):
        resp = self.supabase.table('bills').insert({
            "type": bill_type,
            "account_code": account_code,
            "ymd": ymd,
            "fee": fee,
            "count": count
        }).execute()
        logger.info(resp)


if __name__ == '__main__':
    sbd = SupaBaseData('', '')
    # print(sbd.get_account_list())
    # print(sbd.get_account_bill_types())
    # print(sbd.select_account_bills('xcl', '电费', '2024'))
    datas = [
        ['电费', 'xcl', '2023-12-01', 70, 128],
        ['电费', 'xcl', '2023-11-01', 65.08, 119],
        ['电费', 'xcl', '2023-10-01', 77.11, 141],
        ['电费','xcl', '2023-09-01', 80.39, 147],
        ['电费', 'xcl', '2023-08-01', 116.49, 213],
        ['电费', 'xcl', '2023-07-01', 159.69, 292],
        ['电费', 'xcl', '2023-06-01', 82.04, 150],
        ['电费', 'xcl', '2023-05-01', 79.3, 145],
        ['电费', 'xcl', '2023-04-01', 80.94, 148],
        ['电费', 'xcl', '2023-03-01', 107.19, 196],
        ['电费', 'xcl', '2023-02-01', 80.94, 148],
        ['电费', 'xcl', '2023-01-01', 97.9, 179],
    ]
    for d in datas:
        sbd.insert_account_bill(*d)
