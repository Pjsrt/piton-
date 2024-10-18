s1 = open('денги.txt','r',encoding='utf-8')
text = s1.read()
s2 = input('Сколько денег зароботал человек?')
print('У него ', int(text) + int(s2),'рублей')
s1.close()








