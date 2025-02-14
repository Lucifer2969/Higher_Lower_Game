import art, game_data,os
import random

def person_selection():
    value = random.choice(game_data.person_list)
    game_data.person_list.remove(value)
    return value


count = 0
person_A = person_selection()
person_B = person_selection()
condition = True

print(art.main_logo)
print(f"Compare A: {person_A['name']} a {person_A['description']} from {person_A['country']}")
print(art.second_logo)
print(f"Compare B: {person_B['name']} a {person_B['description']} from {person_B['country']}")

while condition:
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == 'A' and person_A['follower_count'] > person_B['follower_count']:
        person_A = person_B
        person_B = person_selection()
        count += 1
    elif user_choice == 'B' and person_A['follower_count'] < person_B['follower_count']:
        person_A = person_B
        person_B = person_selection()
        count += 1
    elif user_choice == 'A' and person_A['follower_count'] < person_B['follower_count']:
        print('\n'*50)
        print(art.main_logo)
        print(f"Sorry that's wrong. Final Score:{count}")
        print('\n'*10)
        condition = False
        break
    elif user_choice == 'B' and person_A['follower_count'] > person_B['follower_count']:
        print('\n'*50)
        print(art.main_logo)
        print(f"Sorry that's wrong. Final Score:{count}")
        print('\n'*10)
        condition = False
        break
    print('\n'*50)
    print(art.main_logo)
    print(f"You're right. Current Score {count}")
    print(f"Compare A: {person_A['name']} a {person_A['description']} from {person_A['country']}")
    print(art.second_logo)
    print(f"Compare B: {person_B['name']} a {person_B['description']} from {person_B['country']}")

os.system("pause")