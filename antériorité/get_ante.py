import json
def json_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return None
    except json.JSONDecodeError:
        print("Le fichier spécifié n'est pas un fichier JSON valide.")
        return None

def dict_to_json(json_dict, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(json_dict, file, indent=4)
            print(f"Le dictionnaire a été écrit avec succès dans '{file_path}'.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture du fichier JSON : {e}")

def add_to_dict(json_dict, key,value):
    json_dict[key].append(value)


file_path = 'data.json'
json_dict = json_to_dict(file_path)



if json_dict:
    dict_to_json(json_dict, file_path)
