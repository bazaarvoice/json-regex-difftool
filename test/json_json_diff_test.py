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

    def test_list_addition_to_end(self):
        """
        When we add an item to the front of a list we should get an
        appropriate string in the diff telling us what was added
        """
        new_file = self.write_string_to_file('["test1", "test2"]', "item1")
        old_file = self.write_string_to_file('["test1"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=False),
                         [u'+: [1] - test2'])
        self.cleanup()

    def test_list_addition_to_front(self):
        """
        When we add an item to the end of a list we should get an
        appropriate string in the diff telling us what was added
        """
        new_file = self.write_string_to_file('["test2", "test1"]', "item1")
        old_file = self.write_string_to_file('["test1"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=False),
                         [u'+: [0] - test2'])
        self.cleanup()

    def test_list_subtraction_from_front(self):
        """
        When we add an item to the end of a list we should get an
        appropriate string in the diff telling us what was added
        """
        new_file = self.write_string_to_file('["test2"]', "item1")
        old_file = self.write_string_to_file('["test1", "test2"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=False),
                         [u'-: [0] - test1'])
        self.cleanup()

    def test_list_subtraction_from_end(self):
        """
        When we add an item to the end of a list we should get an
        appropriate string in the diff telling us what was added
        """
        new_file = self.write_string_to_file('["test2"]', "item1")
        old_file = self.write_string_to_file('["test2", "test1"]', "item2")
        comparison_tool = JSON_Diff(new_file, old_file)
        self.assertEqual(comparison_tool.diff(useModel=False),
                         [u'-: [1] - test1'])
        self.cleanup()