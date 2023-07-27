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
    c.execute("SELECT * FROM items")
    return c.fetchall()

def addItem(company, id, title, hlink):
    with conn:
        c.execute(f"INSERT INTO items VALUES(:company,:id,:title,:hlink) ON CONFLICT(company, id) DO NOTHING", {'company':company, 'id':id, 'title':title, 'hlink':hlink})


def deleteItem(company, id):
    with conn:
        c.execute("DELETE from items WHERE company = :company AND id = :id", {'company':company, 'id':id})
        
def deleteAll():
    with conn:
        c.execute("DELETE from items")

def exist(company, id):
    c.execute("SELECT 1 FROM items WHERE company = :company AND id = :id LIMIT 1", {'company':company, 'id':id})
    return c.fetchone() is not None

def select(company, id):
    c.execute("SELECT * FROM items WHERE company = :company AND id = :id", {'company':company, 'id':id})
    return c.fetchone()


# print(select('SuperMicro', 22420))
# print(getList())
# conn.close()