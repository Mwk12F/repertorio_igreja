from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.join(app.root_path, "static", "pdfs")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/")
def index():
    if not os.path.exists(BASE_DIR):
        return "Pasta pdfs não encontrada!"
        
    momentos = [p for p in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, p))]
    return render_template("index.html", momentos=momentos)

@app.route("/momento/<nome>")
def momento(nome):
    pasta = os.path.join(BASE_DIR, nome)
    
    if not os.path.exists(pasta):
        return "Momento não encontrado!"
    
    arquivos = os.listdir(pasta)
    return render_template("momento.html", nome=nome, arquivos=arquivos)

@app.route("/pdf/<momento>/<arquivo>")
def pdf(momento, arquivo):
    return send_from_directory(os.path.join(BASE_DIR, momento), arquivo)

if __name__ == "__main__":
    app.run(debug=True)