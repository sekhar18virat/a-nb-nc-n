 import itertools 
def isanbncn(s):
    for i in range(len(s)):                   #iterating characterby character
        if(s[i]!='a'):                        #check until a's are over
            break
    if(i==len(s) or i==0):                    #if i is equal to length of string or zero then return 0
        return 0
    elif(s[i]=='c'):                          #if c comes after b then return 0
        return 0
    
    else:
        for j in range(i,len(s)):             #iterating remaining characters where a's are over
            if(s[j]!='b'):                    #check until b's are over
                break
        if(j==(len(s)) or j==0):              #if no.of b's is equal to length of string or zero then return zero
            return 0
        elif(s[j]=='a'):                      #if a appear after b then return zero
            
            return 0
        
        else:
            for k in range(j,len(s)):          #iterating loops to check for c's
                if(s[k]!='c'):                 #if character isn't c then return 0
                    return 0
                    break
            if(k!=(len(s)-1) or k==0):         #check for the k value if it doesn't equal to length of string or if it equals zero return zero
                return 0
            else:
                return 1                       #this is reached if given string is off form a^nb^nc^n
  
s=input()                                          #taking string input
if(isanbncn(s)):                                   #calling isanbncn function to check
    print("given string is of form a^nb^nc^n",s)   #printing string if it satisfies property
else:
    print("string doesn't satisfy given property")