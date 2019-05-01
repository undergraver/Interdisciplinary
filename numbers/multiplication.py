#!/usr/bin/env python3

from general_test import GeneralTest

class TestMultiplication(GeneralTest):
    def handle_question(self,num1,num2):

        print("{0}*{1}=".format(num1,num2),end='')

        try:
            result = int(input())
            if result == num1 * num2:
                return True
        except:
            pass
        
        return False


def main():
    print("Enter your name:",end='')
    name = input()
    number_of_challenges = 10
    max_value = 10
    t = TestMultiplication(name,number_of_challenges,max_value)
    t.start()

if __name__ == "__main__":
    main()
