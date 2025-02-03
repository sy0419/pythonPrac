class Player():
    def __init__(self, name, team):
        self.name = name
        self.xp =  1500
        self.team = team

    def introduce(self):
        print(f"Hello, My name is {self.name} and I am in {self.team}")

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def show_player(self):
        for player in self.players:
            player.introduce()
    
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)


team_X = Team("Team X")
team_Y = Team("Team Y")

team_X.add_player("Harry")
team_X.add_player("James")
team_X.add_player("Leo")

team_Y.add_player("Anna")
team_Y.add_player("Jane")

team_X.show_player()
team_Y.show_player()
print("------------------")
team_X.remove_player("Leo")

team_X.show_player()
team_Y.show_player()