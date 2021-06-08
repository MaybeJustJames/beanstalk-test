import greenstalk

def main():
    " A Beanstalkd consumer. "
    with greenstalk.Client(('127.0.0.1', 11300)) as client:
        while True:
            job = client.reserve()
            print(job.id, job.body)
            client.delete(job)

if __name__ == "__main__":
    main()
