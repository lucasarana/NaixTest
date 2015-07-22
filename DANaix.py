__author__ = 'lucas.arana'

# -*- coding: utf-8 -*-
import datetime
from SingleDB import SingleDB


class DANaix:
    """
    Class containing all necessary queries for the Data Base
    """
    cursor_object = SingleDB()
    cxn = cursor_object.open_data_base()
    cursor = cxn.cursor()

    @staticmethod
    def initialize_client(user_id, access_token, refresh_token='Null', end_date=20150505):
        """
        Creates Client in the Data Base
        :param user_id: The user who is performing the action
        :param access_token: Access token got from the code redirected
        :param refresh_token: Unused yet. Must correct
        :param end_date: Unused yet. Must correct
        Note: Should overwrite if user exists
        """
        now_date = datetime.datetime.now()
        f = '%Y-%m-%d %H:%M:%S'
        now = now_date.strftime(f)
        sql = """INSERT INTO test
                 (user_id, access_token, start_date)
                 values (%s, %s, %s)
              """
        DANaix.cursor.execute(sql, (user_id, access_token, now))
        DANaix.cxn.commit()

    @staticmethod
    def get_client_token(user_id):
        """
        Gets the client LAST access token found.
        :param user_id: The user who is performing the action
        """

        sql = "SELECT access_token from test.test WHERE user_id ='"
        sql += str(user_id)
        sql += "' ORDER BY start_date DESC limit 1"

        DANaix.cursor.execute(sql, user_id)
        access_token = DANaix.cursor.fetchone()[0]
        return access_token
