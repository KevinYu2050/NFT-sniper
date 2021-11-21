#! python3

#   Author      : Stavros Grigoriou
#   Updated    : yungK1LL
#   GitHub      : https://github.com/unix121
#   GitHub      : https://github.com/blooditrix
#   Year        : 2018
#   Description : [Updated]Script that generates random Gmail account. Still stalls at phone verification.

import pyautogui
import pyperclip
import sys
import time
import random
import string

# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message
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


# Function used to open Firefox
def open_firefox():

    # Printing basic message
    msg(1,'Opening Firefox...')


    pyautogui.press('win')

    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('f')
    pyautogui.typewrite('i')
    pyautogui.typewrite('r')
    pyautogui.typewrite('e')
    pyautogui.typewrite('f')
    pyautogui.typewrite('o')
    time.sleep(1)



    pyautogui.press('enter')
    
    # Print message
    msg(1,'Firefox is now open and running.')

def load_zhenio():
    time.sleep(1)

    msg(1,'Locating Zhenio...')

    pyautogui.hotkey('ctrl','l')
    pyautogui.typewrite('https://www.zhen.io/register')
    pyautogui.press('enter')

    # pyautogui.press('tab')
 
    time.sleep(4)

    # _register_ = pyautogui.locateOnScreen('images/zhenio_new.png')
    # formx, formy = pyautogui.center(_register_)
    # print(formx, formy)
    formx, formy = 1074, 325
    pyautogui.click(formx, formy)
    pyautogui.click(formx, formy)

    pyautogui.moveTo(formx, formy)
    
    # Check and print message
    if not pyautogui.click(formx, formy):
        msg(1,'Located the form.')
    else:
        msg(3,'Failed to locate the form.')
        ext()

def write_info(email):
    time.sleep(1)
    # Type in registration form
    pyautogui.typewrite(email)
    # time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(email.strip('@0ut1OOk.uu.me'))
    # pyautogui.typewrite(email.strip('@h0tma11.uu.me'))
    # pyautogui.typewrite(email.strip('@0ut1ook.uu.me'))
    # pyautogui.typewrite(email.strip('@0ut1ook1.uu.me'))


    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('MjAxOWRjMGRjMWU4ZGUwYjQ4ZTdlNDAx')

    msg(1,'Filled out the form.')




    # Send verification code
    # _code_ = pyautogui.locateOnScreen('images/send_code.png')
    # formx, formy = pyautogui.center(_code_)

    # print(formx, formy)

    formx, formy = 1756, 487
    pyautogui.click(formx, formy)
    pyautogui.moveTo(formx, formy)
    time.sleep(1)
    msg(1,'Sent verification code.')



    # Change to Gmail
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

    # _auth_ = pyautogui.locateOnScreen('images/authentication.png')
    # formx, formy = pyautogui.center(_auth_)
    # print(formx, formy)
    time.sleep(8)
    formx, formy = 593, 310
    pyautogui.click(formx, formy)


    # Copy Verification Code
    # _code_ = pyautogui.locateOnScreen('images/verify_code.png')
    # formx, formy = pyautogui.center(_code_)
    # print(formx, formy)
    formx, formy = 1082, 855
    pyautogui.doubleClick(formx, formy)
    pyautogui.doubleClick(formx, formy)


    code = copy_clipboard()
    print(code)
    msg(1,'Copied verification code.')
    time.sleep(1)
    pyautogui.hotkey('alt', 'left')
    time.sleep(1)



    # Change back to register form
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

    # Type in registration form
    time.sleep(1)
    formx, formy = 1074, 480
    pyautogui.moveTo(formx, formy)
    pyautogui.click(formx, formy)
    pyautogui.typewrite(code)

    # sign up
    time.sleep(1)
    formx, formy = 1074, 680
    pyautogui.click(formx, formy)
    time.sleep(3)
    
    # pix = pyautogui.pixel(1074, 720)
    # pyautogui.moveTo(1074, 720)
    # print(pix)
    # if pix[0] != 255 and pix[1] != 255 and pix[2] != 255:
    #     msg(3,'Login failed')
    #     pyautogui.hotkey('ctrl','w')
    #     return

    with open('./data/used_names_zheniluvu.txt', 'a') as f:
        f.write("%s\n" % email)
    # with open('./data/used_names_zhenzheniluvu.txt', 'a') as f:
    #     f.write("%s\n" % email)

    # with open('./data/used_names.txt', 'a') as f:
    #     f.write("%s\n" % email)
    # with open('./data/used_names_zhencrazy.txt', 'a') as f:
    #     f.write("%s\n" % email)



    # Close Firefox
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('alt', 'tab')








    


def copy_clipboard():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()


def read_names(path):
    msg(1,'Reading names...')
    names = open(path, 'r').read().splitlines()
    return names

def register_email(email):
    msg(1,'Registering email {}...'.format(email))
    if open_firefox() :
        msg(3,'Failed to execute "open_firefox" command.')
        ext()

    if load_zhenio() :
        msg(3,'Failed to execute "load_zhenio" command.')
        ext()

    if write_info(email) :
        msg(3,'Failed to execute "write_info" command.')
        ext()

    msg(1,'Finished registering email {}...'.format(email))



# Main function
if __name__=='__main__':
    all_names = read_names('./data/all_names_zheniluvu.txt')  
    used_names = read_names('./data/used_names_zheniluvu.txt')  
    # all_names = read_names('./data/all_names.txt')  
    # used_names = read_names('./data/used_names.txt')  
    # all_names = read_names('./data/all_names_zhenzheniluvu.txt')  
    # used_names = read_names('./data/used_names_zhenzheniluvu.txt')  
    # all_names = read_names('./data/all_names_zhencrazy.txt')  
    # used_names = read_names('./data/used_names_zhencrazy.txt')  


    emails = list(set(all_names) - set(used_names))

    for email in emails: 
        register_email(email)

    msg(1,'Done...')
    ext()
