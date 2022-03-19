from src.costCalc import *
from xml.etree.ElementTree import *


def reverseArray(array):
    result = []
    i = len(array) - 1
    while i >= 0:
        result.append(array[i])
        i -= 1
    return result


# After getting the edit matrices using NJ algorithm, the matrices
# are stored in a dictionary with their name as key
# using them will get the edit script by tranversing them back
# Note that the result should be flipped
# this method take into considaration only tags


def getTreeEditScript_Tag(matricesDic, A, B, nameA, nameB):

    keyDic = nameA + "/" + nameB
    editScript = []
    matrix = matricesDic.get(keyDic)

    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    while row > 0 and col > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        subTreeBName = nameB + "-" + str(col - 1)

        subTreeA = findSubTree_Tag(A, subTreeAName)
        subTreeB = findSubTree_Tag(B, subTreeBName)

        if matrix[row][col] == (matrix[row - 1][col] + costDelete_Tag(subTreeA, B)):
            editScript.append(("Del", subTreeAName))
            row = row - 1
        elif matrix[row][col] == matrix[row][col - 1] + costInsert_Tag(subTreeB, A):
            editScript.append(("Ins", nameA, subTreeBName, col - 1))
            col = col - 1
        else:
            editScript += getTreeEditScript_Tag(
                matricesDic, A, B, subTreeAName, subTreeBName
            )
            row = row - 1
            col = col - 1

    while row > 0:
        subTreeAName = nameA + "-" + str(row - 1)
        editScript.append(("Del", subTreeAName))
        row = row - 1

    while col > 0:
        subTreeBName = nameB + "-" + str(col - 1)
        editScript.append(("Ins", nameA, subTreeBName, col - 1))
        col = col - 1

    if row == 0 and col == 0:
        if matrix[row][col] == 1:
            editScript.append(("Upd", nameA, nameB))

    return editScript


# def EStoXML(ES):
#     top = Element("EditScript")
#     for ele in ES:
#         tag = SubElement(top, ele[0])
#         if ele[0] == "Upd":
#             tag.set("nameA", ele[1])
#             tag.set("nameB", ele[2])
#         if ele[0] == "Ins":
#             tag.set("nameA", ele[1])
#             tag.set("subTreeBName", ele[2])
#             tag.set("col-1", str(ele[3]))
#         if ele[0] == "Del":
#             tag.set("subTreeAName", ele[1])

#     tree = ElementTree(top)
#     tree.write("ES.xml")
#     return "XMl file created"


# def XMLtoES(xmlFile):
#     tree = ET.parse(xmlFile)
#     root = tree.getroot()

#     ES = []
#     for child in root:
#         tuple = ()
#         tuple += (child.tag,)
#         if child.tag == "Upd":
#             tuple += (child.get("nameA"),)
#             tuple += (child.get("nameB"),)
#         if child.tag == "Del":
#             tuple += (child.get("subTreeAName"),)
#         if child.tag == "Ins":
#             tuple += (child.get("nameA"),)
#             tuple += (child.get("subTreeBName"),)
#             tuple += (int(child.get("col-1")),)

#         ES.append(tuple)

#     print(ES)
#     return ES