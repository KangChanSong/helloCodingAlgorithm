
from collections import deque

graph = dict()
graph["you"] = ["bob", "claire", "alice"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "johnny"]
graph["alice"] = ["peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = ["claire"]
graph["johnny"] = []



def bfs_mango_seller():
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft();
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person];
    return False;

def person_is_seller(name):
    return name[-1] == "m";

if __name__ == '__main__':
    bfs_mango_seller();