nums = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 11, 12]
target = 27


def is_correct(result):
    flat = sorted([item for sublist in result for item in sublist])
    if flat != nums:
        return False

    def rows():
        return sum(result[0]) == target and \
               sum(result[1]) == target and \
               sum(result[2]) == target and \
               sum(result[3]) == target

    def cols():
        return sum([result[0][0], result[1][0], result[2][0], result[3][0]]) == target and \
               sum([result[0][1], result[1][1], result[2][1], result[3][1]]) == target and \
               sum([result[0][2], result[1][2], result[2][2], result[3][2]]) == target and \
               sum([result[0][3], result[1][3], result[2][3], result[3][3]]) == target

    def boxes():
        return sum([result[0][0], result[0][1], result[1][0], result[1][1]]) == target and \
               sum([result[0][2], result[0][3], result[1][2], result[1][3]]) == target and \
               sum([result[2][0], result[2][1], result[3][0], result[3][1]]) == target and \
               sum([result[2][2], result[2][3], result[3][2], result[3][3]]) == target

    def diagonals():
        return sum([result[0][0], result[1][1], result[2][2], result[3][3]]) == target and \
               sum([result[0][3], result[1][2], result[2][1], result[3][0]]) == target

    def center():
        return result[1][1] + result[1][2] + result[2][1] + result[2][2] == target

    def corners():
        return result[0][0] + result[0][3] + result[3][0] + result[3][3] == target

    return corners() and center() and diagonals() and rows() and cols() and boxes()


def run():
    def is_dup(row1, row2):
        return row1[0] == row2[0] and row1[1] == row2[1] and row1[2] == row2[2] and row1[3] == row2[3]

    rows = list()
    # calculate all the ways to make target with 4 numbers from nums
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                for l in range(len(nums)):
                    if len({i, j, k, l}) != 4:
                        continue

                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        row = [nums[i], nums[j], nums[k], nums[l]]
                        dup = False
                        for r in rows:
                            if is_dup(row, r):
                                dup = True
                                break
                        if not dup:
                            rows.append([nums[i], nums[j], nums[k], nums[l]])

    print(rows)
    print(len(rows))

    corner_pairs = []
    center_pairs = []

    def corners(row1, row2):
        return row1[0] + row1[3] + row2[0] + row2[3] == target

    def center(row1, row2):
        return row1[1] + row1[2] + row2[1] + row2[2] == target

    print("Start finding pairs")
    # Create all the possible sets of corners and centers
    for i in range(len(rows)):
        for j in range(i, len(rows)):
            if i == j:
                continue

            if corners(rows[i], rows[j]):
                corner_pairs.append([rows[i], rows[j]])
            if center(rows[i], rows[j]):
                center_pairs.append([rows[i], rows[j]])

    print("Start finding solutions", len(corner_pairs), len(center_pairs))
    for corner_pair in corner_pairs:
        for center_pair in center_pairs:
            result = [corner_pair[0], center_pair[0], center_pair[1], corner_pair[1]]
            if is_correct(result):
                print(result)


run()
