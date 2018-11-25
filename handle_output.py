import json
from os.path import abspath

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
  print(json.dumps(json_out, indent=2))


def output_general(formats, output_format):
  output_file = abspath(output_format["path"])
  with open(output_file, 'w') as out_file:
    out_file.write(output_format["prolog"] + "\n\n\n")

    for content in output_format["contents"]:
      out_file.write(content["prolog"] + "\n\n\n")
      if(content["format"] in formats):
        for format_str in formats:
          out_file.write(content["divider"] + "\n\n")
          comment_format = output_format["comment_format"]
          format_name = content["format"], 
          format_hash = formats[0]
          changed_comment = comment_format.replace("@!content!@", format_name + "-" + format_hash)
          if( not (comment_format == changed_comment)): 
            out_file.write(changed_comment + "\n")
          out_file.write((" ").join(format_str[1]) + "\n")
          if( not (comment_format == changed_comment)): 
            out_file.write(changed_comment + "\n\n")
      
      out_file.write(content["epilog"] + "\n\n")
    
    out_file.write(output_file["epilog"])


output = {
  "json" : lambda formats, output_format : output_json(formats),
  None   : lambda formats, output_format : output_general  (formats, output_format)
}