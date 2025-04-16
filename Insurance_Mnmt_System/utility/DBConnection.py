# utility/DBConnection.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pyodbc
from utility.PropertyUtil import PropertyUtil

class DBConnection:
  
  connection=None
  @staticmethod
  def getConnection():
    if DBConnection.connection is None:
      try:
        conn_str=PropertyUtil.getPropertyString()
        DBConnection.connection=pyodbc.connect(conn_str)
        print("Database Connected Successfully")
      
      except Exception as e:
        print("Database Connection Failed: ",e)
        
    return DBConnection.connection
    
if __name__ == "__main__":
    DBConnection.getConnection()