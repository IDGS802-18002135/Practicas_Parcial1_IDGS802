
from flask import Flask, request,render_template
import forms,math
import datetime
from datetime import datetime
import formsHoroscopo
app=Flask(__name__)

@app.route("/Practica3")
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

'''Practica 4'''
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


'''HOROSCOPO'''

@app.route("/horoscopo",methods=["GET","POST"])

def calcularHoroscopo():
    nombre=""
    apaterno=""
    amaterno=""
    dia=0
    mes=0
    anio=0
    signo="indefinido"
    edad=0
    imagen=""
    sexo=""

 
    rata=[1900, 1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
    buey=[1901, 1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]
    tigre=[1902, 1914, 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]
    conejo=[1903, 1915, 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2023]
    dragon=[1904, 1916, 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]
    serpiente=[1905, 1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]
    caballo=[1906, 1918, 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026]
    cabra=[1907, 1919, 1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027]
    mono=[1908, 1920, 1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028]
    gallo=[1909, 1921, 1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]
    perro=[1910, 1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]
    cerdo=[1911, 1923, 1935, 1947, 1971, 1983, 1995, 2007, 2019, 2031]

    horoscopo_form=formsHoroscopo.HoroscopoForm(request.form)
    if request.method=='POST':
        nombre=horoscopo_form.nombre.data
        apaterno=horoscopo_form.apaterno.data
        amaterno=horoscopo_form.amaterno.data
        dia=int(horoscopo_form.dia.data)
        mes=int(horoscopo_form.mes.data)
        anio=horoscopo_form.anio.data
        sexo=horoscopo_form.sexo.data
        
        if mes>datetime.now().month and dia>datetime.now().day:
            edad=datetime.now().year-anio-1
        elif mes<=datetime.now().month and dia<=datetime.now().day:
            edad=edad=datetime.now().year-anio
        elif mes<=datetime.now().month and dia>=datetime.now().day:
            edad=edad=datetime.now().year-anio
        
        
        imagen ="indefinido.png"
        for data in rata:    
            if anio==data:                    
                signo="rata"
                imagen="rata.jpg"
                

        
        for data in buey:    
            if anio==data:                    
                signo="buey"
                imagen="buey.jpg"
                
        
        
        for data in tigre:    
            if anio==data:                    
                signo="tigre"
                imagen="tigre.jpg"
                

        
        for data in conejo:    
            if anio==data:                    
                signo="conejo"
                imagen="conejo.jpg"
                
                
        
        for data in dragon:
            if anio==data:
                signo="dragon"
                imagen="dragon.jpg"
                
                
        
        for data in serpiente:
            if anio==data:
                signo="serpiente"
                imagen="serpiente.jpg"
                
                
        
        for data in caballo:
            if anio==data:
                signo="caballo"
                imagen="caballo.jpg"
                
                
        
        for data in cabra:
            if anio==data:
                signo="cabra"
                imagen="cabra.jpg"
                
                
        
        for data in mono:
            if anio==data:
                signo="mono"
                imagen="mono.jpg"
                
                
        
        for data in gallo:
            if anio==data:
                signo="gallo"
                imagen="gallo.jpg"
                
                
        
        for data in perro:
            if anio==data:
                signo="perro"
                imagen="perro.jpg"
                
                
        
        for data in cerdo:
            if anio==data:
                signo="cerdo"
                imagen="cerdo.jpg"
                
                
        
        
        
      
    return render_template("formularioHoroscopo.html",form=horoscopo_form,signo=signo,imagen=imagen,nombre=nombre,apaterno=apaterno,amaterno=amaterno,edad=edad)



if __name__=="__main__":
    app.run(debug=True)