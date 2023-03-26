# usando interrupção
# 1) Criar a função callback usando variável globalhelp
z=0
def cb1(x):
    global z
    global i
    global j
    global k
    i=1800
    j=4095
    k=i/j
    if z == 0 :
        z=1
    elif z == 1:
        z=0
    print('K1 - PE3 clicado x=',x)

def cb0(x):
    print('K0 - PE4 clicado x=',x)

# 2) Registrar as interrupções

k1=pyb.ExtInt('PE3', pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, cb1)
k0=pyb.ExtInt('PE4', pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, cb0)

# 3) rodar o programa principal
i = 0
while True:
    print(i,z)
    i=i+1
    pyb.delay(5000)
    
