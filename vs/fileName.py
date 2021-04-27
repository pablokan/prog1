import os
file = '~/home/kan/development/iteclabs.zip'
n = os.path.basename(file)
print(n)


from pathlib import Path
print(Path(file).name)

print(dir(Path))
