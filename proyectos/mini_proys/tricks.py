d = {'uno': 1, "dos": 2, "tres": 3, "dosBis": 2}

e = {v: k for k, v in d.items()}
print(e)

from collections import defaultdict
reversed_dict = defaultdict(list)
for key, value in d.items():
    reversed_dict[value].append(key)
print(reversed_dict)

rev_dict = dict.fromkeys(d.values(), [])
print(rev_dict)
for key, value in d.items():
    rev_dict[value].append(key)
print(rev_dict)

