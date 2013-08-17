from connector import Connector
import solr, sys
s = solr.SolrConnection('http://localhost:8983/solr')

class Deleter(Connector):
    def __init__(self):
        Connector.__init__(self)
        sys.stderr.write('Deleter initialized\n')

    def delete_solr(self):
        s.delete_many(range(0,2000))
        s.commit()

    def delete_mysql(self):
        pass

def main():
    d = Deleter()
    d.delete_solr()
    d.delete_mysql()


if __name__ == "__main__":
    main()
