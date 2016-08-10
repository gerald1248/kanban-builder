#!/usr/bin/env python

"""
Creates Markdown Kanban boards from Yaml input
"""

import os
import sys
import yaml
import glob
import re
import string
import doctest
import dpath.util

USAGE = """
Usage: python [relative/path/to/]kanban_builder.py [input.yml]

Arguments:
--help/-h: display this text 

Build:
$ virtualenv ve
$ pip install pybuilder
$ pybuilder install_dependencies
$ pyb
"""

def parse_dict(obj):
  md = ''
  if obj == {} or isinstance(obj, list):
    return md

  if 'columns' not in obj:
    return md

  columns = dpath.util.get(obj, '/columns')

  headers = []
  arrays = []
  max_string_lengths = []

  for column in columns:
    key = column.keys()[0]
    headers.append(key) #headers
    arr = column[key]
    arrays.append(arr) #arrays
    max_string_length = len(key) + 4; #leave room for bold markers
    for s in arr:
      length = len(s)
      if length > max_string_length:
        max_string_length = length
    max_string_lengths.append(max_string_length) #max_string_lengths

  max_array_length = 0
  for index in range(len(arrays)):
    length = len(arrays[index])
    if length > max_array_length:
      max_array_length = length

  #write headers
  l1 = l2 = ''
  for index in range(len(headers)):
    header = '**' + escape_string(headers[index]) + '**'
    l1 += '|'
    l1 += pad_string(header, max_string_lengths[index])
    l1 += ''
    l2 += '|'
    l2 += pad_string(':', max_string_lengths[index], '-')
  l1 += '|\n'
  l2 += '|\n'
  md += l1
  md += l2

  column_count = len(headers)

  #write table rows and cells
  for row_index in range(max_array_length):
    for col_index in range(column_count):
      cell = ''
      if len(arrays[col_index]) > row_index:
        cell = escape_string(arrays[col_index][row_index])
      md += '|'
      md += pad_string(cell, max_string_lengths[col_index])
    md += '|\n'

  return md

def pad_string(s, length, char=' '):
  while len(s) < length:
    s += char
  return s

def escape_string(s):
  #TODO: what else would cause errors?
  return string.replace(s, '|', ' ')

def read_yaml(path): # pragma: no cover
  try:
    yaml_buffer = open(path)
    obj = yaml.safe_load(yaml_buffer)
    yaml_buffer.close()
  except IOError as ex:
    print "Can't open {}: {}".format(path, ex.strerror)
    sys.exit(1)
  except yaml.parser.ParserError as ex:
    print "Can't parse YAML file {}: {}".format(path, ex)
    sys.exit(2)
  return obj

if __name__ == "__main__": # pragma: no cover
  path = ''
  # don't run if help requested
  if len(sys.argv) > 1:
    for arg in sys.argv:
      if arg == "--help" or arg == "-h":
        print USAGE
        sys.exit(0)
      else:
        path = arg
  else:
    print USAGE
    sys.exit(0)

  obj = read_yaml(path)
  md = parse_dict(obj)

  print md
  sys.exit(0)
