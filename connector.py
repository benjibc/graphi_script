import MySQLdb, MySQLdb.cursors

class Connector:
    def __init__(self):
        self.db=MySQLdb.connect(user="root", passwd="qwe110170",
            db="wikidb", cursorclass=MySQLdb.cursors.SSCursor)
        self.cursor = self.db.cursor()
        self.db2=MySQLdb.connect(user="root", passwd="qwe110170",
            db="wikidb")
        self.cursor2 = self.db2.cursor()
