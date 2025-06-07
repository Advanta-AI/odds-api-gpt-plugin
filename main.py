
from flask import Flask, send_file
app = Flask(__name__)

@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    return send_file("ai-plugin.json", mimetype='application/json')

@app.route('/openapi.yaml')
def serve_openapi():
    return send_file("openapi.yaml", mimetype='text/yaml')

@app.route('/')
def home():
    return "🎯 GPT Plugin is Live"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
