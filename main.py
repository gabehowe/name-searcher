import sys
import time
from typing import List
import colorama
import requests


def main():
    colorama.init()
    lines: List[str] = open('resources/trimmed_wordlist.txt').readlines()
    words = [word.removesuffix('\n') for word in lines]
    available_usernames = []
    with open('./resources/names.txt', 'w+') as file:
        file.truncate()
        file.close()
    for word in words:
        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{word}')
        if r.status_code == 429:
            print('too many requests! waiting 35 seconds...')
            time.sleep(35)
            print('resuming...')
            r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{word}')
        if r.status_code == 200:
            print(colorama.Fore.RED + word)
            continue
        if r.status_code == 204:
            available_usernames.append(word)
            print(colorama.Fore.GREEN + word)
            with open('./resources/names.txt', 'a+') as file:
                file.write(word + '\n')
                file.close()


if __name__ == '__main__':
    main()
