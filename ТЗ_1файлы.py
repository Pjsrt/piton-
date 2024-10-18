f = open('При.txt','r',encoding='utf-8')
text1 = f.read()
s = open('вет.txt','r',encoding='utf-8')
text2 = s.read()
print(text1 +text2)
f.close()
s.close()








