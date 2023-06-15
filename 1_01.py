
# O(N ** 2)
def str_counter(string):
    for sym in set(string):
        count = 0
        for sub_sym in string:
            if sym == sub_sym:
                count += 1
        print(f"{sym} - {count}")

# O(N)
def strcounter(string):
    for sym in set(string):
        print(f"{sym} - {string.count(sym)}")

