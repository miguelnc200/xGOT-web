from flask import Flask, render_template, request, jsonify
import numpy as np
from xgot import compute_xgot_modified

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_xsit', methods=['POST'])
def calculate_xsit():
    try:
        data = request.get_json()

        balon_pos = np.array(data["pos_balon"])           # 3D
        portero = np.array(data["portero"])                # 3D
        end_pos = np.array(data["end_pos"])                # 3D
        portero_end = np.array(data["porterofin"])

        xgot = compute_xgot_modified(balon_pos, portero, end_pos, portero_end)

        return jsonify({'xsit': round(float(xgot), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
