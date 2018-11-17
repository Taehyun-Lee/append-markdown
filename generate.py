import argparse
import os
import binascii
from os import listdir, urandom
from os.path import isfile, join, isdir, abspath

# Parser Construction
parser = argparse.ArgumentParser(
  prog = "append-markdown",
  description = """\
  Reads through specified files and picks out formatted \
  components, and outputs them according to the output formatter\
  supplied\
  """,
)

parser.add_argument(
  "-i", "--inputs",
  nargs = "+",
  type = str,
  help = "Input files and directories (must supply at least one)"
)

parser.add_argument(
  "-t", "--types",
  nargs = "+",
  type = str,
  help = "File types to parse"
)

parser.add_argument(
  "-r", "--recurse",
  action = "store_true",
  help = "Determines whether or not the files are searched recursively or not"
)

parser.add_argument(
  "-o", "--outform",
  nargs = 1,
  #required = True,
  help = "The output format file"
)

# Get all files
def get_file_from_dir(dir):
  return [join(dir, f) for f in listdir(dir)]


def get_random_hash():
  return binascii.hexlify(urandom(8)).decode("utf-8")


def grab_formats(file, formats):
  file_formats = {}
  with open(file) as f:
    for line in f:
      for word in line.split(" "):
        shouldAdd = False

        if(word.startswith("@!") 
           and not(word[2:] in file_formats or word[2:-1] in file_formats)):
          format_word = ""
          if (word.endswith("\n")):
            format_word = word[2:-1]
          else:
            format_word = word[2:]

          # new format_word
          if (not format_word in formats):
            formats[format_word] = []

          file_formats[format_word] = [get_random_hash(), []]
          
        elif(word.startswith("@?") 
             and (word[2:] in file_formats or word[2:-1] in file_formats )):
          format_word = ""
          if (word.endswith("\n")):
            format_word = word[2:-1]
          else:
            format_word = word[2:]
          
          formats[format_word].append(
            file_formats.pop(format_word, None)
          )
        else:
          shouldAdd = True
        
        if (shouldAdd):
          for file_format in file_formats.values():
            file_format[1].append(word)
  
  if (len(file_formats.keys())):
    print("The following format labels were not completed:")
    print(", ".join(file_formats.keys()))
    print("""\
    Please close them by adding @?<label>\
    """)

# Parse user input
def parse_user_input_and_get_format():
  user_input = parser.parse_args()
  user_input = vars(user_input)

  all_files = []
  check = [abspath(path) for path in user_input["inputs"]]

  for path in check:
    if (isfile(path)):
      for file_type in user_input["types"]:
        if(path.endswith(file_type)):
          all_files.append(path)
          break
    elif (isdir(path) and user_input["recurse"]):
      check.extend(get_file_from_dir(path))
    else:
      print(f"{path} is not a file nor a directory")
  
  # Initializing output dictionary
  formats = {}
  
  for file in all_files:
    grab_formats(file, formats)

  print(formats)


if (__name__) == "__main__":
  parse_user_input_and_get_format()
