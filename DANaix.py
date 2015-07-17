__author__ = 'lucas.arana'

# -*- coding: utf-8 -*-
from SingleDB import SingleDB

class DANaix:
    """Class containing all necessary queries for every Petition"""
    cursor_object = SingleDB()
    cxn = cursor_object.open_data_base()
    cursor = cxn.cursor()

    @staticmethod
    def first_query():
        sql = ("INSERT INTO test set idtest = 5")
        DANaix.cursor.execute(sql)
        DANaix.cxn.commit()
        DANaix.cxn.close()
