import sqlite3 as sql

# noinspection SqlNoDataSourceInspection, SqlDialectInspection
SELECT_SQL_WITH_PRIORITY = '''
SELECT *
FROM tasks
WHERE priority = ?;
'''.strip()


def print_tasks_with_priority(cursor: sql.Cursor, priority: int):
    execution = cursor.execute(SELECT_SQL_WITH_PRIORITY, (priority,))
    for row in execution:
        print(row[1])


def main():
    connection = sql.connect('organizer.db')
    cursor = connection.cursor()

    print_tasks_with_priority(cursor, 3)
    
    connection.close()


if __name__ == "__main__":
    main()
