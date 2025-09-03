from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
  data = request.json or {}
  user = data.get('user','guest')
  # return a fake JWT token
  return jsonify({"token": f"jwt-token-for-{user}"})

@app.route('/health')
def health():
  return "ok"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
