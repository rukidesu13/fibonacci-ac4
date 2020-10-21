import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
   prox = 1
   ant = 0
   limite = 50
   found = 0
   resposta = "0 ,"

   while (found < limite):
       temp = prox
       prox = prox + ant
       ant = temp
       found = found + 1
       resposta += str(prox) + ", " + "<br/>"


   return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
