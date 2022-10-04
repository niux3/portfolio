import os

files = os.listdir('./public/css')
output = ""
for file in files:
    output += f"<link rel='stylesheet' href='css/{file}'>"
print(output)