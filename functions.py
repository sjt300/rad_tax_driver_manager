from pathlib import Path


def check_db():
    """
    simply checks that the assets/db folder exists
    if so, launch the program, if not, display install instructions
    :return:
    """
    if not Path("./assets/db/").exists():
        return False
    else:
        return True


if __name__ == '__main__':
    check_db()
