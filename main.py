n = int(input())
items = []
history = []
for _ in range(n):
    parts = input().split(" ")
    cmd = parts[0]
    if cmd == "show":
        if len(items) == 0:
            print("(empty)")
        else:
            print(" ".join(items))
    elif cmd == "add":
        history.append(list(items))
        items.append(parts[1])
        # TODO: save the current list first, then append parts[1]
    elif cmd == "insert":
        history.append(list(items))
        items.insert(int(parts[1]), parts[2])
    elif cmd == "remove":
        if len(items) == 0:
            continue
        if len(parts) == 2 and parts[1] in items:
            history.append(list(items))
            items.remove(parts[1])
        elif len(parts) == 1 or len(parts) == 2 and not parts[1] in items:
            history.append(list(items))
            items.pop()
        else:
            print("Not appropriate sentence")
            continue
    elif cmd == "pop":
        history.append(list(items))
        if len(items) == 0:
            continue
        items.pop()
    elif cmd == "reverse":
        history.append(list(items))
        items.reverse()
    elif cmd == "sort":
        history.append(list(items))
        items.sort()
    elif cmd == "undo":
        if len(history) == 0:
            continue
        items = history.pop()
    else:
        print("Unknown command")
        continue
        


    # TODO: insert, remove, pop, reverse, sort and undo
