import random, time

def stat_roller(stat):
  roll_holder = []
  for i in range(4):
    roll_holder.append(random.randint(1,6))# = random.randint(1,6)
    roll_holder.sort()
  del roll_holder[0]
  print(f'{stat} is {sum(roll_holder)}')

print('Welcome to Character Creator by Grizzled Labs!\n')
time.sleep(1)
print('Character creater rolls 4d6 and drops the\n lowest to create stats for your character')

replay = 'Y'
while replay == 'Y':
  time.sleep(1)
  print('\nRolling the dice...\n')
  time.sleep(1)
  stat_roller('Strength')
  time.sleep(0.25)
  stat_roller('Constitution')
  time.sleep(0.25)
  stat_roller('Dexterity')
  time.sleep(0.25)
  stat_roller('Intelligence')
  time.sleep(0.25)
  stat_roller('Wisdom')
  time.sleep(0.25)
  stat_roller('Charisma')
  time.sleep(0.25)

  replay = input('\nRoll again? Y/N:   ').upper()
  while replay not in ('Y', 'N'):
    replay = input('Y/N:   ').upper()
print('Thanks for using Character Creator by Grizzled Labs!\nFeedback? Email GrizzledLabs@gmail.com')