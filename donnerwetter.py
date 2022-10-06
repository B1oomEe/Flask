from flask import Flask, request
from EqualSolver import GetDis
app = Flask(__name__)
@app.route('/variable/<a>&<b>&<c>')
def equal(a, b, c): return GetDis(int(a), int(b), int(c))
app.run(host='localhost', port=80)