import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-J9FA226;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

init_status='Available'
def Add_Book(Title,Author,Status):
    record=(Title,Author,Status)
    sql="""insert into dbo.books_store values(?,?,?)"""
    cursor.execute(sql,record)
    conn.commit()
    print("Book Inserted Successfully")

#Add_Book("iugh","qaxd",init_status)


def Delete_Book(id):
    cursor.execute('SELECT title,author FROM dbo.books_store where book_id=?',id)
    r=''
    for row in cursor:
        if len(row)!=0:
            r=row
            print(r)
    sql="""Delete from dbo.books_store where book_id=?"""
    cursor.execute(sql,id)
    conn.commit()
    if len(r)!=0:
        print(f"Removed Title:{r[0]}, Author:{r[1]} Successfully")
    else:
        print(f"book_id:{id} Not Found")

#Delete_Book(4)
def View_Book():
    cursor.execute('SELECT * FROM dbo.books_store')
    for row in cursor:
        if len(row)!=0:
            print(f'Book id : {row[0]}, Title : {row[1]}, Author : {row[2]} , Status : {row[3]}')

#View_Book()

def Issue_Book(id):
    print("I'm in view")
    cursor.execute('SELECT * FROM dbo.books_store where book_id=? and status=\'Available\'', id)
    for row in cursor:
        print(len(row))
        if len(row)==0:
            print("Requested book not available")
        else:
            print(f'Issued Book_id: {row[0]}, Title: {row[1]}, Author : {row[2]}')
            cursor.execute('Update dbo.books_store set status=\'Not Available\' where book_id=?', id)
    conn.commit()


#Issue_Book(14)

def Return_Book(id):
    print("I'm in view")
    cursor.execute('SELECT * FROM dbo.books_store where book_id=? and status=\'Not Available\'', id)
    for row in cursor:
        print(len(row))
        if len(row)==0:
            print("Requested book not available")
        else:
            print(f'Returned Book_id: {row[0]}, Title: {row[1]}, Author : {row[2]}')
            cursor.execute('Update dbo.books_store set status=\'Available\' where book_id=?', id)
    conn.commit()