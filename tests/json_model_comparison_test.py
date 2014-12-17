from test.test_helper import TestHelper
from jsondiff import JsonDiff


class JsonModelComparisonTest(TestHelper):

    def test_single_item_equal(self):
        filename1 = self.write_string_to_file('["test"]', "item1")
        filename2 = self.write_string_to_file('["test"]', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_single_item_not_equal(self):
        filename1 = self.write_string_to_file('["test"]', "item1")
        filename2 = self.write_string_to_file('["different"]', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_single_item_regex_equal(self):
        filename1 = self.write_string_to_file('["test"]', "item1")
        filename2 = self.write_string_to_file('["(.*)"]', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_single_item_regex_not_equal(self):
        filename1 = self.write_string_to_file('["test"]', "item1")
        filename2 = self.write_string_to_file('["[0-9]+"]', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_regex_match_key(self):
        filename1 = self.write_string_to_file('{"key":"value"}', "item1")
        filename2 = self.write_string_to_file('{"(.*)":"value"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_regex_match_value(self):
        filename1 = self.write_string_to_file('{"key":"value"}', "item1")
        filename2 = self.write_string_to_file('{"key":"(.*)"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_regex_match_key_and_value(self):
        filename1 = self.write_string_to_file('{"key":"value"}', "item1")
        filename2 = self.write_string_to_file('{"(.*)":"(.*)"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_ambiguous_regex(self):
        """
        We cannot match ambigous regular expressions
        Todo create a recursive search to fix this problem
        """
        filename1 = self.write_string_to_file('{"key1":"value1",'
                                              '"key2":"value2"}', "item1")
        filename2 = self.write_string_to_file('{"(.*)":"value1", '
                                              '"(.*)":"value2"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_almost_ambiguous_regex(self):
        """
        This test demonstrates that crafting slightly more specific
        regular expressions can fix the ambiguity bug
        """
        filename1 = self.write_string_to_file('{"key1":"value1",'
                                              '"key2":"value2"}', "item1")
        filename2 = self.write_string_to_file('{"(.*)[1]+":"value1",'
                                              '"(.*)":"value2"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_list_order(self):
        """
        List order in a JSON document is deterministic.
        If there order is changed they should not match
        """
        filename1 = self.write_string_to_file('["test1", "test2"]', "item1")
        filename2 = self.write_string_to_file('["test2", "test1"]', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        # We cannot match ambigous regular expressions
        # Todo create a recursive search to fix this problem
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_list_order_with_regex(self):
        """
        List order in a JSON document is deterministic.
        If there order is changed they should not match
        Even when using a regex, these should not match
        """
        filename1 = self.write_string_to_file('["test1", "test2"]', "item1")
        filename2 = self.write_string_to_file('["test2", "(.*)"]', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_nested_regex_matching(self):
        """
        We cannot have a regular expression match a whole dictionary.
        """
        filename1 = self.write_string_to_file('{"key1": {"key2":"value2"}}',
                                              "item1")
        filename2 = self.write_string_to_file('{"key1":"(.*)"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_nested_regex_matching_on_key(self):
        """
        Keys still match with a regex if their nested values are equal
        """
        filename1 = self.write_string_to_file('{"key1": {"key2":"value2"}}',
                                              "item1")
        filename2 = self.write_string_to_file('{"(.*)": {"key2":"value2"}}',
                                              "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_multiple_nested_regex_matching(self):
        """
        Test nested regex matches can still be determined
        """
        filename1 = self.write_string_to_file('{"key1": {"key2":"value2",'
                                              '"key3":"value3"}}', "item1")
        filename2 = self.write_string_to_file('{"(.*)": {"key2":"(.*)",'
                                              '"(.*)":"value3"}}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_map_out_of_order(self):
        """
        We should still map map equivalencies with entries out of order
        """
        filename1 = self.write_string_to_file('{"key1":"value1",'
                                              '"key2":"value2"}', "item1")
        filename2 = self.write_string_to_file('{"key2":"value2",'
                                              '"key1":"value1"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_map_out_of_order_with_regex(self):
        """
        We should still map map equivalencies with entries out of order
        """
        filename1 = self.write_string_to_file('{"key1":"value1",'
                                              '"key2":"value2"}', "item1")
        filename2 = self.write_string_to_file('{"(.*)":"value2",'
                                              '"key1":"value1"}', "item2")
        comparison_tool = JsonDiff(filename1, filename2)
        self.assertTrue(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_find_match_in_directory(self):
        """
        A match in a directory should return the filename that it matched
        """
        filename = self.write_string_to_file('["test1"]', "item1")
        dirname = self.write_files_to_directory({
            "dir_item1": '["test1"]',
            "dir_item2": '["test2"]',
            "dir_item3": '["test3"]',
        }, "test")
        comparison_tool = JsonDiff(filename, dirname)
        self.assertEqual(comparison_tool.comparison(use_model=True),
                         "dir_item1")
        self.cleanup()

    def test_no_match_in_directory(self):
        """
        When there is no match in a directory, we should return False
        """
        filename = self.write_string_to_file('["test1"]', "item1")
        dirname = self.write_files_to_directory({
            "dir_item1": '["test4"]',
            "dir_item2": '["test2"]',
            "dir_item3": '["test3"]',
        }, "test")
        comparison_tool = JsonDiff(filename, dirname)
        self.assertFalse(comparison_tool.comparison(use_model=True))
        self.cleanup()

    def test_find_directory_match_regex(self):
        filename1 = self.write_string_to_file('["test1"]', "item1")
        dirname = self.write_files_to_directory({
            "dir_item1": '["(.*)"]',
            "dir_item2": '["test2"]',
            "dir_item3": '["test3"]',
        }, "test")
        comparison_tool = JsonDiff(filename1, dirname)
        self.assertEqual(comparison_tool.comparison(use_model=True),
                         "dir_item1")
        self.cleanup()