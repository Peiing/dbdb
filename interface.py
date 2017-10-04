from physical import Storage
from binary_tree import BinaryTree

class DBDB(object):
    '''
    defines a class (DBDB) which implements the Python dictionary API using the concrete BinaryTree implementation. This is how you'd use DBDB inside a Python program.
    '''
    def __init__(self, f):
        self._storage = Storage(f)
        self._tree = BinaryTree(self._storage)

    def _assert_not_closed(self):
        if self._storage.closed:
            raise ValueError('Database closed.')

    def __getitem__(self, key):
        self._assert_not_closed()
        return self._tree.get(key)

    def __setitem__(self, key, value):
        self._assert_not_closed()
        return self._tree.set(key, value)

    def __delitem__(self, key):
        self._assert_not_closed()
        return self._tree.pop(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def close(self):
        self._storage.close()

    def commit(self):
        self._assert_not_closed()
        self._tree.commit()

    def __len__(self):
        return len(self._tree)

    def find_max(self):
        return self._tree.find_max()
        

