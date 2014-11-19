import os
import unittest

class TestHelper(unittest.TestCase):

    def write_string_to_file(self, string, filename):
        f = open('tmp/'+str(filename), 'w')
        f.write(str(string))
        f.close()
        return 'tmp/'+str(filename)

    def cleanup(self):
        for file in os.listdir('tmp/'):
            os.remove('tmp/'+file)

