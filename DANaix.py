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
        # DANaix.cxn.close()

    @staticmethod
    def get_client_token(client_id):

        sql = """SELECT access_token from test.test WHERE client_id ='efb4da00b3d22f63a53c8f0b9b96c553' ORDER BY start_date DESC limit 1"""
        DANaix.cursor.execute(sql, client_id)
        access_token = DANaix.cursor.fetchone()
        # DANaix.cxn.close()
        return access_token