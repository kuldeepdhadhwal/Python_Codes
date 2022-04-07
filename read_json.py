# reading json file and storing names in dict
def read_json(path):
    import json
    result = {}
    f = open(path)
    data = json.load(f)
    for line in data["process"]:
        print(line)
        if "name" in result:
            result["name"].append(line["name"])
        else:
            result["name"] = [line["name"]]        
    return result

output = read_json('/home/x/Documents/Template.json')
