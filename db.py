
import sqlite3


class DB:
    def __init__(self, dbname="details.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS INFO(hire text, new_technology text, good_conversations text, upcoming_events text, doubts text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, hire, new_technology, good_conversations, upcoming_events, doubts,):
        stmt = "INSERT INTO INFO (hire, new_technology, good_conversations, upcoming_events, doubts) VALUES (?, ?, ?, ?, ?)"
        args = (hire, new_technology, good_conversations, upcoming_events, doubts)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM items WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        stmt = "SELECT hire, new_technology, good_conversations, upcoming_events, doubts FROM INFO"
        return [x for x in self.conn.execute(stmt)]
