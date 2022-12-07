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
            pwd_str = str(pwd)
            if pwd_str not in paths:
                paths[pwd_str] = 0

        if parts[0][0].isdigit():
            pwd_str = str(pwd)
            paths[pwd_str] += int(parts[0])
            file_pwd = pathlib.Path(pwd_str)
            while str(file_pwd) != "/":
                paths[str(file_pwd.parent)] += int(parts[0])
                file_pwd = file_pwd.parent

amount_to_delete = 30_000_000 - (70_000_000 - paths["/"])
possible_for_deletion = {k: v for k,
                         v in paths.items() if v >= amount_to_delete}
print(min(possible_for_deletion.values()))
