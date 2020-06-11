import sqlite3

import os

        
conn = sqlite3.connect('step162.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()


src = "C:\\PythonStep162" 

sourceFiles = os.listdir(src) 
for file in sourceFiles:
    if file.endswith(".txt"):
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_fileList(col_fileName)VALUES (\"%s\");" \
                %(file))
        conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileName FROM tbl_fileList")
    txtFiles = cur.fetchall()
    print(txtFiles)

conn.close()
