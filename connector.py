import MySQLdb, MySQLdb.cursors
import config

class Connector:
    def __init__(self):
        self.db=MySQLdb.connect(user=config.user, passwd=config.password,
            db=config.db, cursorclass=MySQLdb.cursors.SSCursor)
        self.cursor = self.db.cursor()
        self.db2=MySQLdb.connect(user=config.user, passwd=config.password,
            db=config.db)
        self.cursor2 = self.db2.cursor()
