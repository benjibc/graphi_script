from connector import Connector
import solr, sys
s = solr.SolrConnection('http://localhost:8983/solr')

class Deleter(Connector):
    def __init__(self):
        Connector.__init__(self)
        sys.stderr.write('Deleter initialized\n')

    def delete_solr(self):
        s.delete_many(range(0,5000))
        s.commit()

    def delete_mysql(self):
        self.cursor.execute("""
            truncate metadata 
        """)
        self.cursor.execute("""
            truncate entity_to_table_id 
        """)

def main():
    d = Deleter()
    d.delete_solr()
    d.delete_mysql()


if __name__ == "__main__":
    main()
