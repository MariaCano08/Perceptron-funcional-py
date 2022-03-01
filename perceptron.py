import matplotlib.pyplot as plt
import numpy 
import random


def y(x,m,b):
    return m*x+b


def window():
    plt.plot(1,1,'tab:cyan',label="Estimada 0")
    plt.plot(1,1,'tab:pink',label="Estimada 1")
    plt.legend(loc = "upper right")
    plt.title("Perceptron: ")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()

def inputs():
    inputs_=[]
    input_=[]
    x1=[]
    x2=[]
    flag=True
    txt=open('input.txt')
    for linea in txt:
        input_=[-1]
        for lettle in linea:
            if lettle=='\n':
                continue
            elif  lettle == ",":
                continue
            else:
                change=int(lettle)
                input_.append(change)
                if flag :
                    x1.append(change)
                    flag= False
                else:
                    x2.append(change)
                    flag= True
        
        inputs_.append(input_) 
    txt.close()
    print("x1",x1,"x2",x2)
    return inputs_,x1,x2


def activation_funtion(u):
    if u<0:
        return 0
    else:
        return 1


def to_string(input_,boleano):
    if boleano == False :
        print("     ",input_, 0)
    else:
        print("     ",input_, 1)

def inicialize_w():
    return [random.random() for i in range(1,4)]

def change_w(w,theta,err,xi):
    nw=[]
    i=0
    for x in xi:
        nw.append(w[i]+(theta*err*x))
        i+=1
    print("nuevo w",nw)
    return nw

def outputs():
    output=[]
    with open("outputs.txt","r", encoding="utf-8") as f:
        for line in f:
            output.append(int(line))
    #print(output)
    return output


def perceptron(inputs, theta,x1,x2):
    
    fig, ax = plt.subplots()
    w=inicialize_w()
    flag= False
    em=100
    epoch=0
    output=outputs()
    j=0
    lim=[x for x in range(-2,3)]
    for x in output:
        if j==0:
            ax.scatter(x1[j],x2[j],color='tab:cyan')
        else:
            ax.scatter(x1[j],x2[j],color='tab:pink')
        j+=1

    while flag == False and epoch< em:
        flag=True
        i=0
        for input_ in inputs:
            wish_= output[i]
            have=activation_funtion(numpy.dot(input_,w))-theta
            err=wish_-have
            print("err",err,"wish",wish_,"have",have)
            print("error",err)
            if err !=0:
                flag=False
                w=change_w(w,theta,err,input_) #w,theta,err,xi
                # m=-(w[1]/w[2])
                # b=w[0]/w[2]    
                m=-(w[1]/w[2])
                b=theta/w[2]
                print("aqui")
                #ax.plot([-1,m*-1+b],[1,m*1+b],color='tab:red') # 
                
            i=i+1
        epoch+=1
        #break   

    m=-(w[1]/w[2])
    b=theta/w[2]
    ax.plot([-1,m*-1+b],[1,m*1+b],color='tab:green') #
    
    
    plt.show()



def start():
    theta=.4
    input_,x1,x2=inputs()
    perceptron(input_,theta,x1,x2)


    
if __name__ == '__main__':
    start()
