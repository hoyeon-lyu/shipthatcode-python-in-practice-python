n = int(input())
items = []
history = []
for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    if cmd == "show":
        if len(items) == 0:
            print("(empty)")
        else:
            print(" ".join(items))
    elif cmd == "add":
        # TODO: save the current list first, then append parts[1]
        pass
    # TODO: insert, remove, pop, reverse, sort and undo
