__author__ = 'lucas.arana'

# -*- coding: utf-8 -*-
import datetime
from SingleDB import SingleDB

class DANaix:
    """Class containing all necessary queries for every Petition"""
    cursor_object = SingleDB()
    cxn = cursor_object.open_data_base()
    cursor = cxn.cursor()

    @staticmethod
    def initiliaze_client(client_id, access_token, refresh_token='Null', end_date=20150505):
        now_date = datetime.datetime.now()
        f = '%Y-%m-%d %H:%M:%S'
        now = now_date.strftime(f)
        sql = """INSERT INTO test
                 (client_id, access_token, start_date)
                 values (%s, %s, %s)
                 """
        DANaix.cursor.execute(sql, (client_id, access_token, now))
        DANaix.cxn.commit()
        DANaix.cxn.close()
