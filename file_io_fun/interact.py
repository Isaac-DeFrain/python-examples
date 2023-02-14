from pathlib import Path

def get_increment_set(fname: str = "file.txt") -> int:
    '''
    Read `./fname`; increment the value; write back to `./fname`
    '''
    fpath = Path.cwd() / fname
    with fpath.open("r", encoding="utf8") as f:

        try:
            value = int(f.read())
        except:
            value = 0

        f.close()

    print(f"Read: {value}")
    value += 1

    with fpath.open("w", encoding="utf8") as f:
        f.write(str(value))
        f.close()

    print(f"Write: {value}")

def read(fname: str = "file.txt") -> int | None:
    '''
    Read `./fname` if it exists otherwise return `None`
    '''
    fpath = Path.cwd() / fname
    if not fpath.exists():
        print(f"{fpath} does not exist!")

    else:
        with open(fpath, "r", encoding="utf8") as f:
            res = int(f.read())
            f.close()

        return res

if __name__ == "__main__":
    print("Do instead:")
    print("$ python")
    print(">>> import interact")
    print(">>> interact.get_increment_set()")
    print(">>> interact.read()")
