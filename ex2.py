import timeit

class Solucao:
    def __init__(self):
        self.comp = 0
        self.movimentacoes = 0

    def reset(self):
        self.comp=0
        self.movimentacoes=0
 
    def solucao(self,n,x_casa_inicial,y_casa_inicial):
        def tenta(numero_mov, x,y):
            if numero_mov==len(arr)**2-1: # "T(0)" da recursao
                self.comp= self.comp +1
                return True
            for m in range(0,8): # 8 possiveis movimentos
                # movimentando o cavalo
                xn = x+h[m]
                yn = y+v[m]


                self.comp = self.comp +1
                # verifica as bordas do tabuleiro e se ja passou pelo quadrante
                if 0 <= xn < len(arr):
                    if 0 <= yn < len(arr):
                        self.comp=self.comp+1
                        if arr[xn][yn] == -1:
                            self.comp=self.comp+1
                            # registro o movimento
                            arr[xn][yn]=numero_mov+1
                            self.movimentacoes+=1

                            self.comp = self.comp +1
                            # tento um movimento
                            if tenta(numero_mov+1, xn,yn):
                                return True   # caso o movimento seja possivel, retorne true
                            arr[xn][yn]=-1  # senao reseto o movimento
                            self.movimentacoes+=1
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
        antes = timeit.default_timer()
        output=passeio_do_cavalo()
        tempo = timeit.default_timer() - antes
        return [output, self.comp, self.movimentacoes, tempo]
            
s = Solucao()
print(s.solucao(5,0,0))
s.reset()
print(s.solucao(6,0,0))
s.reset()
print(s.solucao(7,0,0))
s.reset()
print(s.solucao(8,0,0))
