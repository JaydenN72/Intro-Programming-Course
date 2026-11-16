class Players:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} - {self.playerPosition}"

class NFLTeam:
    def __init__(self, teamName, players):
        self.teamName = teamName
        self.players = players

    def display_team(self):
        print(f"Team: {self.teamName}")
        print("Players:")
        for player in self.players:
            print(f"  {player}")


player1 = Players("Joe Montana", "QB")
player2 = Players("Barry Sanders", "RB")
player3 = Players("Jerry Rice", "WR")
player4 = Players("Graham Gano", "K")
playerList = [player1, player2, player3, player4]
team = NFLTeam("Smashmouth", playerList)

team.display_team()