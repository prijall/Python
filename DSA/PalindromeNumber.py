class Solution:
    def checkPalindrome(self):

        x=int(input('Enter the value of x:'))
        
        if x < 0:
            print('[WARNING]the number cannot be for palindrome check')
            return

        reverse_val=0
        temp=x
       
        while temp!=0:
            digit=temp % 10
            reverse_val=reverse_val * 10 + digit
            temp //=10
       
        
        if x==reverse_val:
            print('The number is palindrome')
        else:
            print('The number is not palindrome')
               

# Object Creation:
s=Solution()
s.checkPalindrome()