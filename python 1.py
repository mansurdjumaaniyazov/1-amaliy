from datetime import datetime
bugun = datetime.now()
print(bugun.strftime('%d-%m-%y'))
      
dars_nomi = 'python'
maruza = 60
amaliy = 30
print(type(dars_nomi))
print(type(maruza))
print(type(amaliy))

a=5
b=4
c=a+b
print('natija',c)

a=input('birinchi soni kiriting:')
b=input('ikkinchi soni kiriting:')
c=int(a)+int(b)
print('Natija:',c)

a=input('birinchi soni a kiriting:')
b=input('ikkinchi soni b kiriting:')
c=a
a=b
b=c

print('a:',a,'b:',b)
