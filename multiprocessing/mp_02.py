import time
import multiprocessing as mp


def do_something(t=2):
    print(f"Sleeping {t} second(s)...")
    time.sleep(t)
    print("Done sleeping...")


def main():

    # Record start time
    start = time.perf_counter()

    # Initialize process objects
    p_one = mp.Process(target=do_something)
    p_two = mp.Process(target=do_something)
    p_three = mp.Process(target=do_something)

    # Call start method on processes
    p_one.start()
    p_two.start()
    p_three.start()

    p_one.join()
    p_two.join()
    p_three.join()

    # Record stop time
    stop = time.perf_counter()

    # Print out time passed
    print(f"Finished in {round(stop - start, 1)} second(s)")


if __name__ == "__main__":
    main()