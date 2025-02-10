 #***Daily report that tracks the use of machines***
 #which users are currently connected to which machines
 #system that collects every event that happens on the machines on the network

#helper function that sort the list
def get_event_date(event):
    return event.date

#procesing function for current users
def current_users(events):
    events.sort(key=get_event_date)
    #create the dictionary to store the users of the machine
    machines = {}
    #iterate through list of events
    for event in events:
        #check if the macine efected by the event is in dictionary
        if event.machine not in machines:
            #if not in dictionary add in empty set
            machines[event.machine] = set()
        #for the log in event we want to add the user
        if event.type == "login":
            machines[event.machine].add(event.user)
        #for log out event we want to remove the user
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

#function used for printing the report
def generate_report(machines):
    #iterate though the key and values in dictionary
    for machine, users in machines.items():
        #check if the machines has a user loged in and 
        #only to print when the set of users has more than zero elements
        if len(users) > 0:
            #print machine name followed by users logged in the machine
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

# a class that has a constructor for necesary atributes: date, type, machine name and user
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

# examples of types of events
events = [
  Event('2025-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
  Event('2025-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
  Event('2025-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
  Event('2025-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
  Event('2025-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
  Event('2025-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# dictionary with the machine names as keys are created
users = current_users(events)
print(users)

# generating the report
generate_report(users)

# *** Result:{'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': {'chris'}}
# *** webserver.local: lane
# *** mailserver.local: chris
