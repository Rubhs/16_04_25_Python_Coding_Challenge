#utility/PropertyUtil.py

import configparser
import os

class PropertyUtil:
  
  @staticmethod
  def getPropertyString():
    config=configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__),"config.properties"))
    
    server=config.get('DEFAULT','server')
    database=config.get('DEFAULT','database')
    trusted_connection=config.get('DEFAULT','trusted_connection')
    driver=config.get('DEFAULT','driver')
    
    conn_str= f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    
    return conn_str