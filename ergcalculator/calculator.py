from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from conversion import basic_conversion

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tseconds = request.form['tseconds']
    tminutes = request.form['tminutes']
    distance = request.form['distance']
    sseconds = request.form['sseconds']
    sminutes = request.form['sminutes']

    result = basic_conversion(tminutes, tseconds, sminutes, sseconds, distance)

    return render_template('index.html', prediction_text=str(result))

if __name__ == "__main__":
    app.run(debug=True)

# have a box to type in erg scores
# submit
# show conversion after they hit submit