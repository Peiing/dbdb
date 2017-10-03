
from __future__ import print_function
import sys
from __init__ import connect

'''
defines a command-line tool for exploring a database from a terminal window.
$ python -m dbdb.tool example.db get foo
'''

OK = 0
BAD_ARGS = 1
BAD_VERB = 2
BAD_KEY = 3

def usage():
    print("Usage:", file=sys.stderr)
    print("\tpython tool.py DBNAME get KEY", file=sys.stderr)
    print("\tpython tool.py DBNAME set KEY VALUE", file=sys.stderr)
    print("\tpython tool.py DBNAME delete KEY", file=sys.stderr)

def main(argv):
    if not (4 <= len(argv) <= 5):
        usage()
        return BAD_ARGS
    dbname, verb, key, value = (argv[1:] + [None])[:4]
    if verb not in {'get', 'set', 'delete','len'}:
        usage()
        return BAD_VERB
    db = connect(dbname)          # CONNECT
    try:
        if verb == 'get':
            sys.stdout.write(db[key])  # GET VALUE
        elif verb == 'set':
            db[key] = value
            db.commit()
        elif verb=='delete':
            del db[key]
            db.commit()
        elif verb=='len':
            print(len(db))
    except KeyError:
        print("Key not found", file=sys.stderr)
        return BAD_KEY
    return OK

class MyDB(object):

    def __init__(self,dbname):
        self._db=connect(dbname)

    def get(self,key):
        print(key,'=>', self._db[key])
        return self._db[key]

    def set(self,key,value):
        self._db[key]=value
        self._db.commit()

    def delete(self,key):
        del self._db[key]
        self._db.commit()

    
if __name__ == '__main__':
    sys.exit(main(sys.argv))