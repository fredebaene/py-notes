import time


def do_something(t):
    print(f"Sleeping {t} second(s)...")
    time.sleep(t)
    print("Done sleeping...")


def main():
    start = time.perf_counter()
    do_something(2)
    do_something(2)
    do_something(2)
    stop = time.perf_counter()
    print(f"Finished in {round(stop - start, 1)} second(s)")


if __name__ == "__main__":
    main()