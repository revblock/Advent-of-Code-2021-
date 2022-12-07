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

disk_size = 70_000_000
minimum_space = 30_000_000

current_free_space = disk_size - paths["/"]
amount_to_delete = minimum_space - current_free_space
possible_for_deletion = {k: v for k,
                         v in paths.items() if v >= amount_to_delete}
print(min(possible_for_deletion.values()))
