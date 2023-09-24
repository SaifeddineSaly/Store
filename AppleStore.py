#Python while loop is used to run a block code until a certain condition is met.

#The syntax of while loop is:

#while condition:
    # body of while loop

#    A while loop evaluates the condition
#    If the condition evaluates to True, the code inside the while loop is executed.
#    condition is evaluated again.
#    This process continues until the condition is False.
#    When condition evaluates to False, the loop stops.

####################################################################################

import random
import datetime

#add function to add user and pass to file
def generate():
        passlen = int (input(' Enter the length of the password ( > 6): '))
        while passlen > 6:
            if passlen > 6:
                s='abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
                p=''.join(random.sample(s,passlen ))
                print(' Password: '+p)
                break
            else:
                passlen = int (input(' Enter the length of the password: '))
        return p

def add():
    name = input(' \n Username: ')
    d = input (' Do you want to generate your password (yes/no): ').lower()
    while answer.lower() != 'yes' and answer.lower() != 'no':
        d = input(' Do you want to generate your password (yes/no): ').lower()
    if d == 'yes':
       pwd = generate()
    else:
        pwd = input(' Password: ')
    with open('password.txt', 'a') as f:
        f.write(name + ' | ' + pwd + '\n')
        f.close()
    return name


def verify():
    count = 0
    #flag = 0
    while count != 3: 
        username = input(' Username: ').lower()
        password = input(' Password: ').lower()
        with open('password.txt','r') as f: ## reading from file
            for line in f.readlines():
                data = line.strip()
                user, passw = data.split('|')
                user_n = user.strip()
                passw_n = passw.strip()
                if username == user_n and password == passw_n :
                    return username
                    #flag = 1
                #print('User:', user.capitalize(), 'Password:', passw)
            #if flag == 1:
                #return username
                #break
        count = count + 1

###############################################################################

### partie 1 ###

greeting = [' Hello', ' Bonjour', ' Hi', ' Welcome', ' Hola']
random_greeting = random.choice(greeting)
print("\n "+random_greeting)
print(' -----------------------------------')

answer = input(' Do you have an account (yes/no)? ').lower()
while answer.lower() != 'yes' and answer.lower() != 'no':
    answer = input(' Do you have an account (yes/no)? ').lower()
    
if answer == 'yes':
     custumor = verify()   
else:
    custumor = add()


print('\n Welcome '+ custumor.capitalize() +' to our Apple Store\n')
print(' +-----------------------------+')
print(' | This is our products:       |')
print(' +-----------------------------+')
print(' | Headphone    :        150$  | ')
print(' | Phones       :        200$  | ')
print(' | Laptop       :        320$  | ')
print(' | Airpod       :        110$  | ')
print(' | Airtag       :        100$  | ')
print(' +-----------------------------+')

prices={'headphone' : 150 ,'phone' : 200, 'laptop' : 320 ,'airpod' : 110,'airtag': 100 }
pricess={'headphone' : 'headphone' ,'phone' : 'phone    ','laptop' : 'laptop   ','airpod' : 'airpod   ','airtag' : 'airtag   '}

### fin - partie 1 ###

### partie 2 ###
global total

total = 0

while True:
    try:
        prod_num=input('\n How many item you want to buy: ')
        prod_num=int(prod_num)
        break
    except Exception: 
        print(' \nPlease enter a number!')
        
with open('facture.txt', 'w') as f:
    for i in range(prod_num):
        choosen = input('\n What you want to buy: ').lower()
        while not choosen in ['headphone', 'phone', 'laptop', 'airpod', 'airtag']:
            choosen = input(' What you want to buy: ').lower()
        while True:
            try:
                quant = input(' Quantity: ')
                quant = int(quant)
                break
            except Exception:
                print(' Please enter a number!')
                
        p = quant*prices[choosen]
        total+=p
        
        if p >= 1000:
            f.write(' | ' + pricess[choosen].capitalize() +'        '+ str(quant) +'       '+ str(p) + '$' + '  |' +'\n')
        else:
            f.write(' | ' + pricess[choosen].capitalize() +'        '+ str(quant) +'        '+ str(p) + '$' + '  |' +'\n')
        #with open('facture.txt', 'a') as f:
        #f.write(' | ' + choosen.capitalize() +'        '+ str(quant) +'        '+ str(p) + '$' + '      |' +'\n')
        #print(choosen.capitalize() +'        '+ str(quant) +'        '+ str(p) + '$')

### finish - partie 2 ###

### partie 3 ###
        
print('\n ------------------------------------')
print('\n Here\'s your invoice : ')
print(' +---------------------------------+')
print(' | Invoice              ' + str(datetime.datetime.today().date()) + ' |')
print(' +---------------------------------+')
with open('facture.txt','r') as f:
    for line in f.readlines():
        data = line.rstrip()
        print(data)
        
        #print(choosen.capitalize() +'        '+ str(quant) +'        '+ str(p) + '$')
print(' +---------------------------------+')        
if total >= 1000:
    print(' | The total                '+ str(total) +'$' + '  |')
else:
    print(' | The total                 '+ str(total) +'$' + '  |')
print(' |                                 |')
print(' | And thank you for buying from   |')
print(' | our store. Have a nice day :)   |')
print(' +---------------------------------+')