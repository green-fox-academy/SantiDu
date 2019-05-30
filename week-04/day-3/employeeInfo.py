import psycopg2, csv, json, xml.etree.ElementTree as ET

conn = psycopg2.connect(host="localhost",
                        database="workshop",
                        user="postgres",
                        password="password")

cur = conn.cursor()

cur.execute("CREATE TABLE employees (\
id SERIAL PRIMARY KEY,\
name VARCHAR,\
gender VARCHAR CONSTRAINT male_female CHECK(gender IN ('Male', 'Female')),\
birth_date DATE,\
monthly_salary INTEGER CONSTRAINT positive_salary CHECK(monthly_salary > 0),\
nationality VARCHAR,\
university VARCHAR,\
branch VARCHAR,\
position VARCHAR\
);")


tree = ET.parse('employees.xml')
root = tree.getroot()
for record in root:
    name = record.findtext("name")
    birth_date = record.findtext("birth_date")
    branch = record.findtext("branch")
    gender = record.findtext("gender")
    salary_by_year = int(record.findtext("salary_by_year"))
    monthly_salary = round(salary_by_year / 12)
    position = record.findtext("position")
    
    query = "INSERT INTO employees (name, gender, birth_date, monthly_salary, branch, position) \
VALUES (%s, %s, %s, %s, %s, %s);"
    cur.execute(query, (name, gender, birth_date, monthly_salary, branch, position))


with open("employees.json") as f:
    jsond = json.load(f)
    for record in jsond:
        name = record["name"]
        birth_date = record["birth_date"]
        nationality = record["nationality"]
        gender = record["gender"]
        monthly_salary = record["monthly_salary"]
        university = record["university"]

        query = "INSERT INTO employees (name, gender, birth_date, monthly_salary, nationality, university)\
VALUES (%s, %s, %s, %s, %s, %s);"
        cur.execute(query, (name, gender, birth_date, monthly_salary, nationality, university))


with open('employees.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["first_name"] + " " + row["last_name"]
        birth_date = row["birth_date"]
        gender = row["gender"]
        monthly_salary = row["monthly_salary"]

        query = "INSERT INTO employees (name, gender, birth_date, monthly_salary) \
VALUES (%s, %s, %s, %s);"
        cur.execute(query, (name, gender, birth_date, monthly_salary))




cur.close()
# conn.commit()
conn.close()