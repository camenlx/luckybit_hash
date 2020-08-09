import luckybit_hash
from binascii import unhexlify, hexlify

import unittest

# luckybit block #1
# user@b1:~/luckybit$ luckybit-cli getblockhash 1
# 0000052a5b7da4002bb7fdf7ec6443d6c0781d2d952b4780b1fa29859b8d43c7
# user@b1:~/luckybit$ luckybit-cli getblock 0000052a5b7da4002bb7fdf7ec6443d6c0781d2d952b4780b1fa29859b8d43c7
#{ LUCKY
#  "hash": "0000052a5b7da4002bb7fdf7ec6443d6c0781d2d952b4780b1fa29859b8d43c7",
#  "confirmations": 363172,
#  "size": 179,
#  "height": 1,
#  "version": 536870912,
#  "merkleroot": "324ab01a64503d1b7d36857eb386d327510b621ef8c16421ec4149bf3d2645e9",
#  "tx": [
#    "324ab01a64503d1b7d36857eb386d327510b621ef8c16421ec4149bf3d2645e9"
#  ],
#  "time": 1518828899,
#  "mediantime": 1518828899,
#  "nonce": 509006,
#  "bits": "1e0ffff0",
#  "difficulty": 0.000244140625,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#  "previousblockhash": "00000ce77a49057b7b44075e9ae575451aa726d89759398febcfeb7a7460e73c",
#  "nextblockhash": "0000092a559c289e49105ea865022c772aa9376960d9bf399748fc4f2382417b"
#}

header_hex = ("00000020" + # version
    "3ce760747aebcfeb8f395997d826a71a4575e59a5e07447b7b05497ae70c0000" + # reverse-hex previousblockhash
    "e945263dbf4941ec2164c1f81e620b5127d386b37e85367d1b3d50641ab04a32" + # reverse-hex merkleroot
    "637d875a" + # reverse-hex time
    "f0ff0f1e" + # reverse-hex bits
    "4ec40700")  # reverse-hex nonce

best_hash = 'c7438d9b8529fab180472b952d1d78c0d64364ecf7fdb72b00a47d5b2a050000' # reverse-hex block hash

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_luckybit_hash(self):
        self.pow_hash = hexlify(luckybit_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()
