class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1,N2 = len(num1),len(num2)
        if N1<N2:
            N1,N2 = N2,N1
            num1,num2 = num2,num1
        carry = 0
        result =""
        for i in range(N1-1,-1,-1):
            digit1 = int(num1[i])
            digit2 = int(num2[i-N1+N2]) if i-N1+N2>=0 else 0
            result = str((digit1+digit2+carry)%10)+result
            carry = (digit1+digit2+carry)//10
        if carry>0:
            result = str(carry)+result
        return result

            



