class Controller:
    def __init__(self, view, game):
        self.view = view
        self.game = game
        return self
    

    def process_input(self, input:str):
        protagonist = self.game.get_player()
        protagonist.advance_event(input)