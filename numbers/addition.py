#!/usr/bin/env python3

import number_generator

class TestAddition():
    def __init__(self,name,num_challenges,max_value):
        self.name = name
        self.num_challenges = num_challenges
        self.max_value = max_value

    def start(self):
        text_lines = [ "Hello, {0}".format(self.name),
                       "Please answer the next {0} questions".format(self.num_challenges)
                     ]
        self.display_box_message("\n".join(text_lines))
        correct_answers = 0
        num_generator = number_generator.int_pair_generator(0,self.max_value,
                                                            0,self.max_value)
        for _ in range(self.num_challenges):
            num1, num2 = next(num_generator)
            print("{0}+{1}=".format(num1,num2),end='')
            try:
                result = int(input())
                if result == num1 + num2:
                    correct_answers+=1
            except:
                pass

        self.display_box_message(
                "Tudor scored {0} out of {1}".format(
                correct_answers,
                self.num_challenges)
        )

    def display_box_message(self,message):
        lines = message.split('\n')
        num_lines = len(lines)
        max_line_length = max(len(line) for line in lines)
        delimiter = "+"+max_line_length*"-"+"+"
        """
        +----------+
        |msg line 1|
        |msg below |
        +----------+
        """
        if num_lines > 0:
            print(delimiter)

            for line in lines:
                len_of_line = len(line)
                print("|"+line+(max_line_length-len_of_line)*' '+"|")

            print(delimiter)


def main():
    print("Enter your name:",end='')
    name = input()
    number_of_challenges = 20
    max_value = 20
    t = TestAddition(name,number_of_challenges,max_value)
    t.start()

if __name__ == "__main__":
    main()
