from functools import reduce
import read_input_file


def count_by_answer(answers, answer):
    if (answer in answers):
        answers[answer] += 1
    answers[answer] = 1
    return answers


def number_of_unique_answers_per_group(group_answers):
    '''Number of unique answers to the questions for the group. Each line in the array of answers are those from a single person, so a group's answers look like this: ['abc', 'agh']...'''
    # https://www.programiz.com/python-programming/methods/string/join
    # https://www.geeksforgeeks.org/python-dictionary-keys-method/#:~:text=keys()%20method%20in%20Python,the%20keys%20in%20the%20dictionary.&text=Parameters%3A%20There%20are%20no%20parameters,the%20changes%20in%20the%20dictionary.
    return len(reduce(count_by_answer, ''.join(group_answers), {}).keys())


def total_number_of_unique_answers_per_group(all_group_answers):
    '''Total number of unique answers by group'''
    return reduce(lambda count, group_answers: count + number_of_unique_answers_per_group(group_answers), all_group_answers, 0)


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day6.txt')
    print(total_number_of_unique_answers_per_group(lines))
