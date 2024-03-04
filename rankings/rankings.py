import pandas as pd

callisto2024 = pd.read_csv("./rankings/fairfax/callisto.csv")
io2024 = pd.read_csv("./rankings/fairfax/io.csv")


# names of events
EVENT_NAMES = [event for event in callisto2024.loc[:, "Event"]]

# columns to remove
REMOVE_COLS = "number exhibition city state track rank total".split(" ")

class Competition:
    def __init__(self, n: str, filepath: str):
        self.name = n
        self.original = pd.read_csv(filepath)

        # process Woodson teams
        comp = self.original.copy().drop(columns=REMOVE_COLS)
        self.team_results = comp[comp["school"].str.contains("Woodson")].drop(columns="school")

fairfax2024 = Competition("2024 Fairfax Invitational", "./rankings/fairfax/fairfax-2024.csv")


# one Div C competitor
class Person:
    def __init__(self, n: str, e: list):
        self.name = n
        self.events = e
        self.rankings = {}
        for event in e:
            self.rankings[event] = []

    # person is assigned to event
    def has_event(self, event: str) -> bool:
        return event in self.events

    # associate ranking to person
    # PRE: person has event
    def add_ranking(self, event: str, ranking: int):
        self.rankings[event].append(ranking)
    
    # calculate average ranking of person
    def calc_average(self) -> float:
        r = []
        for e in self.rankings.values():
            r += e
        return sum(r) / len(r)
    
    # return string representative of person
    def summary(self) -> str:
        output = f"{self.name}:"
        for event in self.events:
            output += f"\n {event}: ({', '.join([str(n) for n in self.rankings[event]])})"
        return output
    
    def __repr__(self) -> str:
        return f"{self.name}: {', '.join(self.events)}"



# one Div C team
class Team:
    def __init__(self, n: str, team: pd.DataFrame):
        self.name = n
        self.members = []

        # obtain list of member names
        mems = team.columns.values.tolist()[1 : ]

        # iterate members and assign events
        for mem in mems:
            # get raw column values
            mem_col = team[mem].values.tolist()

            # get list of person's events
            mem_events = []
            for i, element in enumerate(mem_col):
                if type(element) != float:
                    mem_events.append(EVENT_NAMES[i])

            # create and save new member
            self.members.append(Person(mem, mem_events))


    # process rankings for competition
    def process_comp(self, comp: Competition, team_name: str):
        team_results = comp.team_results.loc[comp.team_results["team"] == team_name].drop(columns="team")
        for event in EVENT_NAMES:
            if event in team_results.head():
                for member in self.members:
                    if member.has_event(event):
                        member.add_ranking(event, int(team_results[event]))

    # print average rankings of each member
    def print_averages(self):
        for member in self.members:
            print(f"{member.name}: {round(member.calc_average(), 2)}")

    # print full summary
    def print_summary(self):
        for member in self.members:
            print(member.summary())







callisto = Team("Callisto", callisto2024)
callisto.process_comp(fairfax2024, "B")
# callisto.print_summary()
callisto.print_averages()
io = Team("Io", io2024)
# io.process_comp(fairfax2024, "A")
# io.print_averages()
