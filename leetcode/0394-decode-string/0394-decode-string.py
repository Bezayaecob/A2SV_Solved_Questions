class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch !="]":
                stack.append(ch)
            else:
                temp= ""
                while stack[-1] != "[":
                    temp= stack[-1] + temp
                    stack.pop()
                stack.pop()
                num= ""
                while stack and stack[-1].isdigit():
                    num= stack[-1] + num 
                    stack.pop()
                stack.append(temp*int(num))
                
        return "".join(stack)


            

                    
                
            
            
    
             
      
        




    
           
          
            
            
       