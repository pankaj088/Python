Q ="pankajprabhakar"
# index value print kariga

print(Q[2])
# slicing kariga yai bas index o se 4 tak hi kariga
print(Q[0:4])

# skip value print kariga
print(Q[0:15:2])
# 0 yani index 0 se strat hoga,:15 yani string ka length,:2 yani 2 kakr skip karna hai

print(len(Q)) 
# len() se string k akitna length hai oo print kariga

print(Q.count("a"))
# count ke help se Q ke ander kitne a hai

print(Q.capitalize())
# find() se hme pata chaliga ki h kitne number pai hai
print(Q.find("h"))

# replace() kar dega 
print(Q.replace("pankajprabhakar", "Birju"))