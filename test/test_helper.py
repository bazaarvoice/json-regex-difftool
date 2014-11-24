import os
import unittest


class TestHelper(unittest.TestCase):

    def make_tmp_directory(self):
        if not os.path.exists('tmp/'):
            os.mkdir('tmp/')

    def write_string_to_file(self, string, filename):
        self.make_tmp_directory()
        f = open('tmp/' + str(filename), 'w')
        f.write(str(string))
        f.close()
        return 'tmp/' + str(filename)

    def write_files_to_directory(self, filename_to_string, sub_directory):
        self.make_tmp_directory()
        for filename, string in filename_to_string.iteritems():
            if not os.path.exists('tmp/' + sub_directory):
                os.mkdir('tmp/' + sub_directory)
            f = open('tmp/' + sub_directory + '/' + filename, 'w')
            f.write(str(string))
            f.close()
        return 'tmp/' + sub_directory

    def cleanup(self):
        self.cleanup_directory('tmp')

    def cleanup_directory(self, path):
        if not os.path.isdir(path):
            return
        for filename in os.listdir(path):
            if not os.path.isdir(path+'/'+filename):
                os.remove(path+'/'+filename)
            else:
                self.cleanup_directory(path+'/'+filename)
                os.rmdir(path+'/'+filename)

