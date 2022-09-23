players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# kevin = {
#     	"name": "Kevin Durant", 
#     	"age":34, 
#     	"position": "small forward", 
#     	"team": "Brooklyn Nets"
# }
# jason = {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
# }
# kyrie = {
#     	"name": "Kyrie Irving", 
#     	"age":32,
#         "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
# }
    
# Create your Player instances here!
# player_jason = ???





class Player:
    new_team = []
    def __init__(self, player):#challenge 1
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']
        Player.new_team.append(self)

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age} Position: {self.position} Team: {self.team}")

    #Ninja Bonus
    @classmethod
    def get_team(cls, team_list):
        for player in cls.new_team:
            player.display_info()


#challenge 2
# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)

#challenge 3
for index in players:
    index = Player(index)
Player.new_team[len(players)-1].display_info()
print('========')
#goes with Ninja Bonus line 56-60
random_team=[]
Player.get_team(random_team)
