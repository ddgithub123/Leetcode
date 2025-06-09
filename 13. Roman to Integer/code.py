class Solution:
    def romanToInt(self, s: str) -> int:
            #dictionary to maintain roman numerals
            roman={
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
            }
            value = 0
            for idx in range(len(s)-1, -1, -1):      #reverse traversing of the roman numeral string
                if idx == len(s)-1:                  #if the idx value is the last value
                    value += roman[s[idx]]
                    
                elif roman[s[idx]]< roman[s[idx+1]]:    #if cases like IV, XL, IX occur where ith term is lesser than the (i+1)th term
                    value -= roman[s[idx]]
                    
                else:                                #adding all the other values by mapping to the values in the dictionary
                    value += roman[s[idx]]

            return value
