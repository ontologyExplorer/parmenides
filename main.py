from api.src.token import get_access_token


def main():
    get_access_token("test@email.com", "test")


if __name__ == "__main__":
    main()
