import argparse
import binascii
import json
import os
from os import listdir, urandom
from os.path import isfile, join, isdir, abspath
import shutil

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
  default = "",
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
  choices = ["json"],
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
  temp = open("temp", "w")
  with open(file, "r") as f:
    for line in f:
      line_for_temp = line.split(" ")

      for ind, word in enumerate(line_for_temp):
        shouldAdd = False
        format_word = ""
        format_hash = ""

        if(word.startswith("@!") or word.startswith("@?")):
          if (len(word.split("-")) > 1):
            format_word = word.split("-")[0][2:]
          elif (word.endswith("\n")):
            format_word = word[2:-1]
          else:
            format_word = word[2:]
          
          if(len(word.split("-")) == 1):
            if(word.startswith("@!")):
              format_hash = get_random_hash()
            else:
              format_hash = file_formats[format_word][0]
            nl = "\n"
            line_for_temp[ind] = f"{word[0:2]}{format_word}-{format_hash}{nl if word.endswith(nl) else ''}"
          else:
            format_hash = word.split("-")[1]

          if(word.startswith("@!")):
            # new format_word
            if (not format_word in formats):
              formats[format_word] = []

            file_formats[format_word] = [format_hash, []]
          else:
            formats[format_word].append(
              file_formats.pop(format_word, None)
            )
        else:
          shouldAdd = True
        
        if (shouldAdd):
          for file_format in file_formats.values():
            file_format[1].append(word)

      temp.write(" ".join(line_for_temp))

  temp.close()
  shutil.move('temp', file)

  if (len(file_formats.keys())):
    print("The following format labels were not completed:")
    print(", ".join(file_formats.keys()))
    print("""\
    Please close them by adding @?<label>\
    """)

# Takes in a dictionary and outputs in json format
def output_json(format):
  json_out = {}
  json_out["definitions"] = []

  for definition in format:
    def_id = definition.split("-")

    json_def = {
      "id" : def_id[-1],
      "textdata": []
    }

    for string in format[definition][-1][0][-1]:
      json_def["textdata"].append({
        "string": string
      })

    json_out["definitions"].append(json_def)
  return json.dumps(json_out, indent=2)

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

  # Output based on --outform
  if(user_input["outform"] and user_input["outform"][0] == 'json'):
    print(output_json(formats))
  else:
    print(formats)

if (__name__) == "__main__":
  parse_user_input_and_get_format()