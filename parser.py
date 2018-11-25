import argparse

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
  nargs = "+",
  help = "A json file specifying the output format."
)

parser.add_argument(
  "-u", "--outtype",
  nargs = 1,
  default = "json",
  choices = ["json", "md"],
  #required = True,
  help = "The type of the output file"
)