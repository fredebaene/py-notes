import time
import multiprocessing as mp


def do_something(t=2):
    print(f"Sleeping {t} second(s)...")
    time.sleep(t)
    print("Done sleeping...")


def main():

    # Record start time
    start = time.perf_counter()

    # Initialize pool of processes
    pool = mp.Pool()

    # Submit tasks
    times = [3.0, 5.0, 2.5]
    pool.map(do_something, times)

    # Record stop time
    stop = time.perf_counter()

    # Print out time passed
    print(f"Finished in {round(stop - start, 1)} second(s)")


if __name__ == "__main__":
    main()