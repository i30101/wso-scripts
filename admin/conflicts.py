# Author: Andrew Kim
# Version: 2.0.0
# Since: 13 November 2023
# Event conflict identifier


# import external libraries
import pandas as pd


# file data
TEAMS = ["europa", "callisto", "io"]
FILEPATH = "./admin/events/"


# names of all 2024 events
event_names = []

# person-event assignments
roster = {}

# event-people assignments
events = {}

# conflicts each event has with other events
conflicts = {}

# paired events
pairings = [
    ("Anatomy", "Microbe Mission"),
    ("Detector Building", "Robot Tour"),
    ("Air Trajectory", "Flight"),
    ("Chem Lab", "Forensics"),
    ("Codebusters", "Fermi Questions"),
    ("Geologic Mapping", "Dynamic Planet"),
    ("Forestry", "Ecology"),
    ("Optics", "Wind Power")
]




# get initial data
europa = pd.read_csv("./admin/events/europa.csv")
event_names = [event for event in europa.loc[:, "Event"]]


# assigns events of each competitor on a given team
def process_team(team: str):
    # read csv file
    dataframe = pd.read_csv(FILEPATH + team + ".csv")

    # get names of people
    people_in_team = dataframe.columns.values.tolist()[1:]

    # go through names in dataframe
    for member in people_in_team:
        # get raw column values
        member_col = dataframe[member].values.tolist()

        # get list of person's events
        member_events = []
        for i, element in enumerate(member_col):
            if type(element) != float:
                member_events.append(event_names[i])

        # save person and events in dictionary
        roster[member] = member_events


# handles paired events
# returns false: event is not paired
# returns a string: other event in pairing
def process_pair(event: str):
    for pairing in pairings:
        if event == pairing[0]:
            return pairing[1]
        elif event == pairing[1]:
            return pairing[0]
    return False



for team in TEAMS:
    process_team(team)


# get people in each event
for person in roster:
    # print(person, roster[person])
    for event in roster[person]:
        if event not in events:
            events[event] = []
        events[event].append(person)


# find other events conflicting with each events
for event in events:
    # list of conflicts for event
    event_conflicts = []

    # iterate through people in event
    for person in events[event]:
        persons_events = roster[person]
        event_conflicts.extend([e for e in persons_events if e not in event_conflicts and e != event])
    
    conflicts[event] = event_conflicts


for event in conflicts:
    print(event + ": ", " ".join(conflicts[event]))
