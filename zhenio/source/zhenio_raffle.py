import pyautogui
import pyperclip
import sys
import time
import random
import string

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
    time.sleep(3)

    msg(1,'Locating Zhenio...')

    pyautogui.hotkey('ctrl','l')
    pyautogui.typewrite('https://www.zhen.io/login')
    pyautogui.press('enter')

    # pyautogui.press('tab')
 
    time.sleep(3)

    # _register_ = pyautogui.locateOnScreen('images/zhenio_new.png')
    # formx, formy = pyautogui.center(_register_)
    # print(formx, formy)
    formx, formy = 1050, 330
    pyautogui.click(formx, formy)
    
    # Check and print message
    if not pyautogui.click(formx, formy):
        msg(1,'Located the form.')
    else:
        msg(3,'Failed to locate the form.')
        ext()

def login(email):
    time.sleep(2)
    pyautogui.typewrite(email)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('MjAxOWRjMGRjMWU4ZGUwYjQ4ZTdlNDAx')

    msg(1,'Filled out the form.')

    # login 
    formx, formy = 1050, 540
    pyautogui.click(formx, formy)

    time.sleep(2)

def raffle(email):
    msg(1,'Raffling...')
    pyautogui.hotkey('ctrl','l')
    pyautogui.typewrite('https://www.zhen.io/product?waresId=92&activityId=1&activitySubId=5')
    pyautogui.press('enter')
    time.sleep(2)


    formx, formy = 1700, 330
    # pyautogui.moveTo(formx, formy)
    # time.sleep(2)

    pyautogui.click(formx, formy)
    time.sleep(1)
    pyautogui.moveTo(1050, 710)

    # Check if loggedin in through color
    pix = pyautogui.pixel(1050, 710)
    # print(pix)
    if pix[0] == 255 and pix[1] == 255 and pix[2] == 255:
        msg(3,'Login failed')
        pyautogui.hotkey('ctrl','w')

        return


    time.sleep(7)


    pyautogui.hotkey('ctrl','l')
    pyautogui.typewrite('https://www.zhen.io/product?waresId=93&activityId=1&activitySubId=6')
    pyautogui.press('enter')
    time.sleep(2)
    formx, formy = 1700, 330
    # pyautogui.moveTo(formx, formy)
    # time.sleep(2)

    pyautogui.click(formx, formy)
    time.sleep(7)

    pyautogui.hotkey('ctrl','w')

    # with open('./data/raffled_names.txt', 'a') as f:
    #     f.write("%s\n" % email)
    # with open('./data/raffled_names_zhencrazy.txt', 'a') as f:
    #     f.write("%s\n" % email)
    # with open('./data/raffled_names_zhenzheniluvu.txt', 'a') as f:
    #     f.write("%s\n" % email)
    with open('./data/raffled_names_zheniluvu.txt', 'a') as f:
        f.write("%s\n" % email)







def process(email):
    msg(1,'Raffling for email{}...'.format(email))
    if open_firefox() :
        msg(3,'Failed to execute "open_firefox" command.')
        ext()

    if load_zhenio() :
        msg(3,'Failed to execute "load_zhenio" command.')
        ext()

    if login(email) :
        msg(3,'Failed to execute "login" command.')
        ext()
        

    if raffle(email) :
        msg(3,'Failed to execute "raffle" command.')
        ext()   

    msg(1,'Finished raffling for email {}...'.format(email))

def read_names(path):
    msg(1,'Reading names...')
    names = open(path, 'r').read().splitlines()
    return names


if __name__=='__main__':
    # all_names = read_names('./data/all_names.txt')  
    # raffled_names = read_names('./data/raffled_names.txt')  
    # all_names = read_names('./data/all_names_zhencrazy.txt')  
    # raffled_names = read_names('./data/raffled_names_zhencrazy.txt')
    # all_names = read_names('./data/all_names_zhenzheniluvu.txt')  
    # raffled_names = read_names('./data/raffled_names_zhenzheniluvu.txt')  
    all_names = read_names('./data/used_names_zheniluvu.txt')  
    raffled_names = read_names('./data/raffled_names_zheniluvu.txt')  

  

    emails = list(set(all_names) - set(raffled_names))

    for email in emails: 
        process(email)

    msg(1,'Done...')
    ext()
