from textwrap import dedent
import sys

done_ordering = False
ORDER = dict()
WIDTH = 72
BANK = [
    {
        'category': 'Appetizers',
        'foods': ['Wings','Bees','Spring Rolls'],
    },
    {
        'category': 'Entrees',
        'foods': ['Fish','Chicken','Sawdust'],
    },
    {
        'category': 'Desserts',
        'foods': ['Chocolate','Cookies','Cake'],
    },
    {
        'category': 'Drinks',
        'foods': ['Water','Milk','Juice'],
    },
]
FOODS = [
  'Wings','Cookies','Spring Rolls',
  'Fish','Chicken','Sawdust',
  'Chocolate','Cookies','Cake',
  'Water','Milk','Juice'
]

def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to Snakes Cafe!'
    ln_two = 'Order from our menu options below'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}
        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
        {'*' * WIDTH}
    '''))

    for items in BANK:
      print('\n')
      print(items['category'])
      print('-' * len(items['category']))
      for foods in items['foods']:
        print(foods)

def take_order():
    """
    Function which prompt the user to input food
    """
    prompting = 'What would you like to order?'
    decor = len(prompting)
    print(dedent(f'''
        {'_' * decor}
        {prompting}
        {'Enter DONE to stop'}
        {'_' * decor}
    '''))  
    user_input = str(input())
    check_input(user_input)

def check_input(order):
    """
    Function which verify the food inputed exists on the menu and then will add it to the order
    until they input 'DONE'
    """
    if(order.split(' ')[0] == 'remove'):
            remove_item(order.split(' ')[1])
    for foods in FOODS:
        if (order == foods):
            if (order in ORDER):
                ORDER[order] += 1
                print(f'{ORDER[order]} orders of {order} added to your meal')
            else:
                ORDER[order] = 1 
                print(f'{ORDER[order]} order of {order} added to your meal')
        elif(order == 'DONE'):
            done_ordering = True
            return done_ordering
        



def remove_item(food):
    """
    Function which will remove the inputed item from the user's order 
    """
    if (food in ORDER):
      if (ORDER[food] == 1):
        del(ORDER[food])
        print(f'You now have zero orders of {food} on your meal')
      else:
        ORDER[food] -= 1  
        print(f'Removed 1 order of {food} from your meal. You now have {ORDER[food]} orders of {food} on your meal') 

def run():
    greeting()
    while done_ordering == False:
            take_order()

if __name__ == '__main__':
    run()