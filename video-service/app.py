from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/stream')
def stream():
  return jsonify({"stream_url": "http://example.com/mock-stream"})

@app.route('/health')
def health():
  return "ok"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5002)
