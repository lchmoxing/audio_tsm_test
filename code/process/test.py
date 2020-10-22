
def intersec(str1, str2):
    count_char = 0
    str_tmp = ''
    str1_tmp = str1
    str2_tmp = str2
    for i in str1_tmp:
        if i in str2_tmp:
            str_tmp = ''.join([str_tmp, i])
            str2_tmp = str2_tmp.replace(i,'',1)
        else:
            count_char = count_char+1
    return str_tmp,count_char

str1 = 'i\'ve been watching them all night'
str2 = 'i\'ve been watching tv all night'

result = intersec(str1,str2)
print(result)

# str3 = str2.replace('i','',1)
# print(str3)