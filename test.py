from prettytable import PrettyTable
mark=PrettyTable()
field=[ 'name','Chinese','math','English']
person1=['xiaowang',83,65,98]
person2=['xiaohua',92,23,45]
person3=['xiaoli',96,81,85]
mark.field_names=field
mark.add_row(person1)
mark.add_row(person2)
mark.add_row(person3)

suc=[field,person1,person2,person3]
mark_match=[]
for i in range(1,4,1):
    print(suc[5][2])
print (mark[0][0])

a="a"
a=a+"1"
print (a)
if a == 'a1':
    print('success')
