Input="  Hello   World  "
list_words=[]
for each_value in Input.split():
    list_words.append(each_value[::-1])
print(" ".join(list_words))


