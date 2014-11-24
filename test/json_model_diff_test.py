from test_helper import TestHelper
from json_diff import JSON_Diff


class JsonModelDiffTest(TestHelper):

    def test_simple_regex_no_difference(self):
        """
        With no difference we should have an empty list
        """
        new_file = self.write_string_to_file('["test"]', "item1")
        old_file = self.write_string_to_file('["(.*)"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=True), [])
        self.cleanup()

    def test_simple_regex_difference(self):
        """
        With no match we should show a list deletion then list addition.
        """
        new_file = self.write_string_to_file('["test"]', "item1")
        old_file = self.write_string_to_file('["[0-9]+"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=True), [u'+: [0]=test', u'-: [0]=[0-9]+'])
        self.cleanup()

    def test_ambiguous_regex(self):
        """
        With an ambiguous regex, we should match the first item in the list
        """
        new_file = self.write_string_to_file('["test1", "test2"]', "item1")
        old_file = self.write_string_to_file('["(.*)"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=True), [u'+: [1]=test2'])
        self.cleanup()

    def test_list_order_with_regex(self):
        """
        Regex matching should match the first item of the list, and then treat the rest as out of order
        """
        new_file = self.write_string_to_file('["test1", "test2"]', "item1")
        old_file = self.write_string_to_file('["test2", "(.*)"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=True), [u'+: [1]=test2', u'-: [0]=test2'])
        self.cleanup()

    def test_regex_integer_match(self):
        """
        Test to ensure that we can match integers even though their type is not text
        """
        new_file = self.write_string_to_file('[42]', "item1")
        old_file = self.write_string_to_file('["[0-9]+"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=True), [])
        self.cleanup()

    def test_regex_match_value(self):
        filename1 = self.write_string_to_file('{"key":"value"}', "item1")
        filename2 = self.write_string_to_file('{"key":"(.*)"}', "item2")
        comparison_tool = JSON_Diff(filename1, filename2)
        self.assertEqual(comparison_tool.diff(useModel=True), [])
        self.cleanup()

    def test_regex_for_map_type_difference(self):
        """
        Trying to match a regular expression with a dictionary should result in a type difference
        """
        filename1 = self.write_string_to_file('{"key1":{"key2":"value"}}', "item1")
        filename2 = self.write_string_to_file('{"key1":"(.*)"}', "item2")
        comparison_tool = JSON_Diff(filename1, filename2)
        self.assertEqual(comparison_tool.diff(useModel=True), [
            "TypeDifference : key1 - dict: ({u'key2': u'value'}), unicode: ((.*))"])
        self.cleanup()