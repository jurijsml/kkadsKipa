import json

vardnica={'Vārds':'Jānis', 'Izglitība':'Vidēja','Vecums':20}

a=json.dumps(vardnica)

print(a)

print(json.dumps(["kivi", "citrons"]))





py_data = {
  "Name":"Anna",
  "Age":30,
  "Animals":True,
  "Kids":("Sinda", "Aldis"),
  "Cars":[
    {"Model":"Audi", "Year":2007},
    {"Model":"BMW", "Year":2008}
  ]
}

print(json.dumps(py_data, indent=2))

with open("jsondati.json", "w", encoding = "utf-8") as f:
  json.dump(py_data, f, indent=2, ensure_ascii=False)

with open("jsondati.json", "r", encoding = "utf-8") as f:
  json_dati = json.load(f)

print(len(json_dati))

print(json_dati.keys())
print(json_dati.values())

mekl_atslega = "Name"
ista_atslega = ""
for atslega in json_dati.keys():
  if atslega == mekl_atslega:
    ista_atslega=atslega
    print(json_dati[atslega])
  if ista_atslega != mekl_atslega:
   print(f"Izskatās, ka {mekl_atslega} nav sarakstā")


#Funkcijas argumenti - datnes nosaukums un atslēga
#Atvērt failu, nolasīs un atradīs atslēgas vērtību

def json_las(datnesNosaukums, atslega):
  with open(datnesNosaukums, "r", encoding = "utf-8") as f:
    json_dati = json.load(f)