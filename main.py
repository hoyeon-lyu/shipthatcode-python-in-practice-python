n = int(input())
entries = []
for _ in range(n):
    name, ms = input().split(" ")
    entries.append((int(ms), name))

entries.sort()

best_ms:int
worst_name:str
worst_ms:int
for place, (ms, name) in enumerate(entries, start=1):
    if place == 1:
        best_ms = ms
    if place == n:
        worst_name = name
        worst_ms = ms
    if place <= 3:
        print(f"{place}. {name} {ms}")

f_slowest = f"{worst_name} {worst_ms}"
gap = worst_ms - best_ms

# TODO: rank the entries so the fastest comes first and ties are alphabetical
# TODO: print the podium lines, then the slowest line and the gap
print(f"slowest: {f_slowest}")
print(f"gap: {gap}")
