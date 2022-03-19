from tkinter import *
from helper.costCalc import *
from helper.N_J import *
from helper.treePatch import *
from helper.editScript import *
from pprint import pprint

xmlFile = "sample/onlyTag/Sample1/SampleDoc1.xml"
xmlFile2 = "sample/onlyTag/Sample1/SampleDoc2.xml"


treeA = ET.parse(xmlFile)  # xml to tree
rootA = treeA.getroot()
treeB = ET.parse(xmlFile2)  # xml to tree
rootB = treeB.getroot()

dict = {}
NJ1 = NJ(rootA, rootB, "A", "B", dict)
pprint(dict)
print(NJ1)

ES = getEditScript(dict, rootA, rootB, "A", "B")
print(reverseArray(ES))

treePatch(rootA, rootB, reverseArray(ES))
ET.ElementTree(rootA).write("a.xml")

dict = {}
NJ2 = NJ(rootA, rootB, "A", "B", dict)
print(NJ2)

EStoXML(ES)

xml = "ES.xml"

print(XMLtoES(xml))

# root = Tk()
# while True:
#     root.mainloop()
