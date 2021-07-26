def count(i):
    print(i)
    if i <= 1:
        return
    else:
        count(i-1);

if __name__ == '__main__':
    count(10);