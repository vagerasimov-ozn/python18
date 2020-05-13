slovar = {'book':'книга','bear':'медведь'}

print(slovar['book'])
print(slovar['bear'])

books = {'name':['книга','книга2'],'year':[1990,2019]}

for i in range(len(books['name'])):
    print(books['name'][i])
    print(books['year'][i])


slovar['desk']='стол'
print(slovar)

user = {
    'id':1,
    'name':'Pavel',
    'surname':'Yakupov'
}

for key, user in user.items():
    print(key +": " + str(user))
    #print(user)