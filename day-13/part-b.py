from functools import cmp_to_key
from math import prod


def read_packets():
  with open("input.txt") as f:
    packets = [eval(output) for output in (line.strip() for line in f) if len(output)]
  return packets

def sort_packets(left, right) -> int:
  result = 0

  for i in range(min(len(left), len(right))):
    match isinstance(left[i], list), isinstance(right[i], list):
      case True, True: result = sort_packets(left[i], right[i])
      case True, False: result = sort_packets(left[i], [right[i]])
      case False, True: result = sort_packets([left[i]], right[i])
      case _: result = (left[i] > right[i]) - (left[i] < right[i])

    if result:
      return result

  return (len(left) > len(right)) - (len(left) < len(right))

packets = read_packets()
packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(sort_packets))
result = prod(i + 1 for i, p in enumerate(packets) if sort_packets(p, [[2]]) == 0 or sort_packets(p, [[6]]) == 0)

print(result)





