def FV(PV,i,n):
    print('本利和: '+'{:,}'.format(round(PV*(1+i*0.01)**n)))

P=input('請輸入本金:')
I=input('請輸入年利率%: ')
N=input('請輸入期數:')
FV(int(P),int(I),int(N))
