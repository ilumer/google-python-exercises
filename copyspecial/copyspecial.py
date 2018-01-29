# coding:utf-8
#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import commands　The commands module has been removed in Python 3. Use the subprocess module instead.
import subprocess
"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  filenames = os.listdir(dir)
  special_files = [] 
  for filename in filenames:
    if re.match(r'[\w]+_+?[\w]+_(.)+',filename):
      special_files.append(os.path.abspath(os.path.join(dir,filename)))
  return special_files

def copy_to(paths, dir):
  if not os.path.exists(dir):
    #os.mkdir(dir)
    os.makedirs(dir)
    # mkdir -p　如何实现　https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python/600612#600612
  for path in paths:
    basename = os.path.basename(path)
    shutil.copy(path,os.path.join(dir,basename))
    

def zip_to(paths, zippath):
  command = "Command I'm going to do：zip -j "+ zippath;
  command = command +" ".join(paths)
  print command
  paths.insert(0,'zip')
  paths.insert(1,'-j')
  paths.insert(2,zippath)
  #https://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7 修改call的重定向的位置
  #with open('output','w+') as redict:
  #  status = subprocess.call(paths,stdout=redict)
  #  if status != 0:
  #    with open('output','r') as f:
  #      print f.read()
  # 很蠢的修改输出方式
  #subprocess.call(paths)
  #sys.stdout.flush()
  subprocess.call(paths)
  #　好像可以修改输出信息https://fredrikaverpil.github.io/2013/10/11/catching-string-from-stdout-with-python/

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
  
  #剩下的是目标文件夹
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  if todir:
    copy_to(get_special_paths(args[0]),todir)

  if tozip:
    zip_to(get_special_paths(args[0]),tozip)  
  #if todir is not None:
  #  copy_to(paths,todir)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
