import unittest2 as unittest
from list_methods import find_elem, find_elem_by, filter_list, max_elem, max_elem_by, sort_strings

class TestStringFunctions(unittest.TestCase):

    def test_find_elem(self):
        list_of_strings = ["Terrance", "Julia", "Python"]
        self.assertEqual(find_elem(list_of_strings, "Python"), "Python")
        self.assertEqual(find_elem(list_of_strings, "JavaScript"), "")

    def test_find_elem_by(self):
        list_of_dictionaries = [{'name': "Terrance", 'age': 25}, {'name': "Fred", 'age': 35}, {'name': "Anna", 'age': 30}]
        self.assertEqual(find_elem_by(list_of_dictionaries, 'age', 30), {'name': "Anna", 'age': 30})
        self.assertEqual(find_elem_by(list_of_dictionaries, 'age', 20), {})

    def test_filter_list(self):
        #callback_function
        def name_starts_with_t(name):
            return name.lower().startswith('t')
        list_of_strings = ["Terrance", "Julia", "Python"]
        self.assertItemsEqual(filter_list(list_of_strings, name_starts_with_t), ['Terrance'])

    def test_max_elem(self):
        list_of_numbers = [1,4,7,3,10,30,-50]
        self.assertEqual(max_elem(list_of_numbers), 30)

    def test_max_elem_by(self):
        list_of_dictionaries = [{'name': "Terrance", 'age': 25}, {'name': "Fred", 'age': 35}, {'name': "Anna", 'age': 30}]
        self.assertEqual(max_elem_by(list_of_dictionaries, 'age'), {'name': "Fred", 'age': 35})

    def test_sort_strings(self):
        list_of_strings = ["Terrance", "Julia", "Python", "Apple", "Dave"]
        self.assertItemsEqual(sort_strings(list_of_strings), ["Apple", "Dave", "Julia", "Python", "Terrance"])
