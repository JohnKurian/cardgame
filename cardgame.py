import random


outdated_deck = []
num_cards_to_be_dealt = 5
total_num_cards = 50
cards = []
has_dice_rolled = False
god_spell_used = False
resurrect_spell_used = False
countered = False
is_CPU = False


class Player:

    def __init__(self, player_name, is_CPU):
        self.name = player_name
        self.is_CPU = is_CPU
        self.cards = []
        self.is_god_spell_available = True
        self.is_resurrect_spell_available = True
        self.player_number = 1
        self.points = 0
        self.has_next_move = False
        self.top_card_revealed = False
        self.top_card = {}
        print('player: ' + player_name + ' has been created.')

    def add_card_to_deck(self, card):
      self.cards.append(card)
      if len(self.cards) == 1:
        self.top_card = card

    def set_next_move_true(self):
      self.has_next_move = True

    def show_top_card(self):
      print(self.top_card)

    def remove_top_card(self):
      removed_card = self.top_card
      self.cards = self.cards[1:]
      try:
        self.top_card = self.cards[0]
      except IndexError:
        self.top_card = {}
        self.cards = []
      return removed_card


    def push_card_to_top(self, card_number):
      card_to_be_pushed = self.cards.pop(card_number)
      self.cards = [card_to_be_pushed] + self.cards
      self.top_card = card_to_be_pushed

    def use_resurrect_spell(self):
      try:
        if self.is_resurrect_spell_available:
          print('player '+ self.name + ' has used the resurrect spell.')
          print(outdated_deck)
          chosen_outdated_card_index = random.randint(0,len(outdated_deck)-1)
          self.cards = [outdated_deck[chosen_outdated_card_index]] + self.cards
          self.top_card = outdated_deck[chosen_outdated_card_index]
          del outdated_deck[chosen_outdated_card_index]
          print('the card obtained is:', self.top_card)
          self.is_resurrect_spell_available = False
          return True
        else:
          print('resurrect spell already used.')
          return False

      except ValueError:
        print('Cannot use the resurrect spell. No cards are there in the outdated deck.')
        return False

    def add_point(self):
      self.points += 1

    def show_cards(self):
      print(self.cards)

def roll_dice():
  roll_1 = random.randint(1,6)
  roll_2 = random.randint(1,6)
  print('player 1 rolled:', roll_1)
  print('player 2 rolled:', roll_2)
  if roll_1 > roll_2:
    print('player 1 goes first')
    player_one.set_next_move_true()
    return 1
  elif roll_1 == roll_2:
    print('both players rolled the same number. Rolling again..')
    roll_dice()
  else:
    print('player 2 goes first')
    player_two.set_next_move_true()
    return 2

def display_points():
  print('player one points: ', player_one.points)
  print('player two points: ', player_two.points)

def compare_top_cards(power_number):
  global god_spell_used
  global resurrect_spell_used
  
  if player_one.top_card['power_' + power_number] > player_two.top_card['power_' + power_number]:
    print('player one won the duel')
    player_one.add_point()
    player_one.has_next_move = True
    player_two.has_next_move = False
  else: 
    print('player two won the duel')
    player_two.add_point()
    player_one.has_next_move = False
    player_two.has_next_move = True
    
  print('the top card of player 1:', player_one.top_card)
  print('the top card of player 2:', player_two.top_card)
  
  print('adding to the outdated deck.')
  outdated_deck.append(player_one.remove_top_card())
  outdated_deck.append(player_two.remove_top_card())
  
  player_one.top_card_revealed = False
  player_two.top_card_revealed = False
  
  if god_spell_used:
    god_spell_used = False
  if resurrect_spell_used:
    resurrect_spell_used = False

def create_players(is_CPU):
  global player_one, player_two
  player_one = Player('one', False)
  if is_CPU:
    player_two = Player('two', True)
  else:
    player_two = Player('two', False)

def populate_deck():
  global cards
  cards = []
  power_0_chosen_cards = []
  power_1_chosen_cards = []
  power_2_chosen_cards = []
  power_3_chosen_cards = []
  
  for i in range(total_num_cards):
    character = {}
    character['character_name'] = 'character_' + str(i)
    character['power_0'] = random.choice([j for j in range(100) if j not in power_0_chosen_cards])
    power_0_chosen_cards.append(character['power_0'])
    character['power_1'] = random.choice([j for j in range(100) if j not in power_1_chosen_cards])
    power_1_chosen_cards.append(character['power_1'])
    character['power_2'] = random.choice([j for j in range(100) if j not in power_2_chosen_cards])
    power_2_chosen_cards.append(character['power_2'])
    character['power_3'] = random.choice([j for j in range(100) if j not in power_3_chosen_cards])
    power_3_chosen_cards.append(character['power_3'])
    cards.append(character)

def deal_cards_to_players():
  chosen_cards = []
  for i in range(2*num_cards_to_be_dealt):
    if i < num_cards_to_be_dealt:
      chosen_card_number = random.choice([j for j in range(total_num_cards) if j not in chosen_cards])
      player_one.add_card_to_deck(cards[chosen_card_number])
      chosen_cards.append(chosen_card_number)
    else:
      chosen_card_number = random.choice([j for j in range(total_num_cards) if j not in chosen_cards])
      player_two.add_card_to_deck(cards[chosen_card_number])
      chosen_cards.append(chosen_card_number)

def pick_resurrect():
  global outdated_deck
  if len(outdated_deck) > 0:
    power_0_list = []
    power_1_list = []
    power_2_list = []
    power_3_list = []

    for outdated_card in outdated_deck:
      power_0_list.append(outdated_card['power_0'])
      power_1_list.append(outdated_card['power_1'])
      power_2_list.append(outdated_card['power_2'])
      power_3_list.append(outdated_card['power_3'])

    power_0_average = sum(power_0_list) / len(power_0_list)
    power_1_average = sum(power_1_list) / len(power_1_list)
    power_2_average = sum(power_2_list) / len(power_2_list)
    power_3_average = sum(power_3_list) / len(power_3_list)

    if max([power_0_average, power_1_average, power_2_average, power_3_average]) >= 80:
      return True
    else:
      return False
  else:
    return False


print('''\n welcome to the card game. Press x to exit at any point in the game. Press any key to continue. 
      \n Press h to show list of commands.''')
print('Press 1 for CPU, 2 for player')
choice = input()
if int(choice) == 1:
  is_CPU = True
  

print('creating players..')
create_players(is_CPU)
print('populating deck...')
populate_deck()
print('dealing cards to players...')
deal_cards_to_players()
print('rolling dice..')
roll_dice()
print('\n')

while len(player_one.cards) > 0 and len(player_two.cards) > 0:
  print('press enter to continue. press x to quit. p for points. o for outdated deck')
  option = input()
  if option == 'x':
    print('Exiting the game.')
    break
    
  elif option == 'p':
    print('Points table:')
    print('player 1:', player_one.points)
    print('player 2:', player_two.points)
    
  elif option == 'o':
    print('outdated deck:', outdated_deck)

  if player_one.has_next_move:
    print('\nplayer 1 move next. Type b to battle. s to show the card. r to resurrect. g for god spell.')
    if god_spell_used or resurrect_spell_used:
      print('press p to pass')

  elif player_two.has_next_move:
    print('\n player 2 move next. Type b to battle. s to show the card. r to resurrect. g for god spell.')
    if god_spell_used or resurrect_spell_used:
      print('press p to pass')
    
    
  if player_two.has_next_move and player_two.is_CPU:
    if player_two.is_resurrect_spell_available and pick_resurrect():
      print('CPU is picking resurrect')
      option = 'r'
    elif player_two.is_god_spell_available and random.choice([True, False]) and len(player_one.cards)>=3:
        print('CPU is picking god spell')
        option = 'g'
    elif god_spell_used or resurrect_spell_used:
        print('CPU chooses pass')
        option = 'p'
    else:
      print('CPU picks battle.')
      option = 'b'
  else: 
    option = input()
    
  
  if (god_spell_used or resurrect_spell_used) and option == 'p':
    if player_one.has_next_move: 
      player_one.has_next_move = False
      player_two.has_next_move = True
      countered = True
    else:
      player_one.has_next_move = True
      player_two.has_next_move = False
      countered = True
    
  if option == 'b':
    if ((god_spell_used or resurrect_spell_used) and countered) or (not god_spell_used and not resurrect_spell_used):
      print('pick a power number to compare. Press c to cancel')
      if player_two.has_next_move and  player_two.is_CPU:
        print('CPU picks the card.')
        a = list(player_two.top_card.values())[1:]
        power_number = str(a.index(max(a)))
        print('The power number picked by CPU:', power_number)
      else:  
        power_number = input()
      if power_number == 'c':
        continue

      compare_top_cards(power_number)
    else:
      print("can't battle.")
    
    
  elif option == 'r':
    if not countered:
      if player_one.has_next_move:
        if not player_one.top_card_revealed:
          is_resurrected = player_one.use_resurrect_spell()
          if is_resurrected:
            player_one.has_next_move = False
            player_two.has_next_move = True
            if god_spell_used or resurrect_spell_used:
              countered = True
            resurrect_spell_used = True
            if god_spell_used:
              print('player 2 has the option to choose the resurrected card or the previously chosen card. To pick the previously chosen card, press y, else press n.')
              if player_two.is_CPU:
                  change = random.choice(['y','n'])
                  print('CPU chooses', change)
              else:
                  change = input()
              if change == 'y':
                player_one.push_card_to_top(1)
              else:
                pass

        else:
          print('cannot use resurrect. top card has been revealed.')
      else:
        if not player_two.top_card_revealed:
          is_resurrected = player_two.use_resurrect_spell()
          if is_resurrected:
            player_one.has_next_move = True
            player_two.has_next_move = False
            if god_spell_used or resurrect_spell_used:
              countered = True
            resurrect_spell_used = True
            if god_spell_used:
              print('player 1 has the option to choose the resurrected card or the previously chosen card. To pick the previously chosen card, press y, else press n.')
              change = input()
              if change == 'y':
                player_two.push_card_to_top(1)
              else:
                pass
        else:
          print('cannot use resurrect. top card has been revealed.')
    else:
      print('cannot use spell.')
    
  elif option == 's':
    if player_one.has_next_move is True:
      print(player_one.top_card)
      player_one.top_card_revealed = True
   
    else:
      print(player_two.top_card)
      player_two.top_card_revealed = True
      
  elif option=='g':
    if not god_spell_used and not resurrect_spell_used:
      print('select which card of the opponent to be played')
      if player_two.has_next_move and player_two.is_CPU:
          print('CPU picking card from player 1 deck.')
          card_number = random.randrange(1, len(player_one.cards) - 1)
          print('CPU picked:', card_number)
      else:
        card_number = input()

      if player_one.has_next_move:
        if player_one.is_god_spell_available:
          player_two.push_card_to_top(int(card_number))
          player_one.is_god_spell_available = False
          player_one.has_next_move = False
          player_two.has_next_move = True
          if god_spell_used or resurrect_spell_used:
            countered = True
          god_spell_used = True
        else:
          print('already used god spell.')

      else:
        if player_two.is_god_spell_available:
          player_one.push_card_to_top(int(card_number))
          player_two.is_god_spell_available = False
          player_two.has_next_move = False
          player_one.has_next_move = True
          if god_spell_used or resurrect_spell_used:
            countered = True
          god_spell_used = True
        else:
          print('already used god spell.')
    else:
      if resurrect_spell_used and not countered:
        print('cannot use god spell as its not the player round')
      elif god_spell_used and not countered:
        print('cannot use god spell as god spell used by the opponent.')
      else:
        print('cannot use spell.')
    
  else:
    pass

if len(player_one.cards) == 0 or len(player_two.cards) == 0:
  print('game is over.')
  print('player 1:', player_one.points)
  print('player 2:', player_two.points)
  if player_one.points > player_two.points:
    print('player 1 won the game.')
  elif player_one.points == player_two.points:
    print("It's a draw.")
  else:
    print('player 2 won the game.')


