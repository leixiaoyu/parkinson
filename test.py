import sys
from pprint import pprint as p

p(sys.path)

# import os, sys, inspect
#  # realpath() with make your script run, even if you symlink it :)
# cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
# if cmd_folder not in sys.path:
#     sys.path.insert(0, cmd_folder)

#  # use this if you want to include modules from a subforder
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "packages")))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)
