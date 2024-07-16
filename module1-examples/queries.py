
import sqlite3

# make a cursor and a connection to a new database.
conn = sqlite3.connect('mock_db.sqlite3')
curs = conn.cursor()

# CREATE
create_statement = 'CREATE TABLE test_table (name char(20), age int);'

curs.execute(create_statement)

# READ - (SELECT)
select_all = 'SELECT * FROM test_table;'
curs.execute(select_all)
curs.fetchall()

# UPDATE - (INSERT INTO)
insert_statement = 'INSERT INTO test_table (name, age) VALUES ("Jimmy", 12);'
curs.execute(insert_statement)

# READ - (SELECT)
curs.execute(select_all)
curs.fetchall()

# DELETE

# saves all the changes made by a cursor on this connection channel Permanently alters the database's sqlite3 file. 
conn.commit()

# close your cursor when you're done
curs.close()

##############################

# select_all = '''
# SELECT * 
# FROM charactercreator_character;
# '''