
def sum(i):

    if(i == 1):
        return i;
    else:
        return i + sum(i-1);

if __name__ == '__main__':
    print(sum(10))