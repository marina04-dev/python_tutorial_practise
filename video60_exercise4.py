symboloseira ="bcgdvcgdvchsbchsbcjdbcjdbcjdbcdhvbdhvdhvdcdh   cjbjdvbdbjdvb   dvjdbvdfbvuvdf dfhowowdidvd  cndvifvhidfnvdjvn  dfndkvnivndvndj"
print(symboloseira)
my_list = list(symboloseira)
print(my_list)

chars = {}
for char in my_list:
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1
    
print(chars)

max_value = max(chars.values())
print(max(chars.values()))

for key,value in chars.items():
    if value == max_value:
        print(key)
