cmake_minimum_required(VERSION 3.21)
project(challengers)

set(CMAKE_CXX_STANDARD 17)

include_directories(.)
include_directories(hackerrank)
include_directories(interviewbit)
include_directories(leetcode)
include_directories(talenthub)

add_executable(hr_making-anagrams hackerrank/cracking-coding-interview/making-anagrams/solution.c)

add_executable(lc64 leetcode/64.minimum-path-sum.cpp)
add_executable(lc135 leetcode/135.candy.cpp)
add_executable(lc155 leetcode/155.min-stack.cpp)
add_executable(lc169 leetcode/169-majority-element/Solution.cc)
add_executable(lc212 leetcode/212.word-search-ii.cpp)
add_executable(lc239 leetcode/239.sliding-window-maximum.cpp)
add_executable(lc283 leetcode/283-move-zeroes/Solution.cc)
add_executable(lc300 leetcode/300-longest-increasing-subsequence/Solution.cpp)
add_executable(lc303 leetcode/303.range-sum-query-immutable.cpp)
add_executable(lc355 leetcode/355.design-twitter.cpp)
add_executable(lc460 leetcode/460.lfu-cache.cpp)
add_executable(lc1658 leetcode/1658.minimum-operations-to-reduce-x-to-zero.cpp)

add_executable(th9 talenthub/09-biggest_symmetric_subseq/solution.c)

add_executable(ib_distribute-canndy interviewbit/distribute-candy/DistributeCandy.cc)
