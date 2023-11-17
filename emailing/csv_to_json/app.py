import uuid
import json
import csv
import pathlib

ROOT = pathlib.Path(__file__).parent.parent.parent

print(ROOT)
path_source = ROOT / 'emailing' / 'csv_to_json' /'liste-recruteurs.csv'

output = []
with open(path_source, 'r') as resource:
    for row in csv.DictReader(resource):
        row['id'] = str(uuid.uuid4()).replace('-', '')[:13]
        output.append(row)

export_file = 'data_recruteurs.json'
export = [
    ROOT / 'emailing' / 'src' / 'data' / export_file,
    ROOT / 'frontoffice' / 'services' / 'src' / 'model' / 'data' / export_file
]
for path in export:
    with open(path, "w") as f:
        f.write(json.dumps(output))
        print('done >> ', path)

