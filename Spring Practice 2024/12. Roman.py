class Solution:
    def subtract_tl(self, num, romanletter, srl, subnum, roman):
        if num >= (subnum):
            num -= (subnum)
            roman = roman + srl + romanletter 
            print(roman)
            print(num)
        return num, roman

    def subtract_gen(self, num, romanletter, subnum, roman):
        while num >= (subnum):
            num -= (subnum)
            roman = roman + romanletter
        return num, roman

    def intToRoman(self, num: int) -> str:
        roman = ""
        num, roman = self.subtract_gen(num, "M", 1000, roman)
        num, roman = self.subtract_tl(num, "M", "C", 900, roman)
        num, roman = self.subtract_gen(num, "D", 500, roman)
        num, roman = self.subtract_tl(num, "D", "C", 400, roman)
        num, roman = self.subtract_gen(num, "C", 100, roman)
        num, roman = self.subtract_tl(num, "C", "X", 90, roman)
        num, roman = self.subtract_gen(num, "L", 50, roman)
        num, roman = self.subtract_tl(num, "L", "X", 40, roman)
        num, roman = self.subtract_gen(num, "X", 10, roman)
        num, roman = self.subtract_tl(num, "X", "I", 9, roman)
        num, roman = self.subtract_gen(num, "V", 5, roman)
        num, roman = self.subtract_tl(num, "V", "I", 4, roman)
        num, roman = self.subtract_gen(num, "I", 1, roman)
        print(num)
        return(roman)
            
# Better solution
# class Solution:
    # def intToRoman(self, num: int) -> str:
    #     # Creating Dictionary for Lookup
    #     num_map = {
    #         1: "I",
    #         5: "V",    4: "IV",
    #         10: "X",   9: "IX",
    #         50: "L",   40: "XL",
    #         100: "C",  90: "XC",
    #         500: "D",  400: "CD",
    #         1000: "M", 900: "CM",
    #     }
        
    #     # Result Variable
    #     r = ''
        
        
    #     for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
    #         # If n in list then add the roman value to result variable
    #         while n <= num:
    #             r += num_map[n]
    #             num-=n
    #     return r

# Improvements: only one function, uses dictionary to automatically use one number with correct roman numeral.
# My two functions couldve been combined into one function