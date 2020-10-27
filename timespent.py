def is_zero(tickets):
    for v in tickets.values():
        if v != 0:
            return False
    return True


def timespent(tickets):
    tickets_key = {}
    time_spent = {}
    counter = 1

    for i, x in enumerate(tickets):
        tickets_key[i] = x
        time_spent[i] = 0

    while not is_zero(tickets_key):
        for k, v in tickets_key.items():
            if v:
                tickets_key[k] = v - 1
                time_spent[k] = counter
                counter += 1

    res = []
    for k, v in time_spent.items():
        res.insert(k, v)
    return res


print(timespent([1, 2, 3]))
