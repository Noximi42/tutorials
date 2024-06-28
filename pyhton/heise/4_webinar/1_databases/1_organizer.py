import sqlite3 as sql

# noinspection SqlNoDataSourceInspection, SqlDialectInspection
CREATE_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS tasks
(
    id       INTEGER PRIMARY KEY,
    name     TEXT    NOT NULL,
    priority INTEGER NOT NULL
);
'''.strip()

# noinspection SqlNoDataSourceInspection, SqlDialectInspection
INSERT_TASK_SQL = '''
INSERT INTO tasks (name, priority)
VALUES (?, ?);
'''.strip()

# noinspection SqlNoDataSourceInspection, SqlDialectInspection
SELECT_SQL = '''
SELECT *
FROM tasks;
'''.strip()

# noinspection SqlNoDataSourceInspection, SqlDialectInspection
UPDATE_SQL = '''
UPDATE tasks
SET PRIORITY = ?
WHERE name = ?;
'''.strip()

# noinspection SqlNoDataSourceInspection, SqlDialectInspection
DELETE_SQL = '''
DELETE
FROM tasks
WHERE name = ?;
'''.strip()


def main():
    connection = sql.connect('organizer.db')
    cursor = connection.cursor()

    # cursor.execute(CREATE_TABLE_SQL)
    # cursor.execute(INSERT_TASK_SQL, ('Einkaufen', 1))

    connection.commit()

    execution = cursor.execute(SELECT_SQL)
    rows = execution.fetchall()
    for row in rows:
        print(row)

    print('-' * 100)

    # cursor.executemany(INSERT_TASK_SQL, (('Wäsche waschen', 2), ('Bügeln', 5), ('Fenster putzen', 10)))
    # connection.commit()

    execution = cursor.execute(SELECT_SQL)
    row = execution.fetchone()
    while row:
        print(row)
        row = execution.fetchone()

    print('-' * 100)
    
    execution = cursor.execute(SELECT_SQL)
    for row in execution:
        print(row)

    print('-' * 100)

    cursor.execute(UPDATE_SQL, (3, 'Fenster putzen'))
    connection.commit()

    execution = cursor.execute(SELECT_SQL)
    for row in execution:
        print(row)

    print('-' * 100)

    cursor.execute(DELETE_SQL, ('Bügeln',))
    connection.commit()

    execution = cursor.execute(SELECT_SQL)
    for row in execution:
        print(row)

    print('-' * 100)

    connection.row_factory = sql.Row # Return rows as dictionary-like objects.
    cursor = connection.cursor()

    execution = cursor.execute(SELECT_SQL)
    for row in execution:
        print(f"{row['id']:3} | {row['name']:14} | {row['priority']:2}")


    connection.close()

if __name__ == '__main__':
    main()
