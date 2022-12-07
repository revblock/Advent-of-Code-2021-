import pathlib

paths = {}
pwd = pathlib.Path("/")


def cd(pwd, path):
    match path:
        case "..":
            return pwd.parent
        case "/":
            return pathlib.Path(pwd.root)
    return pwd.joinpath(path)


with open("./input.txt") as input_file:
    for line in input_file:
        clean_line = line.strip()
        parts = clean_line.strip("$").strip().split()

        if parts[0] == "cd":
            pwd = cd(pwd, parts[1])
            if str(pwd) not in paths:
                paths[str(pwd)] = 0

        if parts[0][0].isdigit():
            paths[str(pwd)] += int(parts[0])
            file_pwd = pathlib.Path(str(pwd))
            while str(file_pwd) != "/":
                paths[str(file_pwd.parent)] += int(parts[0])
                file_pwd = file_pwd.parent


over_100_000 = {k: v for k, v in paths.items() if v < 100_000}
print(sum(over_100_000.values()))
