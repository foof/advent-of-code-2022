
class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.dirs = []
        self.files = []
        self.parent = parent

    def get_dir(self, dirname):
        for dir in self.dirs:
            if dir.name == dirname:
                return dir

        new_dir = Directory(dirname, self)
        self.dirs.append(new_dir)
        return new_dir

    def get_size(self):
        size = 0
        for dir in self.dirs:
            size += dir.get_size()
        for file in self.files:
            size += file.size
        return size

    def print(self, indent=''):
        print(f"{indent}- {self.name} (dir, size={self.get_size()})")
        for dir in self.dirs:
            dir.print(f"{indent}    ")
        for file in self.files:
            print(f"{indent}    - {file.name} (file, size={file.size})")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def process_directory_1(dirs, directory):
    if directory.get_size() <= 100000:
        dirs.append(directory)
    for dir in directory.dirs:
        process_directory_1(dirs, dir)


smallest_dir = None


def find_smallest_dir_to_delete(size_needed, directory):
    global smallest_dir
    for dir in directory.dirs:
        if dir.get_size() >= size_needed:
            if not smallest_dir or dir.get_size() < smallest_dir.get_size():
                smallest_dir = dir
        find_smallest_dir_to_delete(size_needed, dir)
    return smallest_dir


def part1_2(lines):
    root = None
    pwd = None
    for line in lines:
        if line.startswith('$ cd'):
            path = line[5:]
            if path == '..':
                pwd = pwd.parent
            else:
                if not root:
                    root = Directory(line[5:])
                    pwd = root
                else:
                    pwd = pwd.get_dir(line[5:])
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            pwd.get_dir(line[4:])
        else:
            size, name = line.split(' ')
            pwd.files.append(File(name, int(size)))

    dirs = []
    process_directory_1(dirs, root)
    print(sum([dir.get_size() for dir in dirs]))

    space_needed = 30000000 - (70000000 - root.get_size())
    result_2 = find_smallest_dir_to_delete(space_needed, root).get_size()
    print(result_2)


if __name__ == "__main__":
    with open('./input', 'r') as f:
        part1_2(f.read().splitlines())
