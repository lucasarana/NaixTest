__author__ = 'lucas.arana'

# -*- coding: utf-8 -*-
from SingleDB import SingleDB

class DANaix:
    """Class containing all necessary queries for every Petition"""

    cursor_object = SingleDB()
    cxn = cursor_object.open_data_base()
    cursor = cxn.cursor()

    first_query()

    @staticmethod
    def first_query():
        sql = ("INSERT INTO test set idtest = 1")
        cursor.execute(sql)
        cxn.commit()
        cxn.close()

