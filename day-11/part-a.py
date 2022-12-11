from itertools import islice, repeat
import operator


class Monkey:
    def __init__(self, starting_items, operation, operation_value, divisible_by, throw_true, throw_false):
        self.items = starting_items
        self.operation = operation
        self.operation_value = operation_value
        self.divisible_by = divisible_by
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspected_counter = 0


def parse_input():
    with open("./input.txt") as input_file:
        while True:
            monkey_lines = [line.rstrip('\n')
                            for line in islice(input_file, 6)]
            if not monkey_lines:
                break
            starting_items = list(map(int, monkey_lines[1].strip().replace(
                "Starting items:", "").replace(" ", "").split(",")))
            operation, operation_value = monkey_lines[2].strip().replace(
                "Operation: new = old ", "").split()
            divisible_by = int(monkey_lines[3].strip().replace(
                "Test: divisible by ", ""))
            throw_true = int(monkey_lines[4].strip().replace(
                "If true: throw to monkey ", ""))
            throw_false = int(monkey_lines[5].strip().replace(
                "If false: throw to monkey ", ""))

            yield Monkey(starting_items, operation,
                         operation_value, divisible_by, throw_true, throw_false)


monkeys = list(parse_input())
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

for count in range(20):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            inspected_item = monkey.items.pop(0)
            monkey.inspected_counter += 1
            operation_value = int(
                monkey.operation_value) if monkey.operation_value != "old" else inspected_item
            inspected_item = ops[monkey.operation](
                inspected_item, operation_value)
            inspected_item = inspected_item // 3

            if inspected_item % monkey.divisible_by == 0:
                monkeys[monkey.throw_true].items.append(inspected_item)
            else:
                monkeys[monkey.throw_false].items.append(inspected_item)

monkeys.sort(key=lambda x: x.inspected_counter, reverse=True)
result = monkeys[0].inspected_counter * monkeys[1].inspected_counter
print(result)
