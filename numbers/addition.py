#!/usr/bin/env python3

from general_test import GeneralTest

class TestAddition(GeneralTest):
    def handle_question(self,num1,num2,prefix=''):
        
        print("{0}{1}+{2}=".format(prefix,num1,num2),end='')
        good_result = num1 + num2
        your_result = 0
        try:
            text = input()
            your_result = int(text)
            if your_result == good_result:
                return (True,your_result)
        except:
            pass

        info_text = "{0}+{1}={2} not {3}".format(num1,num2,good_result,text)

        return (False,info_text)


def main():
    print("Enter your name:",end='')
    name = input()
    number_of_challenges = 10
    max_value = 20
    t = TestAddition(name,number_of_challenges,max_value)
    t.start()

if __name__ == "__main__":
    main()
