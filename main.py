import numpy as np
#zad1

# a = np.arange(20)
# print(a)
# j=2
# a[0]=4
#
# for i in range(1,len(a)):
#     a[i]=a[i-1]*2
#
# print(a)

#zad2
# a = np.arange(10, dtype='float')
# b = a.astype('int32')

#zad3


# def podnoszenie(rozmiar):
#     potega = 1
#     a = np.full((rozmiar,rozmiar),2)
#
#     for i in range(0,rozmiar):
#         for j in range(0,rozmiar):
#             a[i,j]**=potega
#             potega+=1
#
#     return(a)
#
# print(podnoszenie(5))

#zad4
liczby_lin = np.logspace(1,5,5)
print(liczby_lin)