"""temp main"""

from utils.token import get_access_token


def main():
    """main function"""
    get_access_token("test@email.com", "test")


if __name__ == "__main__":
    main()
