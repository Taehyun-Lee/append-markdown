import json

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


def output_general(formats, output_format):
  pass


output = {
  "json" : lambda formats, output_format : output_json(formats),
  None   : lambda formats, output_format : output_general  (formats, output_format)
}