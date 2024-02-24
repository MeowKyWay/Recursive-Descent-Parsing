def backtrack(s, grammar, ite=[], index=0):
    if "".join(ite) == s:
        return True
    
    if (len(ite) == 0):
        return backtrack(s, grammar, [list(grammar.keys())[0]], index)
    
    if len(ite)<=index or len(s)<=index or len(ite)<=index:
        return False
    
    if ite[index] == s[index]:
        flag = backtrack(s, grammar, ite, index+1)
        if flag:
            return True
    
    if ite[index] in grammar:
        for word in grammar[ite[index]]:
            
            #bruh no string manipulation
            temp = ite.copy()
            temp.pop(index)
            for i in range(len(word)):
                temp.insert(index+i, word[i])
                
            #print("".join(temp)) #debugging
            
            flag = backtrack(s, grammar, temp, index)
            if flag:
                return True
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

if backtrack(s, grammar):
    print("String is accepted")
else:
    print("String is not accepted")