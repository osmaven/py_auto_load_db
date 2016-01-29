import sys
from sqlalchemy import create_engine
import pandas as pd
tabla=sys.argv[1]
csv='/Users/oventura/git/py_auto_load_pg/' + tabla

engine = create_engine('postgresql://gpadmin:changeme@192.168.177.145/gpadmin')
df = pd.read_csv(csv)
df.to_sql(tabla, engine)
