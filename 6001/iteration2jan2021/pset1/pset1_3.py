s = 'azcbobobegghakl'
est = ''
lamba = ''
last = ''
for letter in s:
    
    
    if letter >= last:
        lamba += letter
    elif len(lamba) > len(est):
        est = lamba
    else:
        lamba = letter
        
    
    last = letter
    
    if len(lamba) > len(est):
        est = lamba
 
print("Longest substring in alphabetical order is:", est)
