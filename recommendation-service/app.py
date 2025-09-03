from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/recommend')
def recommend():
  return jsonify({"recommendations": ["movie1","movie2","movie3"]})

@app.route('/health')
def health():
  return "ok"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5003)
