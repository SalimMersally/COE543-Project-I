from helper.costCalc import *
from helper.treePatch import *
import numpy as np

dict1 = {
    "AB": [[0, 4, 5], [1, 4, 4], [2, 3, 4]],
    "A-1B-1": [[1, 2], [2, 3], [3, 4]],
    "A-1-1B-1-1": [[1, 2, 3]],
    "A-1-2B-1-1": [[1, 2, 3]],
    "A-1B-2": [[0, 1, 2], [1, 0, 1], [2, 1, 0]],
    "A-1-1B-2-1": [[0]],
    "A-1-1B-2-2": [[1]],
    "A-1-2B-2-1": [[1]],
    "A-1-2B-2-2": [[0]],
    "A-2B-1-1": [[1, 2]],
    "A-2B-2": [[1, 2, 3]],
}


def getEditScript(matricesDic, A, B, nameA, nameB):

    keyDic = nameA + nameB
    editScript = []
    matrix = matricesDic.get(keyDic)

    print(np.array(matrix))

    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    while row > 0 and col > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        subTreeBName = nameB + "-" + str(col - 1)

        print(subTreeAName, subTreeBName)

        subTreeA = findSubTree(A, subTreeAName)
        subTreeB = findSubTree(B, subTreeBName)

        print(subTreeA)
        print(subTreeB)

        if matrix[row][col] == (matrix[row - 1][col] + costDelete(subTreeA, B)):
            editScript.append("Del")
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsert(subTreeB, A):
            editScript.append("Ins")
            col = col - 1
        else:
            editScript += getEditScript(matricesDic, A, B, subTreeAName, subTreeBName)
            row = row - 1
            col = col - 1
    # end of first while loop

    while row > 0:
        editScript.append("Del")
        row = row - 1
    # end of the second loop

    while col > 0:
        editScript.append("Ins")
        col = col - 1
    # end of the third loop

    if row == 0 and col == 0:
        if matrix[row][col] == 1:
            editScript.append("Upd")

    return editScript
