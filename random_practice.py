from typing import List


def solveQueries(nums: List[int], queries: List[int]) -> List[int]:
    min_distance = float('inf')
    answer = []
    for i in range(len(queries)):
        target_index = queries[i]
        for j in range(len(nums)):
            if j != target_index and nums[j] == nums[target_index]:
                min_distance = min(min_distance, abs(target_index - j), (len(nums) - target_index + j) if target_index > j else abs(len(nums) - j -target_index))
        if min_distance == float('inf'):
            answer.append(-1)
            continue
        answer.append(min_distance)
        min_distance = float('inf')
    return answer

ans = solveQueries([6,12,17,9,16,7,6], [5,6,0,4])