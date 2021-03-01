import numpy as np
class QuantumOperatorU3:
    def U3(self):
        circ = QuantumCircuit(7)
        for i in range(6):
            circ.h(i)
            circ.cx(i,6)

        circ.measure_all()

        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        b = result.items()
        for x, y in b:
            number = x
        number = str(number)

        def B(binary): 
            decimal = 0 
            for digit in binary: 
                decimal = decimal*2 + int(digit) 
            return decimal

        C = B(number)
        a = 1-(C/64)
        
        import numpy as np
        pi = np.pi
        b = np.arccos(a)
        return b
        
    def __init__(self):
        self.shangGua = np.array([[-1],[-1],[-1]])
        self.shiaGua = np.array([[-1],[-1],[-1]])
        self.shangGua_zhen = np.array([[-1],[-1],[-1]])
        self.shiaGua_zhen = np.array([[-1],[-1],[-1]])
        self.crBuffer = []
        '''
        變卦
        '''
    def bianGua(self): #shangGua: 上卦 shiaGua:下卦
        circ = QuantumCircuit(6)
        for i in range(6):
            circ.u(self.U3(), 0, 0,[i])
            circ.x(i)
        
        circ.measure_all()
    
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        self.__resultToGua(result)
        return(self.shangGua, self.shiaGua)
        '''
        互卦
        '''
    def huGua(self):
        qr = QuantumRegister(6)
        cr = ClassicalRegister(8) # cr[6]: for qr[0] cr[7]: for qr[5]
        circ = QuantumCircuit(qr, cr)
        for i in range(6):
            circ.u(self.U3(), 0, 0,[i])
    
        circ.measure(qr[1], cr[0])
        circ.measure(qr[2], cr[1])
        circ.measure(qr[3], cr[2])
        circ.measure(qr[2], cr[3])
        circ.measure(qr[3], cr[4])
        circ.measure(qr[4], cr[5])

        circ.measure(qr[0], cr[6])
        circ.measure(qr[1], cr[7])
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
            
        for x,y in result.items():
            Gua = x
        self.shangGua[0,0]=Gua[7]
        self.shangGua[1,0]=Gua[6]
        self.shangGua[2,0]=Gua[5]
        self.shiaGua[2,0]=Gua[4]
        self.shiaGua[1,0]=Gua[3]
        self.shiaGua[0,0]=Gua[2]

        self.crBuffer.append(Gua[1])# q[0]
        self.crBuffer.append(Gua[0])# q[6]

        return(self.shangGua, self.shiaGua)
        '''
        綜卦
        '''
    def tzungGua(self):
        circ = QuantumCircuit(6)
        for i in range(6):
            circ.u(self.U3(), 0, 0,[i])
        circ.swap(0,2)
        circ.swap(3,5)
       
        circ.measure_all()
    
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        self.__resultToGua(result)
        return(self.shangGua, self.shiaGua)
    def __resultToGua(self, result): #string to shanGua & shiaGua
            for x,y in result.items():
                Gua = x
            self.shangGua[0,0]=Gua[5]
            self.shangGua[1,0]=Gua[4]
            self.shangGua[2,0]=Gua[3]
            self.shiaGua[2,0]=Gua[2]
            self.shiaGua[1,0]=Gua[1]
            self.shiaGua[0,0]=Gua[0]
    def transZhenGua(self, mode="huGua"): # mode = "huGua" or "bianGua" or "tzungGua" 
            if(mode=="huGua"):
                self.shangGua_zhen[0,0] = self.crBuffer[0]
                self.shangGua_zhen[1,0] = self.shangGua[0,0]
                self.shangGua_zhen[2,0] = self.shangGua[1,0]

                self.shiaGua_zhen[0,0] = self.shiaGua[1,0]
                self.shiaGua_zhen[1,0] = self.shiaGua[2,0]
                self.shiaGua_zhen[2,0] = self.crBuffer[1]

                return(self.shangGua_zhen, self.shiaGua_zhen)
            elif(mode=="bianGua"):
                self.shangGua_zhen = np.where((self.shangGua==0)|(self.shangGua==1), self.shangGua^1, self.shangGua)
                self.shiaGua_zhen = np.where((self.shiaGua==0)|(self.shiaGua==1), self.shiaGua^1, self.shiaGua)
                return(self.shangGua_zhen, self.shiaGua_zhen)
            elif(mode=="tzungGua"):
                self.shangGua_zhen = np.flip(self.shangGua)
                self.shiaGua_zhen = np.flip(self.shiaGua)
                return(self.shangGua_zhen, self.shiaGua_zhen)
            else:
                return -1 #error

import numpy as np
from qiskit import *
class ClassicalOperatorU3:
        
    def U3(self):
        circ = QuantumCircuit(7)
        for i in range(6):
            circ.h(i)
            circ.cx(i,6)

        circ.measure_all()

        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        b = result.items()
        for x, y in b:
            number = x
        number = str(number)

        def B(binary): 
            decimal = 0 
            for digit in binary: 
                decimal = decimal*2 + int(digit) 
            return decimal

        C = B(number)
        a = 1-(C/64)

    #circ1 = QuantumCircuit(6)
        import numpy as np
        pi = np.pi
        b = np.arccos(a)
        return b
        
    def __init__(self):
        self.shangGua = np.array([[-1],[-1],[-1]])
        self.shiaGua = np.array([[-1],[-1],[-1]])
    '''
    變卦
    '''
    def bianGua(self): #shangGua: 上卦 shiaGua:下卦
        assert self.shangGua[0,0] != -1
        print("[classical變卦]")
        shangGua = np.where((self.shangGua==0)|(self.shangGua==1), self.shangGua^1, self.shangGua)
        shiaGua = np.where((self.shiaGua==0)|(self.shiaGua==1), self.shiaGua^1, self.shiaGua)
        return(shangGua, shiaGua) 
    '''
    互卦
    '''
    def huGua(self):
        assert self.shangGua[0,0] != -1
        print("[classical互卦]")
        shangGua = np.array([ [self.shangGua[1,0]],
                              [self.shangGua[2,0]],
                              [self.shiaGua[0,0]]])
        shiaGua = np.array([ [self.shangGua[2,0]],
                             [self.shiaGua[0,0]],
                             [self.shiaGua[2,0]]])
        return(shangGua, shiaGua)
    '''
    綜卦
    '''
    def tzungGua(self):
        assert self.shangGua[0,0] != -1
        print("[classical綜卦]")
        shangGua = np.flip(self.shangGua)
        shiaGua = np.flip(self.shiaGua)
        return(shangGua, shiaGua)
    '''
    正卦
    '''
    def zhenGua(self):
        print("[classical正卦]")
        self.getGua("shangGua")
        self.getGua("shiaGua")
        return(self.shangGua, self.shiaGua)
    def getGua(self,mode="shangGua"): #Two mode: shanGua or shiaGua
        qr = QuantumRegister(3)
        cr = ClassicalRegister(3)
        circuit = QuantumCircuit(qr, cr)
        for i in range(3):
            circuit.u3(self.U3(), 0, 0,[i])
        circuit.measure(qr, cr)
        get_ipython().run_line_magic('matplotlib', 'inline')
        circuit.draw(output='mpl')
        backend = Aer.get_backend('qasm_simulator')
        job = execute(circuit, backend, shots=1)
        result = job.result().get_counts(circuit)
        for x,y in result.items():
            Gua = x
                #print(Gua)
        if(mode=="shangGua"):
            self.shangGua[0,0] = Gua[2]
            self.shangGua[1,0] = Gua[1]
            self.shangGua[2,0] = Gua[0]
                #print(self.shangGua)
        elif(mode=="shiaGua"):
            self.shiaGua[0,0] = Gua[2]
            self.shiaGua[1,0] = Gua[1]
            self.shiaGua[2,0] = Gua[0]
                #print(self.shiaGua)
        else:
            print("mode error")

def get64txt():
    zdic = {}
    with open('./64.txt', encoding = 'utf8') as zfile:
        for line in zfile:
            z = line.split(' ', 1)
            key = z[0]
            value = z[1].split('，',1)
            zdic[key] = value
    return zdic
# for x,y in zdic.items():
#     print('%s %s %s' %(x,y[0],y[1])) 
zdic = get64txt()

def explanGua(shangGua, shiaGua):
    key = str(shangGua[0,0])+str(shangGua[1,0])+str(shangGua[2,0])+str(shiaGua[0,0])+str(shiaGua[1,0])+str(shiaGua[2,0])
    #print(key)
    #print(type(key))
    #print(zdic.get(key))
    return(zdic.get(key))

quantumOp = QuantumOperatorU3()
quantumOp.tzungGua()
quantumOp.bianGua()
quantumOp.huGua()
#quantumOp.transZhenGua("huGua")

gua = {'1' : 'tzungGua', 
       '2' : 'bianGua', 
       '3' : 'huGua'}

while True:
    try:
        print('請如下選擇所卜之卦：\n1代表綜卦;2代表變卦;3代表互卦;9代表重新測卦;0代表結束卜卦')
        i = str(input())
        if i == '0':
            break
        elif i == '9':
            quantumOp = QuantumOperatorU3()
            quantumOp.tzungGua()
            quantumOp.bianGua()
            quantumOp.huGua()
            continue
        quantumOp.transZhenGua(gua[i])
        print('\n')
        print(explanGua(quantumOp.shangGua_zhen, quantumOp.shiaGua_zhen))
        print('\n')
    except KeyError:
        print("\n輸入格式錯誤，請重新輸入\n")