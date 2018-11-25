
from os import listdir
from os.path import isfile, join, isdir, abspath

# Get all files
def get_file_from_dir(dir):
  return [join(dir, f) for f in listdir(dir)]

def get_all_files(check_list, types, shouldRecurse):
  all_files = []
  for path in check_list:
    if (isfile(path)):
      file_type = path.split(".")[-1]
      if(types is None or file_type in types):
        all_files.append(path)
    elif (isdir(path) and shouldRecurse):
      check_list.extend(get_file_from_dir(path))
    else:
      print(f"{path} is not a file nor a directory")
  
  return all_files