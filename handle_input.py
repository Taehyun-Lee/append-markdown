import binascii
import shutil
from os import urandom

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

        if(word.startswith("@!") or word.startswith("!@")):
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