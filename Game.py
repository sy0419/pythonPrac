class Player():
    def __init__(self, name, team):
        self.name = name
        self.xp =  1500
        self.team = team

    def introduce(self):
        print(f"Hello, My name is {self.name} and I am in {self.team}")

    def team_members(self):
        print(f"{self.team}: {self.name}")

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def show_player(self):
        for player in self.players:
            player.introduce()

    def show_team_members(self):
        for player in self.players:
            player.team_members()

    def team_total_xp(self):
        team_total_xp = 0
        for player in self.players:
            team_total_xp += player.xp
        print(f"{self.team_name}'s total xp: {team_total_xp}")
    
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                return print(f"{name} is not in {self.team_name} anymore.")


team_X = Team("Team X")
team_Y = Team("Team Y")

team_X.add_player("Harry")
team_X.add_player("James")
team_X.add_player("Leo")
team_X.add_player("Sam")
team_X.add_player("Tim")

team_Y.add_player("Anna")
team_Y.add_player("Jane")
team_Y.add_player("Julia")

team_X.remove_player("Leo")

# team_X.show_player()
# team_Y.show_player()

team_X.show_team_members()
print("---------------------------")
team_Y.show_team_members()

print("---------------------------")
team_X.team_total_xp()
team_Y.team_total_xp()