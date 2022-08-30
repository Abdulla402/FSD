code=int(input('enter the employ id'))
name=input('enter the name')
des=input('enter your des')
comp=input('enter your com')
sal=int(input('enter your sal'))
ta=sal*0.03
da=sal*0.2
har=sal*0.01
allowance=ta+da+har
pf=sal*0.2
it=sal*0.22
esi=sal*0.255
deduction=pf+it+esi
gross=sal+ta+da+har
nett=gross-pf-it-esi
print('code\t name\t desc\t comp\t sal\t gross\t deduction\t allowance\t nett\t')
print(code,'\t',name,'\t',des,'\t',sal,'\t',gross,'\t',deduction,'\t',allowance,'\t',nett)
