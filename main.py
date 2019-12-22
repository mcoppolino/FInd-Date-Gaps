# Author Michael Coppolino
# michael_coppolino@brown.edu

import timeit
from find_gaps import find_gaps_v0, find_gaps_v1, find_gaps_v2, find_gaps_v3

TRIALS = 2 * 10**6 # run each version 2m times

def test_all_versions():
    """
    Prints the runtime of all versions
    """

    versions = [
        find_gaps_v0,
        find_gaps_v1,
        find_gaps_v2,
        find_gaps_v3,
    ]

    for idx, version in enumerate(versions):
        assert(find_gaps_v0() == version())
        print("V%i time:" % idx, timeit.timeit(version, number=TRIALS))


def test_final_result():
    """
    Prints the wall clock time of the original version and the final version,
    and prints the percent wall clock time decrease.
    """

    print("Running v0 %i times..." % TRIALS)
    v0_time = timeit.timeit(find_gaps_v0, number=TRIALS)
    print("V0 time:", v0_time, '\n')

    print("Running v3 %i times..." % TRIALS)
    v3_time = timeit.timeit(find_gaps_v3, number=TRIALS)
    print("V3 time:", v3_time, '\n')

    pct_decrease = 100 * (v0_time - v3_time) / v0_time
    print("Wall clock runtime decreased by %.2f%%" % pct_decrease)


def main():
     # test_all_versions()
     test_final_result()

if __name__ == '__main__':
    main()
