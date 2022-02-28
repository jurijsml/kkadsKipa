from flask import Flask
import json

app = Flask(__name__)
app.config([JSON_AS_ASCII]) = False

@app.route("/")
def hello():
  return "Sveika, Pasaule!"

@app.route("/datums")
def datums():
  return "Šodien ir 15.februāris"

@app.route("/lietotajs/<vards>/<vecums>")
def lietotajs(vards,vecums):

  with open("dati/lietotaji.json", "w", encoding = "utf-8") as f:
    json_data = json.load(f)

    for key in json.data.key():
      if key == vards:
        break
      if key != vards:
        json_data[vards] = vecums
    return f"{vards} ir sarakstā."
     
  with open("dati/lietotaji.json", "w", encoding = "utf-8") as f:
    json.dump(jaunsIeraksts,f,indent=2,ensure_ascii=False)
    
  return json_data
  
app.run(host = "0.0.0.0", port=8080)