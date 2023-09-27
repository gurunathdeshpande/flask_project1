from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/akshay' , methods=['POST'])
def math_operation():
    if (request.method=='POST'):
     operation=request.form['operation']
     num1=int(request.form['num1'])
     num2=int(request.form['num2'])
     result=0


     if operation=="add":
         result=num1+num2
     elif operation=="multifly":
         result=num1*num2
     elif operation=="division":
         result=num1/num2
     else:
         result=num1-num2

     return render_template("result.html",result=result)


if __name__=="__main__":
    app.run(debug=True)