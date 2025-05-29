import hashlib

class Block():
    def __intit__(self, data):
        self.hash = hashlib.sha256()
        self.nonce = 0
        self.data = data 

    def mine(self, difficulty):
        hash.update(str(self).encode('utf-8'))
        while int(hash.hexdigest(), 16)

    def __str__(self):
        return "{}{}".format(self.data, self.nonce)
    