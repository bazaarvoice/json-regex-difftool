import os
import unittest

class TestHelper(unittest.TestCase):

    def write_string_to_file(self, string, filename, directory=None):
        root_directory = 'tmp/' + directory if directory is not None else 'tmp/'
        if directory is not None and not os.path.exists(root_directory):
            os.mkdir(root_directory)
        f = open(root_directory+str(filename), 'w')
        f.write(str(string))
        f.close()
        return root_directory+str(filename)

    def cleanup(self):
        self.cleanup_directory('tmp')

    def cleanup_directory(self, path):
        if not os.path.isdir(path):
            return
        for file in os.listdir(path):
            if not os.path.isdir(path+'/'+file):
                os.remove(path+'/'+file)
            else:
                self.cleanup_directory(path+'/'+file)
                os.rmdir(path+'/'+file)

