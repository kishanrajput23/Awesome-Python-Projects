import pickle
from .game import Player


class RunRecord():
    '''provide recoded game data
    iterating over instance
    yield rolled_value and index
    '''

    def __init__(self, file_obj):
        self.file_obj = file_obj
        data = pickle.load(self.file_obj)
        self.players = data[0]
        self.game_history = data[1]

    def get_players(self, func=None):
        '''
        return Player object
        recreated from a list
        func is callable which player
        may need for choice delegation
        '''
        res = []
        for colour, name, is_computer in self.players:
            if is_computer:
                player = Player(colour)
            else:
                player = Player(colour, name, func)
            res.append(player)
        return res

    def get_game_history(self):
        return self.game_history

    def __iter__(self):
        return iter(self.game_history)


class MakeRecord():
    '''save game data
    as a nested list which is
    saved with pickle
    '''

    def __init__(self):
        self.players = []
        self.game_history = []

    def add_player(self, player_obj):
        '''Accept Player object and
        it save NOT as object rather as a list
        '''
        if player_obj.choose_pawn_delegate is None:
            is_computer = True
        else:
            is_computer = False
        self.players.append((player_obj.colour,
                             player_obj.name, is_computer))

    def add_game_turn(self, rolled_value, index):
        self.game_history.append((rolled_value, index))

    def save(self, file_obj):
        '''list of lists with players and
        game history
        '''
        pickle.dump([self.players, self.game_history],
                    file_obj)
