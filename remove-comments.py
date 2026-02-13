class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        current_line = ""

        for line in source:
            i = 0
            
            while i < len(line):
                
               
                if in_block:
                    if line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
                        
                
                else:
                    if line[i:i+2] == "//":
                        break 
                    elif line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                    else:
                        current_line += line[i]
                        i += 1
                        
            
            if not in_block and current_line:
                result.append(current_line)
                current_line = ""

        return result
