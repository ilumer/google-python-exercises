# coding:utf-8
#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def sort_by_alphabetical(tuple_name):
  return tuple_name[0]

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  result = {};
  with open(filename) as f:
    text_content = f.read()
    #year = re.search(r'<h3.*?>([\w\s]+?)(\d+)',text_content).group(2)
    #2008 并没有使用<h3>标签
    year = re.search(r'Popularity in (\d+)',text_content).group(1)
    body_name_rank = re.findall(r'<td>(.+)</td><td>(.+)</td><td>(.+)</td>',text_content)
    for item in body_name_rank:
      #考虑有名字重合的情况
      #if item[1] not in result.keys():
      #  result[item[1]] = item[0]
      #else
      # value = result[item[1]]
      # result[item[1]] = value if value < item[0] else item[0] 
      result[item[1]] = item[0]
      result[item[2]] = item[0]
  name_list = [x+' '+y for x,y in result.items()]
  name_list = sorted(name_list)
  name_list.insert(0,year)
  #print(name_list)
  return name_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  for arg in args:
    #写入文本中
    if summary:
      with open(arg+'.summary','w') as f:
        f.write('\n'.join(extract_names(arg)))
    else:
      for  x in extract_names(arg):
        print x
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':  
  main()
