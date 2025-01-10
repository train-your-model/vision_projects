import json
import dir_paths as dp

def check_newuser_presence(emp_id:str):
    json_file_path = dp.record_json_path
    with open(json_file_path) as rec:
        data = json.load(rec)
        if id in data.keys():
            return False
        else:
            return True