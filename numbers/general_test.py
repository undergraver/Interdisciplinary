import number_generator

class GeneralTest():
    def __init__(self,name,num_challenges,max_value):
        self.name = name
        self.num_challenges = num_challenges
        self.max_value = max_value

    def handle_question(self,num1,num2,prefix=''):
        """
        This function handles the operation between num1 and num2.

        Return a (True,value) tuple if the answer is correct, value representing the value
                 (False,info) otherwise, info representing the information

        """
        raise NotImplementedError

    def start(self):
        text_lines = [ "Hello {0},".format(self.name),
                       "Please answer the next {0} questions".format(self.num_challenges)
                     ]
        self.display_box_message("\n".join(text_lines))
        correct_answers_count = 0
        wrong_answers = []
        num_generator = number_generator.int_pair_generator(0,self.max_value,
                                                            0,self.max_value)
        for id in range(self.num_challenges):
            num1, num2 = next(num_generator)
            prefix="Question {index}:".format(index=id+1)
            ok,info = self.handle_question(num1,num2,prefix)
            if ok:
                correct_answers_count += 1
            else:
                wrong_answers.append(info)

        for info in wrong_answers:
            print("Wrong answer: {0}".format(info))

        self.display_box_message(
                "{0} scored {1} out of {2}".format(
                self.name,
                correct_answers_count,
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
