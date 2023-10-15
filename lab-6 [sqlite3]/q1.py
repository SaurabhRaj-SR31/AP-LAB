import sqlite3
# conn = sqlite3.connect('student.db')
# c = conn.cursor()
# c.execute("DROP TABLE student")
# c.execute("DROP TABLE attendance")
# conn.commit()
# conn.close()


def create_new(_id, name, branch, grade, marks):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("INSERT INTO STUDENT VALUES(?,?,?,?,?)",
              (_id, name, branch, grade, marks))
    conn.commit()
    conn.close()


def read_data(_id):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM student WHERE ID = (?)", _id)
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def update(_id, field, value):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("UPDATE student SET "+field+"= "+value+" WHERE ID ="+_id+"")
    conn.commit()
    conn.close()


def delete(_id):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("DELETE FROM student WHERE ID=(?)", _id)
    conn.commit()
    conn.close()


def read_branch(branch):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c2 = conn.cursor()
    c.execute("SELECT * FROM student WHERE BRANCH = (?)", (branch,))
    c2.execute("SELECT COUNT(*) FROM student WHERE BRANCH = (?)", (branch,))
    items = c.fetchall()
    for item in items:
        print(item)

    items = c2.fetchall()
    for item in items:
        print(item[0])


def read_marks():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM student ORDER BY MARKS DESC")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


conn = sqlite3.connect('student.db')
c = conn.cursor()

c.execute("""CREATE TABLE student(
           ID INT PRIMARY KEY  NOT NULL,
                NAME TEXT NOT NULL,
                BRANCH TEXT NOT NULL,
                GRADE TEXT,
                MARKS INT
            );""")
c.execute("""CREATE TABLE attendance(
            ID INT NOT NULL,
                DATE TEXT NOT NULL,
                CLASS TEXT NOT NULL
            );""")

print('''Enter
1> To create a new student
2> To read student's data
3> To Update a student's data
4> To Delete student's data.
5> To Diplay students by branch.
6> To display students by marks.
0> To exit\n
''')
opt = 1
while (opt != 0):
    opt = int(input("Enter Option: "))
    if opt == 1:
        print("Enter student details: ")
        _id = int(input("Enter id: "))
        name = input("Enter name: ")
        branch = input("Enter branch: ")
        grade = input("Enter grade: ")
        marks = int(input("Enter marks: "))
        create_new(_id, name, branch, grade, marks)

    if opt == 2:
        print("Reading student details: ")
        _id = (input("Enter id:  "))
        read_data(_id)

    if opt == 3:
        print("Updating student details: ")
        _id = (input("Enter id: "))
        field = input("Enter field to update: ")
        value = input("Enter new value: ")
        update(_id, field, value)

    if opt == 4:
        print("Deleting student details: ")
        _id = (input("Enter id:   "))
        delete(_id)

    if opt == 5:
        print("Get Students by Branch: ")
        branch = (input("Enter Branch: "))
        read_branch(branch)

    if opt == 6:
        print("Sorted by Marks: ")
        read_marks()


conn.commit()
conn.close()
