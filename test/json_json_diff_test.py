from test_helper import TestHelper
from json_diff import JSON_Diff


class JsonJsonDiffTest(TestHelper):

    def test_simple_no_difference(self):
        """
        With no difference we should have an empty list
        """
        new_file = self.write_string_to_file('["test"]', "item1")
        old_file = self.write_string_to_file('["test"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=False), [])
        self.cleanup()

    def test_simple_type_difference(self):
        """
        When the type changes we should get an appropriate message in the difference
        :return:
        """
        new_file = self.write_string_to_file('["test"]', "item1")
        old_file = self.write_string_to_file('{"key":"value"}', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=False),
                         ["TypeDifference :  - is list: ([u'test']), but was dict: ({u'key': u'value'})"])
        self.cleanup()