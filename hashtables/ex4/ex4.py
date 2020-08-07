def has_negatives(a):
    """
    YOUR CODE HERE
    """
    nums = set(())
    result = []

    for num in a:
        nums.add(num)

        if num != 0:
            if num * -1 in nums:
                if num < 0:
                    result.append(num * -1)
                else:
                    result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
