from datetime import datetime

num = 123.4567
print(f"{num:.2f}")
print(f"{num * 2 = }")
nestedFormat3 = ".3f"
print(f"{num:{nestedFormat3}}")

now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
