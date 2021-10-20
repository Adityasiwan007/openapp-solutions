from tests import ALG_ONE_TESTS


def get_total_identical_pairs(nums):
    """
    Given an array of integers
    Return the amount of "GOOD" pairs in the array
    Where list_of_numbers[a] == list_of_numbers[b] and a < b
    """

    """Setting count to 0"""
    count=0 
    for i in range(len(nums)):
        "Using i+1 to avoid extra running of loop."
        for j in range(i+1, len(nums)):
            "matching the value for Good pair"
            if (nums[i] == nums[j]):
                "Counter for each condition verification"
                count += 1  
        
    return count


if __name__ == "__main__":
    # The below runs tests found in test.py against your solution in get_total_identical_pairs
    # Uncomment it all until your happy to test
    for test in ALG_ONE_TESTS:
        result = get_total_identical_pairs(
            test.get('list_of_numbers'),
        )
        expected_result = test.get('expected_result')
        assert result == expected_result, "This test expected {} pairs, but it returned {} pairs".format(
            result,
            expected_result,
        )
