# import os
from pathlib import Path

CWD = Path.cwd()
HOME = Path.home()

# TODO check subpath

def aux(path: Path, acc: int) -> int | None:
    if path != HOME:
        if path != CWD:
            aux(path.parent, acc + 1)
        else:
            return acc

def cwd_depth(fpath: Path) -> int | None:

    acc = 0
    if fpath == CWD:
        return 0

    elif fpath == HOME:
        return None

    else:
        acc += 1
        return cwd_depth(fpath.parent)

if __name__ == "__main__":
    print(f"res:  {aux(path=CWD, acc=0)}")
    print(f"cwd:  {CWD}")
    # print(f"loc:  {CWD / __file__}")
    print(f"home: {HOME}")
