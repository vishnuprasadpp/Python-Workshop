name="vishnuprasad"
NAME={}
for letter in name:
  if letter in NAME:
    NAME[letter]=NAME[letter] +1
  else:
    NAME[letter]=1
print(NAME)

count_asofnow=0
most_occuring=""

for letter in NAME:
  if NAME[letter]>=count_asofnow:
    count_asofnow=NAME[letter]
    most_occuring=count_asofnow
print(most_occuring)

final={}
for letter in NAME:
  if NAME[letter]==count_asofnow:
    final[letter]=count_asofnow
print(final)
    
  
    

    
    



    
  


 
