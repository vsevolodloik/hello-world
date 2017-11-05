# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:39:08 2017

@author: Vsevolod Loik
"""

https://codereview.stackexchange.com/questions/133906/creating-a-questionnaire/133917#133917



question_list = [  # tuple of the form (question, answer list, correct answer list)
    ('What is the population of New Zealand ?',
    ['A:1830', 'B:1543', 'C:1642', 'D:1765'],
    ['D', 'd', '4.5', '4']),

    ('What year did the first european set foot on New Zealand (Abel Tasman) ?',
    ['A:1830', 'B:1543', 'C:1642', 'D:1765'],
    ['C', 'c', '1642', '3']),

    ('How many Kiwi are there left in New Zealand (Approx) ?',
    ['A:2000', 'B:600',  'C:70,000', 'D:100000'],
    ['D', 'd', '100000', '4']),

    ('How many new babys where born in New Zealand in 2015 ?',
    ['A:61,000', 'B:208,000', 'C:98,000', 'D:18,000'],
    ['D', 'd', '100000', '4']),
]

def questions():
    wrong = 0
    right = 0

    for each_question, each_answer, each_correct_answer in question_list:
        print(each_question + '\n' + ' '.join(each_answer))
        get_answer = raw_input()

        if get_answer in each_correct_answer:
            print('Your answer is correct!\n')
            right += 1
        else:
            print('That is not the answer I had in mind!\n')
            wrong += 1
        print('So far, you answered correctly to {0} questions and incorrectly to {1}. Good luck!'.format(right, wrong))


if __name__ == '__main__':
    questions()
    
    
###############################################################################
    
from random import shuffle

question_list = [  # tuple of the form (question, dict of answers)
    ('What is the population of New Zealand ?',
    {'6.7': False, '3.2': False, '5.1': False, '4.5': True}),

    ('What year did the first european set foot on New Zealand Abel Tasman ?',
    {'1830': False, '1543': False, '1765': False, '1642': True}),

    ('How many Kiwi are there left in New Zealand Approx ?',
    {'2000': False, '600': False,  '70,000': False, '100000': False, '100000': True}),

    ('How many new babys where born in New Zealand in 2015 ?',
    {'61,000': False, '208,000': False, '98,000': False, '18,000': True}),
]


def get_input_in_list(lst):
    while True:
        print("Please enter value from : " + " ".join(lst))
        user_input = raw_input()
        if user_input in lst:
            return user_input


def questions():
    wrong = 0
    right = 0

    for each_question, answer_dict in question_list:
        answers = list(answer_dict)
        shuffle(answers)
        print(each_question)
        user_answer = get_input_in_list(answers) 

        if answer_dict[user_answer]:
            print('Your answer is correct!\n')
            right += 1
        else:
            print('That is not the answer I had in mind!\n')
            wrong += 1
        print('So far, you answered correctly to {0} questions and incorrectly to {1}. Good luck!'.format(right, wrong))


if __name__ == '__main__':
    questions()