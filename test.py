def test():
    win = 0
    fail = 0
    #1
    from rubix_cube import cube
    testCube1 = cube(state="solved")
    
    # Compare the state of the cube, not the cube object itself
    expected_state = [
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
    ]
    
    # Compare testCube1.state with expected_state
    if testCube1.state != expected_state:
        fail += 1
        print("""test 1: fail, expected [
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
    ] but got """ + str(testCube1.state))
    else:
        win += 1
    #2
    if testCube1.state[0][0][0] != 1:
        fail += 1
        print("""test 2: fail, expected 1 but got """ + str(testCube1.state[0][0][0]))
    else:
        win += 1

    print(f"Passed tests: {win}")
    print(f"Failed tests: {fail}")

test()