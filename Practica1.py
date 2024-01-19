import os

class listaNum:
    num1 = 0

    def __init__(self, a):
        self.num1 = a

    def ingresarNum(self):
        self.res = self.num1
        i = 1
        numlista = 0
        lista2 = []
        while i <= self.res:
            numlista = int(input("Ingrese numero: "))
            lista2.append(numlista)
            i += 1
        return lista2

    def ordenar(self, lista):
        lista.sort()
        print(lista)
    
    def separarNumeros(self,lista):
        lista.sort()
        listaPar=[]
        listaImpar=[]
        listaPar2=[]
        listaImpar2=[]

        for data in lista:
            if data%2==0 and data not in listaPar:
                    listaPar.append(data)
                            
            elif data%2!=0 and data not in listaImpar:
                    listaImpar.append(data)
        print("Numeros pares")
        print(listaPar)
        print("Numeros Impares")
        print(listaImpar)
        print("Cantidad de numeros pares")
        for data in listaPar:
            cantidad=lista.count(data)
            
            print("{}={}".format(data,cantidad))

        print("Cantidad de numeros impares")
        for data in listaImpar:
            cantidad=lista.count(data)
            
            print("{}={}".format(data,cantidad))

        

    
     

def main():
    # Línea para limpiar la terminal
    os.system('cls')
    num2 = int(input("¿Cuantos numero desea ingresar?: "))
    obj = listaNum(num2)
    listaRespuesta = obj.ingresarNum()
    print("Numeros ordenados")
    obj.ordenar(listaRespuesta)
    obj.separarNumeros(listaRespuesta)
   
    

if __name__ == "__main__":
    main()
