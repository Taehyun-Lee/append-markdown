from os.path import abspath
from parser import parser
from handle_input import grab_formats
from handle_files import get_all_files
from handle_output import output

# Parse user input
def parse_user_input_and_get_format():
  user_input = parser.parse_args()
  user_input = vars(user_input)

  check = [abspath(path) for path in user_input["inputs"]]
  all_files = get_all_files(check, user_input["types"], user_input["recurse"])
  
  # Initializing output dictionary
  formats = {}
  for file in all_files:
    grab_formats(file, formats)

  # Output based on --outform
  print (output[user_input["outtype"]](formats = formats, output_format = user_input["outform"]))

if (__name__) == "__main__":
  parse_user_input_and_get_format()