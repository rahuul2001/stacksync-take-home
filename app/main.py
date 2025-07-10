from flask import Flask, request, jsonify
from executor import execute_script

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    if not data or 'script' not in data:
        return jsonify({'error': 'Missing "script" field'}), 400

    script = data['script']
    try:
        result, stdout = execute_script(script)
        return jsonify({"result": result, "stdout": stdout})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
