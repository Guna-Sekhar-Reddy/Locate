from flask import *

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('base.html')

@app.route('/locate',methods=["POST"])

def locate():
    latitude=request.form['latitude']
    longitude=request.form['longitude']
    return render_template('locate.html',latitude=latitude,longitude=longitude)

if __name__ == "__main__" :
    app.run(debug=True)