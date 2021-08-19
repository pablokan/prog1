def get_full_name(first_name: str, last_name: str) -> str: 
    full_name = first_name.capitalize() + " " + last_name.capitalize()
    return full_name
print(get_full_name("paul", "kan"))


def daily_average(temperatures: list[float]) -> float:
    return sum(temperatures) / len(temperatures)

print(daily_average([1,2]))

def foo(diccy: dict[str: int]) -> tuple:
    return diccy.values()

print(foo({"a": "1.1", "b": 2}))
