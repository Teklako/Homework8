#დავალება1
import sqlite3

conn = sqlite3.connect("books_db.sqlite")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE books
(books_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(20),
autor VARCHAR(30),
release_year date(20),
price INT);
""")

cursor.execute("""INSERT INTO books(title, autor, release_year, price) VALUES("ვა,სოფელო", "ზაირა არსენიშვილი", 2021,20);""")
conn.commit()

satauri = "სამოსელი პირველი"
saxeli = "გურამ დოჩნაშვილი"
release = 2021
fasi = 21
cursor.execute("""INSERT INTO books(title, autor, release_year, price) VALUES(?,?,?,?)""", (satauri,saxeli,release,fasi));
conn.commit()

books_list = [
    ("იგი","ჯემალ ქარჩხაძე", 1589,12),
    ("ვეფხისტყაოსანი","შოთა რუსთაველი", 1656,15),
    ("ბახტრიონი","ვაჟა_ფშაველა", 1712,13),
    ("აჩრდილი","ილია ჭავჭავაძე",1234,45)
]
cursor.executemany("INSERT INTO books(title, autor, release_year, price) VALUES(?,?,?,?)", books_list)
conn.commit()

conn.close()

#დავალება2
import sqlite3

conn = sqlite3.connect("titanic.sqlite3")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE titan
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              passenger_name VARCHAR(50),
              age INTEGER,
              sex VARCHAR(30),
              ticket  VARCHAR(30),
              cabin  VARCHAR(30));''')
cursor.execute("""INSERT INTO titan(passenger_name,age,sex,ticket,cabin) VALUES("tekla",18,"mdedrobiti","a","j9");""")
conn.commit()

passenger = input("saxeli:")
ago = input("asaki:")
sqesi = input("sqesi:")
bileti = input("bileti:")
cabina = input("cabina:")

cursor.execute("""INSERT INTO titan(passenger_name,age,sex,ticket,cabin) VALUES(?,?,?,?,?)""", (passenger,ago,sqesi,bileti,cabina));
conn.commit()

for i in range(3):
    titan_list = [
    input("saxeli:"),
    input("asaki:"),
    input("sqesi:"),
    input("bileti:"),
    input("cabina:")
    ]
    print(i)
cursor.executemany("INSERT INTO titan(passenger_name,age,sex,ticket,cabin) VALUES(?,?,?,?,?)", titan_list)
conn.commit()
cursor.close()


#დავალება3
class Movie:
    def __init__(self,title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb
    def __str__(self):
        return f"{self.title},{self.genre},{self.year},{self.imdb} "
import sqlite3
conn = sqlite3.connect("movies.sqlite3")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE filmebi
             (movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
              title VARCHAR(50),
              genre VARCHAR(20),
              year INTEGER,
              imdb  VARCHAR(30);
''')
cursor.execute("""INSERT INTO filmebi(title,genre,year,imdb) VALUES("spider man","satavgadasavlo",2020,"CD");""")
conn.commit()

obj1 = Movie("სიამაყე და ცრურწმენა","დრამა",2018,"CD")
cursor.execute("""INSERT INTO filmebi(title,genre,year,imdb) VALUES(?,?,?,?)""", (obj1));
conn.commit()

movie2 = Movie("sens da chems shoris", "drama", 1972, "CD")
movie3 = Movie("udiplomo sasidzo", "komedia", 2008, "CD")
movie4 = Movie("titanici", "drama", 1997, "CD")

movie_list = [(movie2.title, movie2.genre, movie2.year, movie2.imdb),
              (movie3.title, movie3.genre, movie3.year, movie3.imdb),
              (movie4.title, movie4.genre, movie4.year, movie4.imdb)]

cursor.executemany("INSERT INTO filmebi(title, genre, yearr, imdb) VALUES (?,?,?,?)", movie_list)

conn.close()
