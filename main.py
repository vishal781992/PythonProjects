def main(a, b, c):
    # take the list and convert that list into a args print every arg
    print("First name: %s, Last name: %s, gender: %s " % (a, b, c))


if __name__ == '__main__':
    list_x = ["vish", "chopade", "male"]
    main(*list_x)