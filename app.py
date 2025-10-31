from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# CORS headers for all responses
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response

def fetch_api(url):
    """Helper function to fetch data from external APIs"""
    try:
        response = requests.get(url, timeout=10)
        try:
            return response.json()
        except:
            return {"success": True, "data": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/')
@app.route('/help')
def home():
    """API Documentation"""
    return jsonify({
        "success": True,
        "message": "API Wrapper - Available Endpoints",
        "endpoints": [
            {"path": "/upi", "params": "upi_id", "example": "/upi?upi_id=9864382851"},
            {"path": "/mobile", "params": "mobile, key(optional)", "example": "/mobile?mobile=7827163040"},
            {"path": "/aadhar", "params": "aadhar, key(optional)", "example": "/aadhar?aadhar=937264000578"},
            {"path": "/email", "params": "email, key(optional)", "example": "/email?email=test@example.com"},
            {"path": "/vehicle", "params": "rc, key(optional)", "example": "/vehicle?rc=UP4520210006534"},
            {"path": "/numdb", "params": "num", "example": "/numdb?num=3247452828"},
            {"path": "/imei", "params": "no", "example": "/imei?no=869945059254041"},
            {"path": "/dl", "params": "dl", "example": "/dl?dl=UP4520210006534"},
            {"path": "/fb", "params": "fb", "example": "/fb?fb=9059061797"},
            {"path": "/ration", "params": "ration", "example": "/ration?ration=WAP0135603A0139"}
        ]
    })

@app.route('/upi')
def upi():
    upi_id = request.args.get('upi_id')
    if not upi_id:
        return jsonify({"success": False, "error": "Missing upi_id parameter"}), 400
    
    url = f"https://upi.info-sudiptasmm.workers.dev/upi_id={upi_id}"
    return jsonify(fetch_api(url))

@app.route('/mobile')
def mobile():
    mobile = request.args.get('mobile')
    if not mobile:
        return jsonify({"success": False, "error": "Missing mobile parameter"}), 400
    
    key = request.args.get('key', 'deva555')
    url = f"https://except-rod-merchant-cayman.trycloudflare.com/search?key={key}&mobile={mobile}"
    return jsonify(fetch_api(url))

@app.route('/aadhar')
def aadhar():
    aadhar = request.args.get('aadhar')
    if not aadhar:
        return jsonify({"success": False, "error": "Missing aadhar parameter"}), 400
    
    if len(aadhar) == 12:
        url = f"https://aadhartofamily.errornetwork807010.workers.dev/?aadhar={aadhar}"
    else:
        key = request.args.get('key', 'deva555')
        url = f"https://except-rod-merchant-cayman.trycloudflare.com/search?key={key}&aadhar={aadhar}"
    
    return jsonify(fetch_api(url))

@app.route('/email')
def email():
    email = request.args.get('email')
    if not email:
        return jsonify({"success": False, "error": "Missing email parameter"}), 400
    
    key = request.args.get('key', 'deva555')
    url = f"https://except-rod-merchant-cayman.trycloudflare.com/search?key={key}&email={email}"
    return jsonify(fetch_api(url))

@app.route('/vehicle')
def vehicle():
    rc = request.args.get('rc')
    if not rc:
        return jsonify({"success": False, "error": "Missing rc parameter"}), 400
    
    key = request.args.get('key', 'DEBA')
    url = f"https://aetherosint.site/cutieee/vehicle.php?key={key}&rc={rc}"
    return jsonify(fetch_api(url))

@app.route('/numdb')
def numdb():
    num = request.args.get('num')
    if not num:
        return jsonify({"success": False, "error": "Missing num parameter"}), 400
    
    url = f"https://ahmadmodstools.online/apis/db.php?num={num}"
    return jsonify(fetch_api(url))

@app.route('/imei')
def imei():
    no = request.args.get('no')
    if not no:
        return jsonify({"success": False, "error": "Missing no parameter"}), 400
    
    url = f"https://emei-api-j4tnx.vercel.app/no={no}"
    return jsonify(fetch_api(url))

@app.route('/dl')
def dl():
    dl = request.args.get('dl')
    if not dl:
        return jsonify({"success": False, "error": "Missing dl parameter"}), 400
    
    url = f"https://driving.errornetwork807010.workers.dev/?dl={dl}"
    return jsonify(fetch_api(url))

@app.route('/fb')
def fb():
    fb = request.args.get('fb')
    if not fb:
        return jsonify({"success": False, "error": "Missing fb parameter"}), 400
    
    url = f"https://fb.errornetwork807010.workers.dev/?fb={fb}"
    return jsonify(fetch_api(url))

@app.route('/ration')
def ration():
    ration = request.args.get('ration')
    if not ration:
        return jsonify({"success": False, "error": "Missing ration parameter"}), 400
    
    url = f"https://rationx.errornetwork807010.workers.dev/?ration={ration}"
    return jsonify(fetch_api(url))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
