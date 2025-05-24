from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GAS_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxqkvnWJHlgghjqfpzszpBGe11Cqu1kbRA9d6KU3MX3dHEmlz9pCP2SvZDxPJRQTzix/exec"

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        res = requests.post(GAS_WEBHOOK_URL, json=data)
        return jsonify({"status": "ok", "message": res.text})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def hello():
    return "✅ 플로체스페이스 기사등록 서버 작동 중입니다."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)