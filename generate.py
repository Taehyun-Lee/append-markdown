import argparse
from os import listdir
from os.path import isfile, join, isdir, abspath

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

user_input = parser.parse_args()
user_input = vars(user_input)

def get_file_from_dir(dir):
  return [join(dir, f) for f in listdir(dir)]

dir_present = False
all_files = []
check = [abspath(path) for path in user_input["inputs"]]


for path in check:
  if (isfile(path)):
    all_files.append(path)
  elif (isdir(path) and user_input["recurse"]):
    check.extend(get_file_from_dir(path))
  else:
    print(f"{path} is not a file nor a directory")

formats = {}

def grab_formats(file, format):
  file_formats = {}
  with open(file) as f:
    for line in f:
      for word in line.split(" "):
        if(word.startswith("@!") 
           and not(word[2:] in file_formats or word[2:-1] in file_formats)):
          format_word = ""
          if (word.endswith("\n")):
            format_word = word[2:-1]
          else:
            format_word = word[2:]

          # new format_word
          if (not format_word in formats):
            formats[format_word] = [0, []]

          file_formats[format_word] = [formats[format_word][0], []]
          formats[format_word][0] += 1
          
          
        elif(word.startswith("@?") 
             and (word[2:] in file_formats or word[2:-1] in file_formats )):
          format_word = ""
          if (word.endswith("\n")):
            format_word = word[2:-1]
          else:
            format_word = word[2:]
          
          file_formats[format_word][1].pop(0)
          
          formats[format_word][1].append(
            file_formats.pop(format_word, None)
          )
        
        for file_format in file_formats.values():
          file_format[1].append(word)
  
  if (len(file_formats.keys())):
    print("The following format labels were not completed:")
    print(", ".join(file_formats.keys()))
    print("""\
    Please close them by adding @?<label>\
    """)



          
for file in all_files:
  grab_formats(file, formats)

print(formats)

