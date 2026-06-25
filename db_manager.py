import sqlite3
from random import randint

con = sqlite3.connect("database.db")
cur = con.cursor()

def create_table():   
    cur.execute("CREATE TABLE IF NOT EXISTS posts(" \
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
    "post_text VARCHAR(255) NOT NULL) " \
)
    con.commit()

def insert_data():
    cur.execute("""
    INSERT INTO posts (post_text) VALUES 
('and there were no words for the way that you felt
so you opened your mouth and you started to sing'),

('some flowers bloom when the green grass grows
our praise is not for them
but the ones who bloom in the bitter snow'),

('i knew you before we met
and i dont even know you yet
all i know is youre someone i have always known'),

('i am more than memory
i am what might be, i am mystery
you know me, so show me'),

('melt with you til it all turns black
melt with you til it just feels sad'),

('in the fog, in the flood beams, on a lark
in their midst, our silhouettes kiss
guess thats showbiz'),

('i know you see me dancing wildly in the fog of your memory
you dont have to tell me, i can still believe'),

('i wanna do it again, i wanna dance in the strobe light
i wanna choke on the smoke and feel your eyes on me'),

('you say youre a winter bitch but summers in your blood
you cant help but become the sun'),

('everythings growing in our garden
you dont have to know that its haunted'),

('and suddenly hades was only a man
with a taste of nectar upon his lips'),

('to know how it ends and still begin to sing it again
as if it might turn out this time
i learnt that from a friend of mine');
    """)
    con.commit()

def get_random_quote():

    cur.execute("SELECT post_text FROM posts ORDER BY RANDOM()")    
    result = cur.fetchone()

    if result:
        return result[0]
    return None

create_table()
insert_data()
