print('Кирпич стоит:30 рублей за штуку, килограмм цемента стоит:130, килограмм песка стоит:100')
print('получаеся....')
y = open('кирпич.txt','r',encoding='utf-8')
text1 = y.read()
r = open('цемент.txt','r',encoding='utf-8')
text2 = r.read()
p = open('песок.txt','r',encoding='utf-8')
text3 = p.read()
a = (int(text1)*200)+(int(text2)*3)+(int(text3)*5)
print('Вам это всё обойдётся в',a,"рублей.")















