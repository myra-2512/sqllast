import pandas as pd
import numpy as np

import sqlite3

database='basketball.sqlite'
conn=sqlite3.connect(database)

tables=pd.read_sql("""SELECT *
                    FROM sqlite_master  
                    WHERE type='table';""", conn)
print(tables)

team=pd.read_sql("""SELECT *
                    FROM Team""", conn)
print(team)

team_atr=pd.read_sql("""SELECT *
                    FROM Team_Attributes""", conn)
print(team_atr)

team1=pd.read_sql("""SELECT *
                    FROM Team_Attributes
                    WHERE ID IN (SELECT id
                                 FROM Team
                                 WHERE state = 'New York')""", conn)
print(team1)