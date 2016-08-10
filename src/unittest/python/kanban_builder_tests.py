import unittest

from kanban_builder import parse_dict
from kanban_builder import pad_string
from kanban_builder import escape_string

class ParseDictTest(unittest.TestCase):
  def test_parse_dict(self):
    self.assertEqual(
        parse_dict({'columns': [ { 'header1': [ 'a', 'b' ] }, { 'header2': [ 'c', 'd'] } ] }),
        '|**header1**|**header2**|\n|:----------|:----------|\n|a          |c          |\n|b          |d          |\n'
    )

class PadStringTest(unittest.TestCase):
  def test_pad_string(self):
    self.assertEqual(
        pad_string('foo', 5, '='),
        'foo=='
    )

class EscapeStringTest(unittest.TestCase):
  def test_escape_string(self):
    self.assertEqual(
        escape_string('a|b|c'),
        'a b c'
    )
