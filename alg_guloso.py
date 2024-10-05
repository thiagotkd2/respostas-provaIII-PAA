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
    
    
    def alg_guloso(self, w:list, v:list):

        
        W = w.pop(0)
        n = v.pop(0)


        self.mov+=2
        return self.knapSack(v,w,W,n)

    def knapSack(self,v,w,capacity,n):
        total_value = 0
        total_weight = 0
        selected_items = [0] * n
        w_aux = w[:]
        self.mov += 2*n


        i = 0

        self.comp+=1
        while i <n:
            self.comp+=1
            idx_min = self.indice_menor(w_aux) # n
            if not total_weight + w_aux[idx_min] <= capacity:
                self.comp+=1
                return total_value,selected_items
            
            self.mov+=n
            
            selected_items[idx_min] = 1
            total_value += v[idx_min]
            total_weight += w_aux[idx_min]
            w_aux[idx_min] = float('inf')
            self.mov+=4
            i+=1

        return total_value, selected_items

                    
    def main(self, w,v):
        antes = timeit.default_timer()
        saida = self.alg_guloso(w,v)
        depois = timeit.default_timer() - antes

        return saida, depois




        
    
   

    


    

