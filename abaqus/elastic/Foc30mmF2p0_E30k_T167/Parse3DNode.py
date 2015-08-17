import sys

from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *
from array import array

odbFile = str(sys.argv[1])
instance = str(sys.argv[2])
nodeset = str(sys.argv[3])
variable = str(sys.argv[4])
step = str(sys.argv[5])
precision = str(sys.argv[6])
resultFile = odbFile+'parse'

# open odb file
odb = openOdb(path=odbFile)

# get handle to model
hNodeSet = odb.rootAssembly.instances[instance].nodeSets[nodeset]

# read node coordinates blood
print('Start reading node information\n')
numberOfNode = array('i')
nodeLabel = array('i')
nodeCoordinate = array('d')
for node in hNodeSet.nodes:
    nodeLabel.append(node.label)
    nodeCoordinate.append(node.coordinates[0])
    nodeCoordinate.append(node.coordinates[1])
    nodeCoordinate.append(node.coordinates[2])
numberOfNode.append(nodeLabel.buffer_info()[1])
print('Finish reading node information\n')

# read variable
print('Start reading variable information\n')
numberOfFrame = array('i')
frameTime = array('d')
frameNodeLabel = array('i')
frameNodeVariable = array('d')
frameCounter = 0
for currentFrame in odb.steps[step].frames:
    print('Read frame {0}\n'.format(frameCounter))
    frameCounter = frameCounter+1
    frameTime.append(currentFrame.frameValue)
    value = currentFrame.fieldOutputs[variable].getSubset(region=hNodeSet).values
    for v in value:
        frameNodeLabel.append(v.nodeLabel)
        if precision == "double":
            frameNodeVariable.append(v.dataDouble[0])
            frameNodeVariable.append(v.dataDouble[1])
            frameNodeVariable.append(v.dataDouble[2])
        if precision == "single":
            frameNodeVariable.append(v.data[0])
            frameNodeVariable.append(v.data[1])
            frameNodeVariable.append(v.data[2])
numberOfFrame.append(frameTime.buffer_info()[1])
print('Finish reading variable information\n')

# construct header
type = array('c','node')
typeStrSize = array('i')
typeStrSize.append(type.buffer_info()[1])
odbFile = array('c',odbFile)
odbFileStrSize = array('i')
odbFileStrSize.append(odbFile.buffer_info()[1])
instance = array('c',instance)
instanceStrSize = array('i')
instanceStrSize.append(instance.buffer_info()[1])
nodeset = array('c',nodeset)
nodesetStrSize = array('i')
nodesetStrSize.append(nodeset.buffer_info()[1])
variable = array('c',variable)
variableStrSize = array('i')
variableStrSize.append(variable.buffer_info()[1])
step = array('c',step)
stepStrSize = array('i')
stepStrSize.append(step.buffer_info()[1])
precision = array('c',precision)
precisionStrSize = array('i')
precisionStrSize.append(precision.buffer_info()[1])

# open file
f = open(resultFile,'wb+')
# write header
typeStrSize.tofile(f)
type.tofile(f)
odbFileStrSize.tofile(f)
odbFile.tofile(f)
instanceStrSize.tofile(f)
instance.tofile(f)
nodesetStrSize.tofile(f)
nodeset.tofile(f)
variableStrSize.tofile(f)
variable.tofile(f)
stepStrSize.tofile(f)
step.tofile(f)
precisionStrSize.tofile(f)
precision.tofile(f)

# write node information
numberOfNode.tofile(f)
nodeLabel.tofile(f)
nodeCoordinate.tofile(f)

# write variables
numberOfFrame.tofile(f)
frameTime.tofile(f)
frameNodeLabel.tofile(f)
frameNodeVariable.tofile(f)

# close file
f.close()
