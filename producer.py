import greenstalk


def main():
    " A Beanstalkd producer. "
    with greenstalk.Client(('127.0.0.1', 11300)) as client:
        job = client.put('Hello')
        print(job)


if __name__ == "__main__":
    main()
