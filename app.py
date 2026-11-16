from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__, static_folder="static", static_url_path="")
client = anthropic.Anthropic()  # klucz z ANTHROPIC_API_KEY

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    historia = request.json["messages"][-20:]  # ogranicza długość historii
    odp = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1000,
        system="Jesteś pomocnym asystentem. Odpowiadaj po polsku.",
        messages=historia,
    )
    return jsonify({"reply": odp.content[0].text})

if __name__ == "__main__":
    app.run(debug=True)