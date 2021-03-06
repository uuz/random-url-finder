import httpx, string, os, platform
from time import sleep
from threading import Thread
from random import choice, randint

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        print()
        os.system('clear')

ASK = "\033[1;37;40m[\033[1;36;40m?\033[1;37;40m]"
BANNER = "\033[1;37;40m[\x1b[35m#\x1b[39m]\033[1;37;40m"
INFO = "\033[1;37;40m[\033[1;32;40m!\033[1;37;40m]"
SUCCESS = "\033[1;37;40m[\033[1;32;40m+\033[1;37;40m]"
GREEN = "\033[1;92;40m"
WHITE = "\033[1;37;40m"
BLUE = "\033[1;90;40m"
BLUE2 = "\033[1;36;40m"
YELLOW = "\033[1;93;40m"
RED = "\033[1;31;40m"

domains = ['.com', '.co', '.ml', '.ru', '.de', '.tk', '.io', '.gg', '.cf', '.ga', '.xyz']
done = 0
skipped = 0
error = 0
def find():
    global done, domains, skipped, error, rng1, rng2
    while True:
        try:
            pool = string.ascii_lowercase+string.digits
            pool  = ''.join(choice(pool)  for _ in range(randint(int(rng1), int(rng2))))
            domain = choice(domains)
            response = httpx.get(url='http://' + pool + domain)
            if response.text == '' or 'available' in response.text or 'for sale' in response.text or 'domain.dot.tk' in response.text or response.status_code == 0 or response.status_code == 403 or response.status_code == 400 or response.status_code == 404 or response.status_code == 503 or response.status_code == 525:
                skipped += 1
            else:
                done += 1
                success = open("found.txt", "a")
                success.write(f"http://{pool}\n")
                success.close()
        except Exception as w:
            error += 1
            find()

def ip():
    global done, skipped, error
    while True:
        try:
            a = str(randint(1,255))
            b = str(randint(1,255))
            c = str(randint(1,255))
            d = str(randint(1,255))
            pool = "{}.{}.{}.{}".format(a,b,c,d)
            response = httpx.get(url='http://' + pool)
            if response.text == '' or 'available' in response.text or 'for sale' in response.text or 'domain.dot.tk' in response.text or response.status_code == 0 or response.status_code == 403 or response.status_code == 400 or response.status_code == 404 or response.status_code == 503 or response.status_code == 525:
                skipped += 1
            else:
                done += 1
                success = open("found.txt", "a")
                success.write(f"http://{pool}\n")
                success.close()
        except Exception as w:
            error += 1
            ip()

clear()
print(f'{BANNER} Falling Random Url Finder\n')
print(f'{INFO} Select mode\n')
print(f'[{BLUE2}1{WHITE}] Random between range\n[{BLUE2}2{WHITE}] Random IP\n')
mode = input(f"{ASK} Mode: ")
while mode == '' or int(mode) <= 0 or int(mode) > 2:
    mode = input(f"{ASK} Please enter a valid mode: ")
if mode == '1':
    print(f'\n{INFO} Define range\n')
    rng1 = input(f"{ASK} Minimum lenght: ")
    rng2 = input(f"\n{ASK} Maximum lenght: ")
    while rng1 == '' or rng2 == '' or rng1 == rng2 or int(rng1) < 0 or int(rng2) < 0 or int(rng1) > int(rng2):
        print(f"\n{INFO} Please, enter a valid range!\n")
        rng1 = input(f"{ASK} Minimum lenght: ")
        rng2 = input(f"\n{ASK} Maximum lenght: ")
    thrds = input(f"{ASK} Threads: ")
    for i in range(int(thrds)):
        thread = Thread(target=find)
        thread.setDaemon(True)
        thread.start()
    print("\n{} All threads successfully initialized.\n".format(SUCCESS))
else:
    thrds = input(f"\n{ASK} Threads: ")
    for i in range(int(thrds)):
        thread = Thread(target=ip)
        thread.setDaemon(True)
        thread.start()
    print("\n{} All threads successfully initialized.\n".format(SUCCESS))


while True:
    for spinner in ['.  ', '.. ', '...', ' ..', '  .', '   ']:
        print('{}[{}{}{}] Found: {}{:,}{} | Skipped: {}{:,}{} | Fail: {}{:,}{}'.format(WHITE, RED, spinner, WHITE, GREEN, done, WHITE, BLUE, skipped, WHITE, YELLOW, error, WHITE), end=" \r")
        sleep(.25)
