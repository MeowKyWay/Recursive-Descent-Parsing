def backtrack(s, grammar, ite=[], index=0):
    if "".join(ite) == s: #check if iterator is equal to string
        return True
    
    if (len(ite) == 0): #check if iterator is empty
        return backtrack(s, grammar, [list(grammar.keys())[0]], index)
    
    if len(ite)<=index or len(s)<=index or len(ite)<=index: #check if index is out of range
        return False
    
    if ite[index] == s[index]: #check if matching
        flag = backtrack(s, grammar, ite, index+1)
        if flag:
            return True
    
    if ite[index] in grammar: #check if non-terminal
        for word in grammar[ite[index]]: #iterate through the words
            temp = ite.copy()
            temp.pop(index)
            for i in range(len(word)):
                temp.insert(index+i, word[i])
                
            #print("".join(temp)) #debugging
            flag = backtrack(s, grammar, temp, index)
            if flag:
                return True
            
    #check if mismatch
    return False

n = int(input("Enter the number of grammar: "))

grammar = {}

for i in range(n):
    key = input("Enter the key: ")
    words = input("Enter the words: ").split("|")
    for j in range(len(words)):
        words[j] = words[j].strip()
    grammar[key] = words
        
s = input("Enter the string: ")

start = input("Enter the start symbol: ")

if backtrack(s, grammar, [*start]):
    print("String is accepted")
else:
    print("String is not accepted")