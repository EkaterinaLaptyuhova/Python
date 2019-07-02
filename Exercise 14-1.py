def sed(pattern_word, replacement_word, file_input, file_output):
    try:
        in_file = open(file_input)
        out_file = open(file_output, 'w')

        for line in in_file:
            for word in line.split():
                if word == pattern_word:
                    out_file.write(replacement_word + ' ')
                else:
                    out_file.write(word + ' ')
    except:
        print('Something went wrong.')



sed('трудозатрат', 'ОК', 'input.txt', 'output.txt')
