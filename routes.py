import json


def hello_world():  # put application's code here
    return 'Hello World!'


def sample_json():
    f = open("data/201.json")
    return json.load(f)

def load_json(line_id):
    file = line_id + ".json"
    f = open(f"data/{file}")
    return json.load(f)