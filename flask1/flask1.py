from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
  return "Sveika, Pasaule!"

@app.route("/datums")
def datums():
  return "Šodien ir 15.februāris"

@app.route("/lietotajs/<vards>")
def lietotajs(vards):
  jaunsIeraksts = {"vards":vards}

  with open("dati/lietotaji.json", "w") as f:
    f.write(json.)

app.run(host = "0.0.0.0", port=8080)