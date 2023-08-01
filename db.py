import sqlite3

conn = sqlite3.connect('data.db', check_same_thread=False)

c = conn.cursor()

# c.execute(f"""CREATE TABLE items (
#             company text,
#             id INT,
#             title text,
#             hlink text,
#             PRIMARY KEY (company, id)
#             )""")
# conn.commit()

def getList():
    """fetches entire list"""
    c.execute("SELECT * FROM items")
    return c.fetchall()

def addItem(company, id, title, hlink):
    """adds item to the current db"""
    with conn:
        c.execute(f"INSERT INTO items VALUES(:company,:id,:title,:hlink) ON CONFLICT(company, id) DO NOTHING", {'company':company, 'id':id, 'title':title, 'hlink':hlink})


def deleteItem(company, id):
    """deletes item using primary keys"""
    with conn:
        c.execute("DELETE from items WHERE company = :company AND id = :id", {'company':company, 'id':id})
        
def deleteAll():
    """deletes entire database"""
    with conn:
        c.execute("DELETE from items")

def exist(company, id):
    """checks whether a certain items exist based on primary keys"""
    c.execute("SELECT 1 FROM items WHERE company = :company AND id = :id LIMIT 1", {'company':company, 'id':id})
    return c.fetchone() is not None

def select(company, id):
    """selects from the database given item from primary keys"""
    c.execute("SELECT * FROM items WHERE company = :company AND id = :id", {'company':company, 'id':id})
    return c.fetchone()