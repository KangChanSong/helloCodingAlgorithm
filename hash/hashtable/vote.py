voted = {}

def check_voter(name):
    if voted.get(name):
        print("돌려 보내")
    else:
        voted[name] = True
        print("투표하게 하세요")


if __name__ == '__main__':
    check_voter("John");
    check_voter("Chan");
    check_voter("John");