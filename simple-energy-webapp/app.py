from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>welcome to EVR 🚴‍♂️⚡</h1>
    <img src="{url_for('static', filename='segway-xyber-kv-making.webp')}" alt="Simple Energy EV Bike" width="600">
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

