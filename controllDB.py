import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()
# c.execute("""CREATE TABLE mobie(
#     use_name varchar(32),
#     call_duration int
# )""")
c.execute("delete  FROM mobie ")

conn.commit()
conn.close()
