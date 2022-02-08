# dictionary
word_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
# dictionary
digit_dict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


class calc_gcd():
    def to_num(self, str):
        # starting and ending pointer to get the substring from the input
        start = 0
        end = 0
        number = ""

        while(end < len(str)):
            # checking the substring is present or not if present then change it to the number
            if(word_dict.get(str[start:end+1])):
                number += word_dict.get(str[start:end+1])
                # moving to next character after finding substring
                start = end+1

            end += 1
        return number

    def gcd(self, x, y):
        if(y == 0):
            return x
        else:
            return self.gcd(y, x % y)

    def __init__(self, str1, str2):

        str1 = self.to_num(str1)
        str2 = self.to_num(str2)
        result = str(self.gcd(int(str1), int(str2)))
        answer = ''
        # converting number into the string
        i = 0
        while i < len(result):
            answer += digit_dict.get(result[i])
            i += 1
        print("Output:", answer)
        # function to find GCD

        # function to convert string input into the number


# taking the inputs
str1 = input('Input 1 : ')
str2 = input('Input 2 : ')
obj = calc_gcd(str1, str2)
