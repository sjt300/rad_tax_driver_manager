from pathlib import Path
import re


def check_db():  # todo check all files for integrity
    """
    simply checks that the assets/db folder exists
    if so, launch the program, if not, display install instructions
    :return:
    """
    if not Path("./db/").exists():
        return False
    else:
        return True


# used for password checking if valid
# takes password, regular expression to check and the label to alter config based on outcome of check
def check_pass(passwd, check, lbl):
    re_check = re.compile(check)
    if re_check.search(passwd):
        lbl.config(fg='green')
        return True
    else:
        lbl.config(fg='red')
        return False


if __name__ == '__main__':
    check_db()
