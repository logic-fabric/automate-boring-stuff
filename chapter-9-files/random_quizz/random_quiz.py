"""Implement functions to generate, from a list of Q/A, random quizzes and the related lists of answers.
Each generated quizz and each related list of answers wille be a text file.
"""

from random import shuffle

from quizz_questions import QUIZZ_QUESTIONS


def create_quizz_file(quizz_index, qa_list):
    filename = f"quizz-{quizz_index}.txt"
    
    with open(filename, 'w') as f:
        for i, question_answer in enumerate(qa_list):
            question = question_answer['question']
            f.write(f"{i + 1}. {question}\n")

def create_answers_file(quizz_index, qa_list):
    filename = f"quizz_answers-{quizz_index}.txt"
    
    with open(filename, 'w') as f:
        for i, question_answer in enumerate(qa_list):
            answer = question_answer['answer']
            f.write(f"{i + 1}. {answer}\n")

def create_all_quizzes(qa_list, number_of_quizz):
    for quizz_index in range(1, number_of_quizz + 1):
        shuffle(qa_list)
        create_quizz_file(quizz_index, qa_list)
        create_answers_file(quizz_index, qa_list)


if __name__ == '__main__':
    create_all_quizzes(QUIZZ_QUESTIONS, 5)
