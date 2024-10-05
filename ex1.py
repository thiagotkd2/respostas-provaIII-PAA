import alg_guloso
import alg_proDinamica
import alg_backtrack
import alg_genetico

v = []
w = []
size = -2
max_w=0

f = open("knapPI_1_100_1000_1", "r")
mapa = []
i = 0
for linha in f:
    if i ==int(size)+1:
        mapa = linha.split()
        break
    linha_separada = linha.split()
    if i ==0:
        size = linha_separada[0]
    v.append(int(linha_separada[0])) 
    w.append(int(linha_separada[1]))
    i+=1



    

w_aux = w[:]
v_aux = v[:]



a = alg_guloso.Solucao()
print(a.main(w_aux,v_aux))
print(f'Mov: {a.mov}, Comp: {a.comp}')
print("-------------------")

w_aux = w[:]
v_aux = v[:]

dp = alg_proDinamica.Solucao()
print(dp.main(w_aux,v_aux))
print(f'Mov: {dp.mov}, Comp: {dp.comp}')
print("-------------------")

w_aux = w[:]
v_aux = v[:]

bt = alg_backtrack.Solucao()
print(bt.main(w_aux,v_aux))
print(f'Mov: {bt.mov}, Comp: {bt.comp}')
print("-------------------")
w_aux = w[:]
v_aux = v[:]

gen = alg_genetico.Solucao()
print(gen.main(w_aux,v_aux))
print(f'Mov: {gen.mov}, Comp: {gen.comp}')
print("-------------------")

v = []
w = []

# f2

f2 = open("knapPI_1_500_1000_1", "r")
mapa = []
i = 0
for linha in f2:
    if i ==int(size)+1:
        mapa = linha.split()
        break
    linha_separada = linha.split()
    if i ==0:
        size = linha_separada[0]
    v.append(int(linha_separada[0])) 
    w.append(int(linha_separada[1]))
    i+=1


w_aux = w[:]
v_aux = v[:]

a = alg_guloso.Solucao()
print(a.main(w_aux,v_aux))
print(f'Mov: {a.mov}, Comp: {a.comp}')
print("-------------------")
w_aux = w[:]
v_aux = v[:]

dp = alg_proDinamica.Solucao()
print(dp.main(w_aux,v_aux))
print(f'Mov: {dp.mov}, Comp: {dp.comp}')
print("-------------------")
# w_aux = w[:]
# v_aux = v[:]

# bt = alg_backtrack.Solucao()
# print(bt.main(w_aux,v_aux))
# print(f'Mov: {bt.mov}, Comp: {bt.comp}')

w_aux = w[:]
v_aux = v[:]

gen = alg_genetico.Solucao()
print(gen.main(w_aux,v_aux))
print(f'Mov: {gen.mov}, Comp: {gen.comp}')