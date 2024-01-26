
from flask import Flask, request,render_template
app=Flask(__name__)

@app.route("/")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET","POST"])
def multiplica(): 
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        num3=0
        opciones=request.form.get("opciones")
        if opciones=="suma":
            num3=int(num1)+int(num2)
        elif opciones=="resta":
            num3=int(num1)-int(num2)
        elif opciones=="multiplicacion":
            num3=int(num1)*int(num2)
        elif opciones=="division":
            num3=int(num1)/int(num2)
        return render_template("formulario1.html",resultado=num3,operacion=opciones)

if __name__=="__main__":
    app.run(debug=True)