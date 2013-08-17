import MySQLdb
import MySQLdb.cursors

import solr
s = solr.SolrConnection('http://localhost:8983/solr')

class Topics:
    def __init__(self):
        self.topics = []
        self.db=MySQLdb.connect(user="root", passwd="qwe110170", \
            db="wikidb", cursorclass=MySQLdb.cursors.SSCursor)
        self.cursor1 = self.db.cursor()

    def process(self):
        all_nodes = set()
        all_relations = []
        self.cursor1.execute("""select
            page_id, page_title
            FROM node
            JOIN page on node.id = page.page_id 
            WHERE page_id < 10000 
            """)
        row1 = self.cursor1.fetchone()
        counter = 0
        while row1 is not None:
            name_str = row1[1].decode('utf-8').replace('_', ' ')
            s.add(id=row1[0], name=name_str)
            counter+=1
            if counter % 10000 == 0:
                s.commit()
                print counter
            row1 = self.cursor1.fetchone()
        s.commit()
        self.cursor1.close()
        self.db.close()

def main():
    topics = Topics()
    topics.process()

if __name__ == "__main__":
        main()
