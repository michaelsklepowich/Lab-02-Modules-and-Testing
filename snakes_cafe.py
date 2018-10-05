from textwrap import dedent
import sys
import uuid

ORDER = {
        'price': 0, 
        'order_id': uuid.uuid4()
        }
WIDTH = 72
BANK = [
    {
        'category': 'Appetizers',
        'foods': ['Wings','Bees','Spring Rolls', 'Grass', 'Sea Water', 'Tacos'],
    },
    {
        'category': 'Entrees',
        'foods': ['Fish','Chicken','Sawdust', 'Relish', 'Tomatoes', 'Popcorn'],
    },
    {
        'category': 'Desserts',
        'foods': ['Ice Cream','Cookies','Cake', 'Ranch', 'Eggs', 'Yogurt'],
    },
    {
        'category': 'Drinks',
        'foods': ['Water','Milk','Juice', 'Wine', 'Gatorade', 'Vodka'],
    },
    {
        'category': 'Sides',
        'foods': ['Snakes', 'Mustard', 'Cheese', 'Bananas', 'Grapes', 'Apples']
    }
]
FOODS = {
  'wings': 4.99,
  'bees': 2.99,
  'spring rolls': 4.99,
  'grass': 3.99,
  'sea water': 3.99,
  'tacos': 4.99,
  'fish': 6.99,
  'chicken': 6.99,
  'sawdust': 7.99,
  'relish': 2.99,
  'tomatoes': 4.99,
  'popcorn': 5.99,
  'ice cream': 3.99,
  'cookies': 3.99,
  'cake': 6.99,
  'ranch': 1.99,
  'eggs': 2.99,
  'yogurt': 2.99,
  'water': 0.99,
  'milk': 1.99,
  'juice': 2.99,
  'wine': 7.99,
  'gatorade': 2.99,
  'vodka': 6.99,
  'snakes': 5.99,
  'mustard': 2.99,
  'cheese': 1.99,
  'bananas': 1.99,
  'grapes': 2.99,
  'apples': 2.99,
}

# SIDES = [
#     {
#         'green': 1.99,
#         'red': 2.99,
#         'blue': 3.99,
#         'orange': 4.99,
#         'purple': 5.99,
#         'yellow': 6.99,
#     }
# ]

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
    Function which prompts the user to input food or done
    """
    done_ordering = False

    while done_ordering == False:
        prompting = 'What would you like to order?'
        decor = len(prompting)
        print(dedent(f'''
            {'_' * decor}
            {prompting}
            {'Enter DONE to stop'}
            {'_' * decor}
        '''))  
        user_input = str(input())
        if user_input.lower() == 'done':
            print('\nThanks for ordering!\n') 
            done_ordering = True
        elif user_input.lower() == 'order':
            if ORDER == {}:
                print('\nYou haven\'t ordered anything')
            else:    
                print_order()

        else:
            check_input(user_input)
    
def print_order():
    """Seperate function for printing the items in the users order"""
    
    print('The Snakes Cafe')
    print('Order: ', ORDER['order_id'])

    print(dedent(f'''
        {'=' * WIDTH}
    '''))
    dots = '.' * WIDTH

    for indv_food in ORDER:
        if indv_food in FOODS:
          print(f'\n{indv_food} x{ORDER[indv_food]}{dots[0:(WIDTH -4 - len(indv_food) - len(str(FOODS[indv_food])))]} {FOODS[indv_food]}')

    b = ORDER['price']
    print('\nSubtotal:', "%.2f" % b)
    a = ORDER['price'] * 0.096
    print('\nSales Tax:', "%.2f" % a)
    float_fix = str(ORDER['price'] + a)[0:5] 
    print ('----------')
    print('\nTotal Due:', f'${float_fix}')
   
def check_input(order):
    """
    Function which verify the food inputed exists on the menu and then will add it to the order
    """
    order = order.lower()
    for categories in BANK:
        if (order == categories['category'].lower()):
            print(categories['category'].upper())
            for i in categories['foods']: 
                    print('- ' , i)
    if order == 'menu':
        print_menu()                
    for foods in FOODS:
        if (order == foods.lower()):
            if (order in ORDER):
                ORDER[order] += 1
                ORDER['price'] = ORDER['price'] + FOODS[order.lower()]
                print(f'{ORDER[order]} orders of {order} added to your meal')
                float_fix = str(ORDER['price'])[0:5]
                print(f'Total: ${float_fix}') 
            else:
                ORDER[order] = 1 
                ORDER['price'] = ORDER['price'] + FOODS[order.lower()]
                print(f'{ORDER[order]} order of {order} added to your meal')    
                float_fix = str(ORDER['price'])[0:5]
                print(f'Total: ${float_fix}')     



def remove_item(food):
    """
    Function which will remove the inputed item from the user's order 
    """
    if (food in ORDER):
      if (ORDER[food] == 1):
        del(ORDER[food])
        ORDER['price'] = ORDER['price'] - FOODS[food.lower()]
        print(f'You now have zero orders of {food} on your meal')
        float_fix = str(ORDER['price'])[0:5]
        print(f'Total: ${float_fix}')  
      else:
        ORDER[food] -= 1  
        ORDER['price'] = ORDER['price'] - FOODS[food.lower()]
        print(f'Removed 1 order of {food} from your meal. You now have {ORDER[food]} orders of {food} on your meal') 
        float_fix = str(ORDER['price'])[0:5]
        print(f'Total: ${float_fix}')  

def print_menu():
    """prints the menu to the console"""
    print('MENU')
    for categories in BANK:
            print(categories['category'].upper())
            for i in categories['foods']: 
                    print('- ' , i)

  
def run():
    """
    calls the other functions
    """
    greeting()
    take_order()

if __name__ == '__main__':
    run()

