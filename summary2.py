from db import DB
import sqlite3

def db():
    db = DB()
    db.setup()
    db.add_item(hire,new_technology,good_conversations,upcoming_events,doubts)
with open("simple.txt", "r") as f:       
    words = list(map(str.strip, f.readlines()))
    try: 
        text=words[words.index("#hire")+1]
        hire=text
        print(text)
        text=words[words.index("#new_technology")+1]
        new_technology=text
        print(text)
        text=words[words.index("#good_conversations")+1]
        good_conversations=text
        print(text)
        text=words[words.index("#upcoming_events")+1]
        upcoming_events=text
        print(text)
        text=words[words.index("#doubts")+1]
        doubts=text
        print(text)
        db()
    except:
        print("Sorry the word is not found.")
        print ("Hello World")