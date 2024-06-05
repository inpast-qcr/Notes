from os.path import splitext


def get_suffix(filename, ignore_dot=True):
    return splitext(filename)[0]#[1:]


print(get_suffix('readme.txt'))