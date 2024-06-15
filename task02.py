
import random  #random number generate

def random_num_gen():
    ran_num = random.randint(1,3) # random number from 1 to 3
    return ran_num

def check(player,pc):  # game rules
    if (player == pc):
        return "DRAW"
    if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
        return "YOU WIN"
    if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
        return "PC WIN"

def game():
    print("ROCK[1] , PAPER[2] , SCISSOR[3]") # user screen output
    user = int(input())
    randm_num = random_num_gen()
    if randm_num == 1:
        print("PC choose : ROCK")
    elif randm_num == 2:
        print("PC choose : PAPER")
    elif randm_num == 3:
        print("PC choose : SCISSOR")
    decision = check(user, randm_num)
    return decision

# Start the Game :

print("START[1] | EXIT[0]")
player_choice = int(input())
if player_choice == 1:
    while True:
        final_result = game() # loop for continue the game till exit
        print(final_result)
        print("TRY AGAIN ?? >> YES[1] | NO[0]") # game continue or not
        player_choice = int(input())
        if player_choice ==1:
            continue
        else:
            break
print("THANK YOU")   # End of the game