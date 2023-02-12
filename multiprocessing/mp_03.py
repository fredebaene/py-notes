import time
import multiprocessing as mp


def do_something(t=2):
    print(f"Sleeping {t} second(s)...")
    time.sleep(t)
    print("Done sleeping...")


def main():

    # Record start time
    start = time.perf_counter()

    # Initialize and start process objects
    processes = []

    for _ in range(10):

        p = mp.Process(target=do_something, args=[5.0])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    # Record stop time
    stop = time.perf_counter()

    # Print out time passed
    print(f"Finished in {round(stop - start, 1)} second(s)")


if __name__ == "__main__":
    main()