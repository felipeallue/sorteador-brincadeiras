from flask import Flask, render_template, jsonify, Response
import random
import json

app = Flask(__name__)

def carregar_brincadeiras():
    with open("data/brincadeiras.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para sortear uma brincadeira
@app.route('/sortear')
def sortear_brincadeira():
    brincadeiras = carregar_brincadeiras()
    brincadeira = random.choice(brincadeiras)
    return Response(
        json.dumps(brincadeira, ensure_ascii=False),
        content_type='application/json; charset=utf-8'
    )

if __name__ == '__main__':
    app.run(debug=True)
