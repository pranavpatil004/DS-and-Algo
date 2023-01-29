from battleship import GameFactory
from players import PlayerFactory

if __name__ == "__main__":
    player_factory = PlayerFactory()
    player_1 = player_factory.get_player()
    player_2 = player_factory.get_player()

    grid_size = int(input())
    game = GameFactory().get_game("Missile", [player_1, player_2], grid_size, grid_size)
    ships = int(input())
    input_pos = input().split(":")

    battleship_positions = []
    for position in input_pos:
        x, y = position.split(",")
        battleship_positions.append((int(x), int(y)))

    game.add_battleship_positions(player_1, battleship_positions)
    input_pos = input().split(":")

    for position in input_pos:
        x, y = position.split(",")
        battleship_positions.append((int(x), int(y)))
    game.add_battleship_positions(player_2, battleship_positions)

    total_missiles = input()
    player_1_missiles_input = input().split(":")
    player_2_missiles_input = input().split(":")
    player_1_missiles = []
    player_2_missiles = []
    for position in player_1_missiles_input:
        x, y = position.split(",")
        player_1_missiles.append((int(x), int(y)))

    for position in player_2_missiles_input:
        x, y = position.split(",")
        player_2_missiles.append((int(x), int(y)))

    player_1_score = game.execute_playing_strategy(player_2, player_1_missiles)
    player_2_score = game.execute_playing_strategy(player_1, player_2_missiles)

    if player_1_score == player_2_score:
        print("Its a draw")
    elif player_1_score > player_2_score:
        print("Player 1 wins")
    else:
        print("Player 2 wins")
    game.print_grids()
