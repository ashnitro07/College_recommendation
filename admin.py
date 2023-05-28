import sqlite3

# Create a connection to the database (or open it if it already exists)
conn = sqlite3.connect('database1.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS college1 (
                    sno number primary key,
                    cname varchar(30),
                    loc varchar(30),
                    coname varchar(30),
                    agp varchar(30),
                    hostel varchar(3),
                    zone number,
                    y1 number(4),
                    co1 number(5),
                    y2 number(4),
                    co2 number(5),
                    y3 number(4),
                    co3 number(5),
                    y4 number(4),
                    co4 number(5),
                    y5 number(4),
                    co5 number(5),
                    yfin number(5)
                )''')

# Insert data into the table
data = [
    (1,'College of Engineering','Trivandrum','AE','GOVT','yes',2,2017,3935,2018,2694,2019,2569,2021,2987,2022,3398,99999),
    (2,'College of Engineering','Trivandrum','civil','GOVT','yes',2,2017,1875,2018,2155,2019,3097,2021,3113,2022,4939,99999),
    (3,'College of Engineering','Trivandrum','CS','GOVT','yes',2,2017,732,2018,606,2019,479,2021,481,2022,443,99999),
    (4,'College of Engineering','Trivandrum','ECE','GOVT','yes',2,2017,1005,2018,837,2019,788,2021,713,2022,618,99999),
    (5,'College of Engineering','Trivandrum','EEE','GOVT','yes',2,2017,1712,2018,1402,2019,1609,2021,1659,2022,1657,99999),
    (6,'College of Engineering','Trivandrum','MECH','GOVT','yes',2,2017,919,2018,935,2019,1532,2021,2473,2022,986,99999),
    (7,'College of Engineering','Kozhikode','AE','GOVT','no',3,2017,16665,2018,20235,2019,13501,2021,12326,2022,19646,99999),
    (8,'College of Engineering','Kozhikode','MECH','GOVT','no',3,2017,5908,2018,7754,2019,10914,2021,13554,2022,24961,99999)
]

cursor.executemany('INSERT OR REPLACE INTO college1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)

conn.commit()
conn.close()
