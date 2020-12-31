import cx_Oracle
import sys
import pandas as pd
from pprint import pprint
import os
from LoggingHandler import LoggingHandler
from OracleConn import OracleConn
import argparse
import logging


class OracleConnEx(OracleConn):
    def __init__(self):
        self.logger = LoggingHandler(self.__class__.__name__, logging.DEBUG)
        self.logger.log.debug('OracleConn init.')

    def dump(self, sql, file):
        """
        dump data from the sql to the file
        """
        try:
            count = 0
            self.cursor.arraysize = 2000
            self.cursor.execute(sql)
            with open(file, 'w') as fw:
                while True:
                    rows = self.cursor.fetchmany()
                    if rows == []:
                        break
                    for row in rows:
                        fw.write('{0}\n'.format(row).replace('(', '').replace(')', ''))
                        count = count + 1
                    if count % 100000 == 0:
                        self.logger.log.info(count)
                self.logger.log.info(count)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 955:
                self.logger.log.error('Table already exists')
            elif error.code == 1031:
                self.logger.log.error("Insufficient privileges")
            self.logger.log.error(error.code)
            self.logger.log.error(error.message)
            self.logger.log.error(error.context)

            # Raise the exception.
            raise


# example how to use this class

if __name__ == "__main__":
    try:
        # file_in = open(sys.argv[1], 'r')
        # data_in = pd.read_csv(file_in, sep='\t', na_filter=False, dtype='unicode')
        ora = OracleConnEx()
        ora.connect('curation', 'cosmic1234', '172.17.72.67', '1521', 'cosp')
        # dump example
        ora.dump('select * from SNP_SOURCE_ANNOT_37_TMP', 'SNP_SOURCE_ANNOT_37_TMP.tsv')

        print('finished')
    # Ensure that we always disconnect from the database to avoid
    # ORA-00018: Maximum number of sessions exceeded.
    finally:
        ora.disconnect()

