def FV(PV,i,n):
    print('本利和: '+'{:,}'.format(round(PV*(1+i*0.01)**n)))


P=input('請輸入本金:')
while str.isdigit(P)==False:
    print('請輸入數字!')
    P=input('請輸入本金:')
    if str.isdigit(P)==True:
        break

I=input('請輸入年利率%: ')
while str.isdigit(I)==False:
    print('請輸入數字!')
    I=input('請輸入年利率%: ')
    if str.isdigit(I)==True:
        break

N=input('請輸入期數:')
while str.isdigit(N)==False:
    print('請輸入數字!')
    N=input('請輸入期數:')
    if str.isdigit(N)==True:
        break

FV(int(P),int(I),int(N))
input();