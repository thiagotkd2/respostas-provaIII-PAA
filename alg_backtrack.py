import timeit


class Solucao:
    comp = 0
    mov = 0

    def indice_menor(self,arr):
        if len(arr)>0:
            return arr.index(min(arr))

    def reset(self):
        self.comp = 0
        self.mov = 0
    
    
    

    
    def knapsack(self, weights, values, capacity, n):
        if n == 0 or capacity == 0:
            self.comp += 1
            self.comp += 1
            return 0

        if weights[n-1] > capacity:
            self.comp += 1
            return self.knapsack(weights, values, capacity, n-1)

        else:
            self.mov += 1
            include_item = values[n-1] + self.knapsack(weights, values, capacity - weights[n-1], n-1)
            self.mov += 1
            exclude_item = self.knapsack(weights, values, capacity, n-1)
            self.comp += 1
            return max(include_item, exclude_item)


    def alg_BT(self, w:list, v:list):
        W = w.pop(0)
        n = v.pop(0)
        self.mov+=1

        return self.knapsack(w,v,W,n)
                    
    def main(self, w,v):
        antes = timeit.default_timer()
        saida = self.alg_BT(w,v)
        depois = timeit.default_timer() - antes

        return saida, depois




        
    
   

    


    

