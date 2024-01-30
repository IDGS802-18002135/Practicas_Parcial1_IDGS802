from flask import Flask, request,render_template
import forms,math
app=Flask(__name__)

@app.route("/distancia",methods=["GET","POST"])

def distancia():
    x1=""
    x2=""
    y1=""
    y2=""
    dist=""
    distancia_form=forms.DistanciaForm(request.form)
    if request.method=='POST':
        x1=distancia_form.x1.data
        x2=distancia_form.x2.data
        y1=distancia_form.y1.data
        y2=distancia_form.y2.data
        
        restax=((int(x2)-int(x1))**2)   
        restay=((int(y2)-int(y1))**2) 
        print("resta x2-x1")
        print(restax)
        print("resta y2-y1")
        print(restay) 
        print("suma:")
        print(restax+restay)

        dist=math.sqrt(restax+restay) 
        
        print("x1 :{}".format(x1))
        print("x2 :{}".format(x1))
        print("y1 :{}".format(y1))
        print("y2 :{}".format(y2))
        
        
    return render_template("formularioDistanciaEntrePuntos.html",form=distancia_form,x1=x1,x2=x2,y1=y1,y2=y2,dist=dist)


if __name__=="__main__":
    app.run(debug=True)