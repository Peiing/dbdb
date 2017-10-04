
import datetime
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
    print("Usage:")
    print("> get KEY")
    print("> set KEY VALUE")
    print("> del KEY")
    print("> len")


def main(argv):
    if not (4 <= len(argv) <= 5):
        usage()
        return BAD_ARGS
    dbname, verb, key, value = (argv[1:] + [None])[:4]
    if verb not in {'get', 'set', 'delete', 'len'}:
        usage()
        return BAD_VERB
    db = connect(dbname)          # CONNECT
    try:
        if verb == 'get':
            sys.stdout.write(db[key])  # GET VALUE
        elif verb == 'set':
            db[key] = value
            db.commit()
        elif verb == 'delete':
            del db[key]
            db.commit()
        elif verb == 'len':
            print(len(db))
    except KeyError:
        print("Key not found", file=sys.stderr)
        return BAD_KEY
    return OK


def cmd_main():

    print('DBDB version 1.0.0',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('Enter "help" for usage hints.')
    print('Use "open> FILENAME" to reopen on a persistent database.')

    db=None
    while db==None:
        filename = input('open> ')
        if filename!=None:
            db = connect(filename)
        else:
            pass

    while True:
        cmd = input('dbdb> ')
        cmd = cmd.split()
        if len(cmd)<=1:
            verb=cmd[0]
            if verb not in {'len', 'exit', 'help','max'}:
                usage()
            elif verb=='help':
                usage()
            elif verb=='len':
                print(len(db))
            elif verb=='max':
                print(db.find_max())
            elif verb=='exit':
                return
            else:
                pass
            continue               

        verb, key, value = (cmd + [None])[:3]
        try:
            if verb == 'get' and key != None and value == None:
                print(db[key])
            elif verb == 'set' and key != None and value != None:
                db[key] = value
                db.commit()
            elif verb == 'del' and key != None and value == None:
                del db[key]
                db.commit()
            else:
                usage()
        except KeyError:
            print("Key not found")


if __name__ == '__main__':
    cmd_main()
    