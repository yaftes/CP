class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        i = 0
        while i < len(command):
            if command[i] == '(':
                if command[i+1] == ')':
                    s+='o'
                    i+=2
                else:
                    s+='al'
                    i+=4
            else:
                s+='G'
                i+=1
        return s
        