from bigO import BigO
from random import randint
from sorting_algorithms import *
lib = BigO()
complexity = lib.test(bucketsort, "random")
# complexity = lib.test(countsort_neg, "sorted")
# complexity = lib.test(countsort_neg, "reversed")
# complexity = lib.test(countsort_neg, "partial")
# complexity = lib.test(countsort_neg, "Ksorted")

# lib.test_all(countsort)