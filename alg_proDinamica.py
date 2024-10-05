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
    
    
    def alg_DP(self, w:list, v:list):
        W = w.pop(0)
        n = v.pop(0)
        self.mov+=2
        return self.knapSack(v,w,W,n)

    def knapSack(self, v, w, capacity, n):
        
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        self.mov+=(n+1) * (capacity+1)

        # Build the dp table
        for i in range(1, n + 1):
            for j in range(capacity + 1):
                self.comp+=1
                if w[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                    self.mov+=1
                else:
                    a = dp[i - 1][j]
                    b = dp[i - 1][j - w[i - 1]] + v[i - 1]
                    dp[i][j] = max(a, b)
                    self.mov+=3

        # Now trace back to find which items are included
        selected_items = [0] * n
        
        j = capacity
        self.mov+=n +1
        for i in range(n, 0, -1):
            self.comp+=1
            if dp[i][j] != dp[i - 1][j]:
                selected_items[i - 1] = 1
                j -= w[i - 1]
                self.mov+=2

        return selected_items, dp[n][capacity]


                    
    def main(self, w,v):
        antes = timeit.default_timer()
        saida = self.alg_DP(w,v)
        depois = timeit.default_timer() - antes

        return saida, depois




        
    
   

    


    

