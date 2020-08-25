def resolve(n, start, arrival, inter):
    """
    parameters
    ----------
    n: numbers of disk
    start: (str) name of the starting peg
    arrival: (str) name of the arrival peg
    inter: (str) name of the intermediate peg

    return
    ------
    (list) resolving steps
    """
    if n == 1:
        steps = [(start, arrival)]
    else:
        steps = resolve(n-1, start, inter, arrival)
        steps.append((start, arrival))
        steps.extend(resolve(n-1, inter, arrival, start))

    return steps

if __name__ == '__main__':
    steps = resolve(4, 'A', 'C', 'B')
    print("{} steps".format(len(steps)))
    print(steps)