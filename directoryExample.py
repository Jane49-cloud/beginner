from pathlib import Path


path = Path("ecommerce ")
print(path.exists())

path1 = Path()
for file in path1.glob("*.py"):
    print(file)




