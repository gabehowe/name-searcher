import os
import re


def main():
    trimmed_list = []
    with open('./resources/wordlist.txt') as file:
        file_contents = file.readlines()
        for i in file_contents:
            if not re.match('^[a-zA-Z0-9_]{3,16}$', i):
                continue
            trimmed_list.append(i)
        file.close()
    if os.path.exists('./resources/trimmed_wordlist.txt'):
        with open('./resources/trimmed_wordlist.txt', 'w+') as file:
            file.writelines(trimmed_list)
            file.close()
    else:
        with open('./resources/trimmed_wordlist.txt', 'w+') as file:
            file.writelines(trimmed_list)
            file.close()


if __name__ == '__main__':
    main()
