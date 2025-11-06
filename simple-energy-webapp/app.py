from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Simple Energy 🚴‍♂️⚡</h1>
    <img src="https://www.simpleenergy.in/_next/image?url=%2Fimages%2Fhome%2Fbanner.webp&w=1920&q=75" alt="Simple Energy EV Bike" width="600">
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
