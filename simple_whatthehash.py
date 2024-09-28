import hashlib
class Color:

    """Class representing colors"""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[54m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[91m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def color_reset():
    print(Color.END)

def verify_checksu():
    print("Enter Checksum Provided by Authorized Distrubutor or Developer...")
    given_checksum = input()
    print(Color.PURPLE + "You entered: " + given_checksum)
    print(Color.GREEN + "Calculated :" + sha256_hash.hexdigest())
    if given_checksum == sha256.hexdigest():
        safe_result = (Color.BOLD + Color.GREEN + "Checksum Verfied! File is OK.")
        print(safe_result)
    else:
        bad_result = (Color.BOLD + Color.RED + "WARNING!!! Checksum is NOT verified. Verify checksum entry with the checuksum source. Verifiy correct file or package. This is a potentially harmful file or package! Do not proceed! Notify developer or distributor if correct software is being checked and teh calculated checksum continues to not match checksum from developer or distributor.")
        print(bad_result)
        color_reset()


