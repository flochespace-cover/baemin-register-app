from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

GAS_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxqkvnWJHlgghjqfpzszpBGe11Cqu1kbRA9d6KU3MX3dHEmlz9pCP2SvZDxPJRQTzix/exec"

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')  # 모든 도메인 허용
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

@app.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 200  # CORS 프리플라이트 응답

    try:
        data = request.get_json()
        res = requests.post(GAS_WEBHOOK_URL, json=data)
        return jsonify({"status": "ok", "message": res.text})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/')
def home():
    return "✅ 플로체스페이스 등록 서버 작동 중입니다."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
