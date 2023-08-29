from flask import Flask, redirect, url_for, render_template, request
from model import predict_titanic
app = Flask(__name__)

@app.route('/result/<surv>')
def result(surv):
   return print(surv)

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
    
        tix = request.form.get['tix_class']
        age = request.form.get["age"]
        sibsp = request.form.get["sibsp"]
        parch = request.form.get["parch"]
        fare = request.form.get['fare']
        sex = request.form.get["sex"]
        embark = request.form.get["embark"]

        demo_list = [tix,age,sibsp,parch,fare,sex,embark]
        survival = predict_titanic(demo_list)
        return redirect(url_for('result', surv = survival))
      
   else:
      return render_template("/")

if __name__ == '__main__':
   app.run(debug = True)