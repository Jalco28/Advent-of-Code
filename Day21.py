from functools import lru_cache
import sympy

class HumanError(Exception):
    pass

with open("Day21Input.txt", "r") as f:
    data = [(monkey[:4]+monkey[5:]).strip('\n').split(" ") for monkey in f]
monkeys = {}
for monkey in data:
    value = monkey[1:]
    if len(value) == 1:
        monkeys[monkey[0]] = int(value[0])
    else:
        monkeys[monkey[0]] = value

@lru_cache(maxsize = None, typed=False)
def calculate_monkey(monkey_id:str):
    monkey = monkeys[monkey_id]
    if isinstance(monkey, int):
        return monkey
    else:
        value1 = calculate_monkey(monkey[0])
        value2 = calculate_monkey(monkey[2])
        return eval(f'{value1} {monkey[1]} {value2}')

# print(calculate_monkey('root'))
#Part 2

@lru_cache(maxsize = None, typed=False)
def calculate_monkey(monkey_id:str):
    if monkey_id == 'humn':
        raise HumanError
    monkey = monkeys[monkey_id]
    if isinstance(monkey, int):
        return monkey
    else:
        value1 = calculate_monkey(monkey[0])
        value2 = calculate_monkey(monkey[2])
        return eval(f'{value1} {monkey[1]} {value2}')

@lru_cache(maxsize=None, typed=False)
def calculate_algebraic_monkey(monkey_id:str):
    if monkey_id == 'humn':
        return '(h)'
    monkey = monkeys[monkey_id]
    if isinstance(monkey, int):
        return f'({monkey})'
    else:
        value1 = calculate_algebraic_monkey(monkey[0])
        value2 = calculate_algebraic_monkey(monkey[2])
        return f'({value1} {monkey[1]} {value2})'

try:
    wanted_value = calculate_monkey(monkeys['root'][0])
    incomplete_monkey = monkeys['root'][2]
except HumanError:
    wanted_value = calculate_monkey(monkeys['root'][2])
    incomplete_monkey = monkeys['root'][0]
print(wanted_value)
math_string = calculate_algebraic_monkey(incomplete_monkey)
h = sympy.symbols('h')
print(sympy.solveset(sympy.Eq(wanted_value, sympy.sympify(math_string))))

print()