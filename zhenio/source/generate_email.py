import pyautogui
import sys
import time
import random
import string

ret_names = []

def msg(
        _option_,
        _message_
        ):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')

# Exiting function
def ext():
    msg(1,'Exiting...')
    sys.exit()

def read_names():
    msg(1,'Reading names...')
    names = open('./data/orignal_email_names.txt', 'r').read().splitlines()
    random.shuffle(names)
    return names

def generate_email(names):
    msg(1,'enerating email...')
    pyautogui.hotkey('alt', 'tab')
    # time.sleep(1)

    for i in range(200, 1000):
        # _new_ = pyautogui.locateOnScreen('images/new_email.png')
        # formx, formy = pyautogui.center(_new_)
        formx, formy = 602, 444
        # pyautogui.moveTo(formx, formy)
        # time.sleep(1)
        pyautogui.click(formx, formy)
        # print(formx, formy)

        time.sleep(1)

        # _input_ = pyautogui.locateOnScreen('images/input.png')
        # formx, formy = pyautogui.center(_input_)
        # formx, formy = 700, 510
        # time.sleep(2)

        # pyautogui.click(formx, formy)

        name = names[i]+(str)(random.randint(0,1000))
        ret_names.append(name)
        with open('./data/all_names_zhencrazy.txt', 'a') as f:
            f.write("%s@h0tma11.uu.me\n" % name)

        pyautogui.typewrite(name)

        time.sleep(1)

        # _confirm_ = pyautogui.locateOnScreen('images/confirm.png')
        # formx, formy = pyautogui.center(_confirm_)
        formx, formy = 1064, 526
        pyautogui.click(formx, formy)
        # print(formx, formy)

        time.sleep(5)





    # email = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

if __name__ == '__main__':
    msg(1,'Starting...')
    names = read_names()

    if generate_email(names) :
        msg(3,'Failed to execute "generate_email" command.')
        ext()

    ext()

    print(ret_names)
