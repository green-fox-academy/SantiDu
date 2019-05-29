import argparse, psycopg2

parser = argparse.ArgumentParser(prog="todo", description="An application \
that easily keeps track of your day-to-day tasks")

parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument("-l", "--list", action='store_true')
parser.add_argument("-a", "--add")
parser.add_argument("-c", "--check", type=int)
parser.add_argument("-r", "--remove", type=int)

args = parser.parse_args()


lsSQL = "SELECT * FROM todolist;"
addSQL = "INSERT INTO todolist (activity) VALUES (%(activity)s);"
checkSQL = "SELECT * FROM todolist WHERE id = %(id)s;"
rmSQL = "DELETE FROM todolist WHERE id = %(id)s;"

def printfetchall(fetch):
    for id, activity in fetch:
        print(f"{id} - {activity}")

def databaseManeuver():
    conn = psycopg2.connect(host="localhost",
            database="workshop",
            user="postgres",
            password="password")
    cur = conn.cursor()
    if args.list:
        cur.execute(lsSQL)
        printfetchall(cur.fetchall())
    elif args.add:
        cur.execute(cur.mogrify(addSQL, {"activity":args.add}))
    elif args.check:
        cur.execute(cur.mogrify(checkSQL, {"id":args.check}))
        printfetchall(cur.fetchall())
    else:
        cur.execute(cur.mogrify(rmSQL, {"id":args.remove}))
        cur.execute("ALTER SEQUENCE todolist_id_seq RESTART;")
        cur.execute("UPDATE todolist SET id = DEFAULT;")
    conn.commit()
    cur.close()
    conn.close()



if __name__ == "__main__":
    databaseManeuver()