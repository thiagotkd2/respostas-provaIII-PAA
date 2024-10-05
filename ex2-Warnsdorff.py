import timeit

class Solucao:
    def __init__(self):
        self.comp = 0
        self.movimentacoes = 0

    def reset(self):
        self.comp=0
        self.movimentacoes=0

    def printArr(self, arr,f):
        for i in arr:
            f.write("[")
            for j in i:
                f.write(f'{j} ')
            f.write("]\n")

    def simulacao_pos_inicio(self):
        f = open("output.txt", "a")
        for i in range(0,8):
            for j in range(0,8):
                    inicio = timeit.default_timer()
                    resultado = s.solucao(8,i,j)
                    tempo_gasto = timeit.default_timer() - inicio
                    self.printArr(resultado,f)
                    f.write(f'comparacoes: {self.comp}, movimentacoes: {self.movimentacoes}\ntempo: {tempo_gasto}\n')
                    f.write(f'quadrante: [{i}][{j}]\n')
                    f.write("------------------------------------\n\n")
                    s.reset()
        f.close()

    def simulacao_tamanho(self):
        f = open("output2.txt", "a")
        for i in range(5,9):
                inicio = timeit.default_timer()
                resultado = s.solucao(i,0,0)
                tempo_gasto = timeit.default_timer() - inicio
                self.printArr(resultado,f)
                f.write(f'comparacoes: {self.comp}, movimentacoes: {self.movimentacoes}\ntempo: {tempo_gasto}\n')
                f.write(f'tamanho: [{i}][{i}]\n')
                f.write("------------------------------------\n\n")
                s.reset()
        f.close()
 
    def solucao(self,n,x_casa_inicial,y_casa_inicial):
        def movimentos_seguintes(x,y):
            c = 0
            for m in range(8):
                xn = x + h[m]
                yn = y + v[m]
                self.movimentacoes+=2
                self.comp+=1
                if 0 <= xn < len(arr):
                    self.comp+=1
                    if 0 <= yn < len(arr):
                        self.comp=self.comp+1
                        if arr[xn][yn] == -1:
                            c+=1
            return c
 
        def tenta(numero_mov, x,y):
            if numero_mov==len(arr)**2-1: # "T(0)" da recursao
                self.comp= self.comp +1
                return True
            
            movimentos_possiveis = []
            for m in range(0,8): # 8 possiveis movimentos
                # movimentando o cavalo
                xn = x+h[m]
                yn = y+v[m]
                self.movimentacoes=self.movimentacoes+2
                self.comp = self.comp +1
                # verifica as bordas do tabuleiro e se ja passou pelo quadrante
                if 0 <= xn < len(arr):
                    self.comp=self.comp+1
                    if 0 <= yn < len(arr):
                        self.comp=self.comp+1
                        if arr[xn][yn] == -1:
                            movimentos_possiveis.append((movimentos_seguintes(xn,yn), xn,yn))
                            
            movimentos_possiveis.sort()

            for _, xn, yn in movimentos_possiveis:
                self.movimentacoes+=1
                arr[xn][yn] = numero_mov +1
                self.comp+=1
                if tenta(numero_mov+1, xn,yn):
                    return True   # caso o movimento seja possivel, retorne true
                self.movimentacoes+=1
                arr[xn][yn]=-1  # senao reseto o movimento
            return False # caso os movimentos se esgotem, retorne false
        
        def passeio_do_cavalo():
            if tenta(0,x_casa_inicial,y_casa_inicial):
                return arr
            return None
     
        arr = [([-1] * n) for _ in range(n)]
        h = [0] * 8
        v = [0] * 8
        h=[2, 1, -1, -2, -2, -1, 1, 2]
        v=[1, 2, 2, 1, -1, -2, -2, -1]
        arr[x_casa_inicial][y_casa_inicial] = 0
        return passeio_do_cavalo()
            
s = Solucao()
arr = s.solucao(8,0,0)
s.simulacao_tamanho()