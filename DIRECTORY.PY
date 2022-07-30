import os


DIRECTORIES = []
for i in range(1,14):
    DIRECTORIES.append(f"{os.getcwd()}\WEEKS\{i}")
for i in DIRECTORIES:

    if not os.path.isdir(i):
        os.makedirs(r"{}".format(i))

for i in DIRECTORIES:
    f = open(r"{}\__init__.py".format(i), 'w')
