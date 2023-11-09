with open('Day7Input.txt', 'r') as f:
    commands = f.readlines()

commands = [command.strip('\n') for command in commands]


class Folder:
    def __init__(self, name, parent=None):
        self.name: str = name
        self.parent: Folder | None = parent
        self.contents = None
        self.path = self.absolute_path()

    def add_contents(self, item):
        if self.contents == None:
            self.contents = [item]
        else:
            self.contents.append(item)

    def absolute_path(self):
        if self.parent is None:
            return '/'
        else:
            string = self.parent.absolute_path()+self.name+'/'
            return string

    def __repr__(self) -> str:
        return f'Folder {self.name}'


class File:
    def __init__(self, name, size, parent):
        self.name: str = name
        self.size: int = size
        self.parent: Folder = parent

    def __repr__(self) -> str:
        return f'File {self.name}'


root = Folder('/')
folders = {'/': root}
current_folder = folders['/']
for command in commands:
    if command[:5] == '$ cd ':
        if command[5:] == '..':
            current_folder = current_folder.parent
        elif command[5:] == '/':
            pass
        else:
            current_folder = folders[current_folder.path + command[5:]+'/']
    elif command[:4] == 'dir ':
        temp_folder = Folder(command[4:], current_folder)
        folders[temp_folder.path] = temp_folder
        current_folder.add_contents(folders[temp_folder.path])
    elif command[:5] == '$ ls':
        pass
    else:
        file_size = int(command.split(' ')[0])
        file_name = command.split(' ')[1]
        current_folder.add_contents(File(file_name, file_size, current_folder))


def find_folder_size(folder: Folder):
    size = 0
    for item in folder.contents:
        if type(item) == File:
            size += item.size
        elif type(item) == Folder:
            size += find_folder_size(item)
    return size


for folder in folders.values():
    folder.size = find_folder_size(folder)

total = 0
for folder in folders.values():
    if folder.size <= 100000:
        total += folder.size
# print(total)

# Part 2
FREE_SPACE = 70000000 - folders['/'].size
NEEDED_SPACE = 30000000
MINIMUM_DELETION = NEEDED_SPACE - FREE_SPACE
current_best = folders['/']
for folder in folders.values():
    if folder.size < current_best.size and folder.size>=MINIMUM_DELETION:
        current_best = folder
print(current_best.size)