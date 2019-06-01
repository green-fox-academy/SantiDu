import psycopg2

conn = psycopg2.connect(host="localhost",
                 database="slack",
                 user="postgres",
                 password="password")

cur = conn.cursor()



### ouput mentions
cur.execute("""SELECT msg.user_id, men.user_id, COUNT(*)
FROM messages AS msg
JOIN mentions AS men
ON men.msg_id = msg.id
GROUP BY msg.user_id, men.user_id
HAVING msg.user_id IS NOT NULL AND men.user_id IS NOT NULL
ORDER BY count DESC;""")


edges_mentioned = cur.fetchall()


with open("edges_mentioned.csv", "w") as f:
    for edge in edges_mentioned:
        f.write(f"{edge[0]}, {edge[1]}, {edge[2]} \n")

        
        
### output reactions
cur.execute("""SELECT msg.user_id, reac.user_id, COUNT(*)
FROM messages AS msg
JOIN reactions AS reac
ON reac.msg_id = msg.id
GROUP BY msg.user_id, reac.user_id
HAVING msg.user_id IS NOT NULL AND reac.user_id IS NOT NULL
ORDER BY count DESC;""")


edges_reactions = cur.fetchall()


with open("edges_reactions.csv", "w") as f:
    for edge in edges_reactions:
        f.write(f"{edge[0]}, {edge[1]}, {edge[2]} \n")

cur.close()
conn.close()