# class Solucao_guloso_backtracking:
#     def main(self, arr):
#         def calcula_subsequencia(arr, dict,n,i):
#             if n==len(arr):
#                 return dict

#             if max(dict[i])<arr[n]:
#                 dict[i] = dict[i] + [arr[n]]

#             return calcula_subsequencia(arr,dict,n+1,i)

#         maior_subs = []
#         atual = []
#         for i in range(0,len(arr)):
#             dict ={}
#             dict[i] = [arr[i]]
#             atual = max(calcula_subsequencia(arr, dict,i+1,i).values(), key=len)
#             maior_subs = max(atual, maior_subs, key=len)
#         return maior_subs
    
class Solucao_prog_dinamica:
    comp = 0
    mov = 0
    def reset(self):
            self.comp = 0
            self.mov = 0
    def main(self, arr):
        def calcula_subsequencia(arr,n): # primeira chamada (calcula_subsequencia(arr,len(arr),[]))
            if n==0:
                self.comp+=1
                return arr
            
            best = [None] * n
            next = [0] * n
            best[n-1] = 1 
            self.mov= 2*n + 1
            for i in range(n-1,-1, -1):
                best[i] = 1
                self.mov+=1
                for j in range(i+1, n):
                    self.comp+=1
                    if arr[j] > arr[i] : 
                        self.comp+=1
                        if 1+best[j]>best[i]:
                            best[i]=1+best[j]
                            next[i] = j
                            self.mov+=2
            maior_best = max(best) # itera n-1 vezes, retornando um valor x
            indice_maior_best = best.index(maior_best)
            self.comp+=2*(n-1)
            self.mov+=2 # considera-se uma movimentação para index e max, 
                        # ja que é dificil saber o numero exato

            resposta = []
            resposta.append(arr[indice_maior_best])
            self.mov+=1

            i = next[indice_maior_best]
            self.mov+=1
            self.comp+=1
            while(i!=0):
                resposta.append(arr[i])
                i = next[i]
                self.mov+=2 
                self.comp+=1
            

            return best, next,resposta, f'size={n}, comp={self.comp}, mov={self.mov}'
        return calcula_subsequencia(arr, len(arr))


v = [32,19,32,17,31,43,30,29,54,16,28,66,15,41,65,14,50]
spdv = Solucao_prog_dinamica()
print(spdv.main(v))
spdv.reset()


arr1 = [34, 7, 23, 32, 5, 62, 32, 12, 45, 18]
spd1 = Solucao_prog_dinamica()
print(spd1.main(arr1))
spd1.reset()

arr2 = [19, 22, 8, 13, 25, 30, 5, 14, 27, 21, 44, 3, 11, 45, 29]
spd2 = Solucao_prog_dinamica()
print(spd2.main(arr2))
spd1.reset()

arr3 = [12, 45, 23, 67, 8, 39, 49, 50, 20, 15,
         38, 5, 18, 31, 14, 60,
         10, 29,
         11]
spd3 = Solucao_prog_dinamica()
print(spd3.main(arr3))



arr4 = [56, 78, -2, -5,
         -1 ,0 ,4 ,8 ,12 ,
         -6 ,15 ,18 ,20 ,
         -10 ,25 ,30 ,
         -3 ,9 ,11 ,
         -4 ,14 ,28 ,
         -7 ,35 ,40]
spd4 = Solucao_prog_dinamica()
print(spd4.main(arr4))


arr5 = [56, 78, -2, -5,
         -1 ,0 ,4 ,8 ,12 ,
         -6 ,15 ,18 ,20 ,
         -10 ,25 ,30 ,
         -3 ,9 ,11 ,
         -4 ,14 ,28 ,
         -7 ,35 ,40,24,41,765]
spd5 = Solucao_prog_dinamica()
print(spd5.main(arr5))
