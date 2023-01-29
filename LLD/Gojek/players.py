class Player:
    def __init__(self, player_id) -> None:
        self.__player_id = player_id


class PlayerFactory:
    def __init__(self) -> None:
        self.__player_id = 0

    @property
    def player_id(self):
        return self.__player_id

    def get_player(self):
        player = Player(self.__player_id)
        self.__player_id += 1
        return player


class PlayerScore:
    def __init__(self) -> None:
        self.__players_scores = {}

    @property
    def players_scores(self):
        return self.__players_scores

    def get_player_score(self, player_id):
        return self.__players_scores.get(player_id, "Player not found")

    def set_player_score(self, player_id, score):
        if player_id not in self.__players_scores:
            self.__players_scores[player_id] = 0
        self.__players_scores[player_id] += score
