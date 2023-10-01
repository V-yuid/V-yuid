ch = ['&','¬','∧','∨','⊕','→','⇔','x','y','z','w','(',')',' ', 'A','B','C','D','E','F']
ch_p = ['and', 'not', 'and', 'or', '!=', '<=', '==','x','y','z','w','(',')',' ', 'A','B','C','D','E','F']
alf = ['x','y','z','w', 'A','B','C','D','E','F']
x=0
y=0
z=0
w=0
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
#quantity_alf = [x,y,z,w]
quantity_alf = {'x': x, 'y': y, 'z': z, 'w': w, 'A':A ,'B':B,'C':C,'D':D,'E':E,'F':F}

#def xor(str1, str2):
    #return int(bool(str1) != bool(str2))
from itertools import product

def stro(): #преобразует введенную строку
    ss=''
    for s in l_s:
        nn = ch.index(s)
        v = ch_p[nn]
        if v=='': v=v
        ss+= v
        ss+= ' '
    ss = ss[:-1]
    return ss

def str_fun(right_ls): #переводит введенную строку в функйию
    return int(eval(right_ls))

def values(l_s):
    global quantity, variables
    l_values = []
    variables = set()
    for s in l_s:
        if s in alf:
            variables.add(s)
    quantity = len(variables) #кол-во различных переменных
    variables = sorted(list(variables))
    for i in product('01', repeat=quantity):
        l_values.append(list(i)) #список списков ['0', '0', '0'] всех возможных комбинаций значений
    
    return l_values





#старт
print('берите выражения с and и not в скобки ')
l_s = input('введите лог выражение (НАПРИМЕР (x∧y)⊕z) - ') #(x∧y)⊕z   x⇔((y∧z)&w)
print(' ТАБЛИЦА ИСТИННОСТИ ')
print()

# получаем правильный вид введенной записи
right_ls = stro()
#надо получить значения переменных
val = values(l_s) #список списков ['0', '0', '0'] всех возможных комбинаций значений 
#оформление
print(*variables, sep = '   ', end = '')
print('  ', l_s)
for j in range(len(val)):
    for sj in range(quantity):
        #variables[sj] = eval(variables[sj],int(val[j][js]))
        quantity_alf[variables[sj]] = int(val[j][sj])
    x = quantity_alf['x']
    y = quantity_alf['y']
    z = quantity_alf['z']
    w = quantity_alf['w']
    A = quantity_alf['A']
    B = quantity_alf['B']
    C = quantity_alf['C']
    D = quantity_alf['D']
    E = quantity_alf['E']
    F = quantity_alf['F']
        
    for ii in range(quantity):
        print(quantity_alf[variables[ii]], end= '   ')
    print('    ', int(eval(right_ls)))
            
    

