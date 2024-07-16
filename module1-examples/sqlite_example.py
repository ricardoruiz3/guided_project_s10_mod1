# Part 1

# Step 0 - import sqlite3
import sqlite3
import queries as q

# Step 1 - Connect to the Database
# please triple check that your DB name is correct.
connection = sqlite3.connect("rpg_db.sqlite3")

# Step 2 - Make the "cursor"
cursor = connection.cursor()

# Step 3 - Write your query
select_all = 'SELECT * FROM charactercreator_character;'

# Step 4 - Execute your query on the cursor
cursor.execute(select_all)

# Step 5 - Pull the results from the cursor
results = cursor.fetchall()

###################

# Part 2

cursor.execute(q.select_all)

###################

# DB Connect function


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


# Make cursor and execute query function


def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results


if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5])