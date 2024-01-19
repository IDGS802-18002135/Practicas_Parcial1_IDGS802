import os

class impPiramide:
    num1=0
    

    def __init__(self,a):
        self.num1=a

    def Piram(self):
        self.res=self.num1
        '''int(input("¿de que tamaño quiere la base de la piramide?"))
        '''
        i=1
        caracter="*"
        for piramide in range(1,self.res+1,1):
            while i<=self.res:    
                print(caracter*i)
                i+=1

def main():
    #Linea para limpiar la terminal
    os.system('cls')
    num2=int(input("¿de que tamaño quiere la base de la piramide?"))
    obj=impPiramide(num2)
    obj.Piram()

if __name__=="__main__":
    main()





    
    