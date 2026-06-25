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
i learnt that from a friend of mine'),
                
('do you ever feel so alone that you could implode and no one would know?'),

('searching for a bloodstain, bandages are clean
baby, take it easy following a whim
listen how the heart beats lying next to him'),

('sunshine through the curtain, music in my head
still be singing to you long after we’re dead'),

('here come my genie in a screw cap bottle
to grant me temporary solace
i could never be without her
i had to write a song about her
who am i without you now?'),

('my final act of love was surrender'),

('sung over the bones of you and I
words spun into daisy wheels in my mind
i am vasilisa, guide me through the night
nothing more will enter me but light'),

('i can''t heal, you keep ripping me open
i can''t feel you, keep ripping me open'),

('every now and then in a far off land
familiar but foreign, a liminal feeling
i know you know me now like the back of your hand
but can I still get your heart reeling?'),

('stranded here on mars
what''s the odds you''d get stuck here too?'),

('come hell or heaven, angels or devils
i won''t move
and I don''t care what happens after
i won''t quit on you'),

('chaos-ridden inner space
turns out home is not a place
when I think home, I see your face'),

('chaos reaches outer space
turns out nowhere is a place
desire, tidal wave, i can''t tame it
i''m not a water bender, can''t change it
i''m thinking maybe i need a surfboard 
just gotta ride it out, get it all out
when you''re not mine, am i allowed?'),

('you could call me miss paramour
fate’s got a funny way, baby');
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
