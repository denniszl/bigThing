from flask import Flask, request, render_template
from theNextBigThing.makeBig import makeBig

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('big.html')
    elif request.method == 'POST':
        print request.form
        return makeBig(request.form['makeMeBig'])

if __name__ == '__main__':
    app.run()
