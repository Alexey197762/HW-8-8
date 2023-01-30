Espresso=(1,0,0)

Capuchino=(1,3,0)

Maciato=(2,1,0)

Viena=(1,0,2)

LateMak=(1,2,1)

ConPanna=(1,0,1)

mss=(ConPanna, LateMak, Viena, Maciato, Capuchino, Espresso)  

mssName=('Кон Панна', 'Латте Маккиато', 'по-венски', 'Маккиато', 'Капучино', 'Эспрессо ')

coff, milk, sl = map(int, input('Введите количество кофе_молока_сливок: ').split() )

def choose_coffee(ind, var, preference0, preference1, preference2):

 if ((mss[ind][0] <= preference0) and (mss[ind][1]<=preference1) and (mss[ind][2]<=preference2)):

     preference0 = preference0 - mss[ind][0]

     preference1 = preference1 - mss[ind][1]

     preference2 = preference2 - mss[ind][2]

     print(mssName[ind])

     var += 1  

 ind += 1

 if  ind<6:

   choose_coffee(ind, var, preference0 , preference1, preference2)

 if (var==0)and(ind==6):

   print('Вариантов нет')  

   exit

choose_coffee(0, 0, coff, milk, sl)