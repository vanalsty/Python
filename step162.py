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


src = ('information.docx', 'Hello.txt', 'myImage.png',\
       'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for file in src:
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
