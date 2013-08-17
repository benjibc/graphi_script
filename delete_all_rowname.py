from connector import Connector
import solr, sys
s = solr.SolrConnection('http://localhost:8983/solr')

class Deleter(Connector):
    def __init__(self):
        Connector.__init__(self)
        sys.stderr.write('Deleter initialized\n')

    def delete_solr(self):
        s.delete_many(range(100000000,100010000))
        s.commit()

    def delete_mysql(self):
        self.cursor.execute("""
            truncate row_name 
        """)
        self.cursor.execute("""
            truncate entity_to_table_id 
        """)
        self.cursor.execute("""
            truncate table_id_to_entity 
        """)
        self.cursor.execute("""
            ALTER TABLE row_name AUTO_INCREMENT = 100000000
        """)

def main():
    d = Deleter()
    d.delete_solr()
    d.delete_mysql()


if __name__ == "__main__":
    main()
