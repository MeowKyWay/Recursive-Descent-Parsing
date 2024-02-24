def recursive(iterator):
    print("iterator: ", iterator)
    if(input()=="return"):
        return
    recursive(iterator+1)
    print(iterator)
    
    return
    
recursive(0)