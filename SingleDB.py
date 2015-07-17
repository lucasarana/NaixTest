__author__ = 'lucas.arana'

# -*- coding: utf-8 -*-
import config
import mysql.connector
from mysql.connector import errorcode

class SingleDB:
    """Class to open, report or close the MYSQL connection"""

    @staticmethod
    def open_data_base():
        """Opens data base"""
        try:
            cnx = mysql.connector.connect(**config.db_params)
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)

        return cnx
