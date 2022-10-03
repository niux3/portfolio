data = [
    "sacla",
    "cavadeos",
    "banquecasino",
    "peugeot 4008",
    "mypeugeot",
    "decolorstop",
    "qui est le moins cher",
    "michel edouard leclerc",
    "fidelity vie",
    "algeco",
    "cfcopies",
    "air Madagascar",
    "air caraïbes",
    "europcar",
    "flyopenskies",
    "areva",
    "leroy merlin",
    "peugeot",
    "peugeot design lab",
    "dyson affaire aireblade",
    "brasserie flo",
    "bazarchic",
    "mytravelchic",
    "afflelou",
    "adp",
    "atelier Renault",
    "le siège renault",
    "Renault kadjarquest",
    "Renault clio RS Melody",
    "upsa",
    "system dacia",
    "serie toplexil",
    "honda moto",
    "rene furterer",
    "cevital",
    "longchamp",
    "rimowa",
    "carenity",
    "le point",
    "palmares le point",
    "radio france",
    "john paul",
]
colors = [
    "#1abc9c",
    "#2ecc71",
    "#3498db",
    "#9b59b6",
    "#34495e",
    "#e67e22",
    "#e74c3c",
    "#95a5a6",
]

output = ""
for i, row in enumerate(data):
    output += '#work nav ul li:nth-child(' + str(i + 1) + '):before{background-color:' + str(colors[i % len(colors)]) + ';}'

with open('./public/color-slide.css', 'w') as f:
    f.write(output)

print('done !')