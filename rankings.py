import pandas as pd

fairfax2024 = pd.read_csv("./fairfax-2024.csv")
callisto2024 = pd.read_csv("./callisto.csv")
io2024 = pd.read_csv("./io.csv")


class Person:
    def __init__(self, n: str, e: list):
        self.name = n
        self.events = e
        self.rankings = {}


    # person is assigned to event
    def has_event(self, event: str) -> bool:
        return event in self.events


    # associate ranking to person
    # PRE: person has event
    def add_ranking(self, event: str, ranking: int):
        self.rankings[event] = ranking
    

    # calculate average ranking of person
    def calc_average(self) -> float:
        return sum(self.rankings.values()) / len(self.rankings)



class Team:
    def __init__(self, n: str):
        self.name = n
        self.members = []

    def add_member(self, m: Person):
        self.members.append(m)



# names of events
EVENT_NAMES = [event for event in callisto2024.loc[:, "Event"]]

def process_team(team: pd.DataFrame, n: str) -> Team:
    # new team object
    new_team = Team(n)
    
    # obtain list of member names
    members = team.columns.values.tolist()[1:]
    
    # iterate members and assign events
    for member in members:
        # get raw column values
        member_col = team[member].values.tolist()

        # get list of person's events
        member_events = []
        for i, element in enumerate(member_col):
            if type(element) != float:
                member_events.append(EVENT_NAMES[i])

        # create and save new member
        new_team.add_member(Person(member, member_events))

    # return complete team
    return new_team


callisto = process_team(callisto2024, "Callisto")
io = process_team(io2024, "Io")


print(fairfax2024)