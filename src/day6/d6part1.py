import read_input_file


def number_of_unique_answers_per_group(answers):
    '''Number of unique answers to the questions for the group. Each line in the array of answers are those from a single person, so a group's answers look like this: ['abc', 'agh']...'''
    return 0


def total_number_of_unique_answers(all_group_answers):
    '''Total number of unique answers by group'''
    return 0


if __name__ == '__main__':
    lines = read_input_file.read(
        '/Users/jondarrer/Code/advent-of-code-2020/src/input/day6.txt')
    print(total_number_of_unique_answers(lines))
