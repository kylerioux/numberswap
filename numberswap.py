import random
from pynput import keyboard

# generate a list of randomly sorted unique integers
def generateList(len):
    numbers = list(range(len))
    random.shuffle(numbers)
    return numbers

# check if numbers are in order
def orderCheck(numlist):
    #print('order check')

    numlist = numlist.copy()#[0]#.tolist()
    print(numlist)
    #print(type(numlist))
    #global user_initiated 
    for i, each in enumerate(numlist):
        if i == len(numlist)-1:
            # if user_initiated and user_initiated == True:
            #print("The numbers are in order!")
            return True
            
        if numlist[i]+1 != numlist[i+1]:
            return False

def on_press(key):
    global numlist
    if key == keyboard.Key.left:
        numlist =  numlist[1:]+[numlist[0]]
        exit()
    if key == keyboard.Key.right:
        numlist = [numlist[-1]] + numlist[:-1]
        exit()
    if str(key) == "'s'":
        numlist[0], numlist[1] = numlist[1], numlist[0]
        exit()
    if key == keyboard.Key.esc:
        exit()

def userInput():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def printList(numlist):
    visual = numlist.copy()
    #print('pList')
    # print(visual)
    visual.insert(0, '|')
    visual.insert(3, '|')
    print(*visual)
    
# main iteration loop
def iterator():
    global numlist
    while True:
        printList(numlist)
        if orderCheck(numlist) == True:
            return
        user_cmd = userInput()

# if this file is run directly, let the user play the game with keyboard controls
def main():
    global numlist
    # global user_initiated 
    # user_initiated = True
    print("Press left and right arrow keys to shift the numberline, press 's' to swap the numbers within: |x y|")
    
    numlist = generateList(5)   
    iterator()

if __name__== "__main__" :
    main()


