# Author: [REDACTED]
# Last Modified: 04/01/21
# Title: Rock Generator
# Description: Allows the user to specify the dimensions and
#              subdivisions of each rock fragment, the number
#              of fragments the rock consists of, and their radius.
# Credit: Refactored and modified from Jon Macey's (2020) MEL Rock Generator.
#         Macey, J., 2020. MEL Rock Generator.

import maya.cmds as cmd
import random

class RockWindow():
    def __init__(self):
        """[Initialises the Rock Generator window UI]
        """
        self.myRockWindow = cmd.window(title = "Rock Generator", widthHeight = (400, 218), sizeable = False)
        layout = cmd.columnLayout(adjustableColumn = True)
      
        # Quantity
        self.fragments = cmd.intSliderGrp(label = "Number of Fragments:", value = 10, minValue = 2, maxValue = 25, field = True, fieldMaxValue = 50)
        cmds.separator(height = 10, style = 'none')
        
        # Dimensions
        self.radius = cmd.floatSliderGrp(label = "Median Fragment Radius:", value = 1, minValue = 1, maxValue = 10, field = True, fieldMaxValue = 100, precision = 4)
        self.variation = cmd.intSliderGrp(label = "Radius Variation %:", value = 10, minValue = 0, maxValue = 25, field = True, fieldMaxValue = 100)
        cmds.separator(height = 10, style = 'none')
        
        # Subdivisions
        self.xDiv = cmd.intSliderGrp(label = "Fragment X divisions:", value = 5, minValue = 1, maxValue = 20, field = True, fieldMaxValue = 10)
        self.yDiv = cmd.intSliderGrp(label = "Fragment Y divisions:", value = 5, minValue = 1, maxValue = 20, field = True, fieldMaxValue = 10)
        cmds.separator(height = 10, style = 'none')
        
        # Merge / History
        self.mergeHistory = cmd.radioButtonGrp(numberOfRadioButtons = 2, label = "Merge / Delete History? ", labelArray2 = ["Yes", "No"], select = 1)
        cmds.separator(height = 10, style = 'none')
        
        # Buttons
        cmd.button(label = "Create", width = 100, command = self.createRock)
        cmd.button(label = "Exit", width = 100, command = self.exit)
        
        cmd.showWindow()
        
    # Getters  
    def getFragments(self):
        """[Return the Number of Fragments, input by the user]

        Returns:
            [integer]: [Number of Fragments]
        """
        _fragments = cmd.intSliderGrp(self.fragments, query = True, value = True)
        return _fragments
        
    def getRadius(self):
        """[Return the median fragment radius, input by the user]

        Returns:
            [float]: [Median Fragment Radius]
        """
        _radius = cmd.floatSliderGrp(self.radius, query = True, value = True)
        return _radius
        
    def getVariation(self):
        """[Return the Radius Variation %, input by the user]

        Returns:
            [integer]: [Radius Variation % of each fragment]
        """
        _variation = cmd.intSliderGrp(self.variation, query = True, value = True)
        return _variation
        
    def getXSubDiv(self):
        """[Return the Fragment X divisions, input by the user]

        Returns:
            [integer]: [X divisions of each fragment]
        """
        _xDiv = cmd.intSliderGrp(self.xDiv, query = True, value = True)
        return _xDiv
    
    def getYSubDiv(self):
        """[Return the Fragment Y divisions, input by the user]

        Returns:
            [integer]: [Y divisions of each fragment]
        """
        _yDiv = cmd.intSliderGrp(self.yDiv, query = True, value = True)
        return _yDiv
        
    def getMergeHistory(self):
        """[Return the Merge / Delete History, input by the user]

        Returns:
            [integer]: [Merge / Delete History]
        """
        _mergeHistory = cmd.radioButtonGrp(self.mergeHistory, query = True, select = True)
        return _mergeHistory
                
    # Create Rock
    def createRock(self, *args):
        """[Creates and iterates through all rock fragments applying the user specified inputs.]
        """
        variation = (self.getRadius() / 100) * self.getVariation()
        minRadius = self.getRadius() - variation
        maxRadius = self.getRadius() + variation
        objGroup = []
        
        # Create ALL fragments
        for i in range(0, self.getFragments()):
            randomRadius = random.uniform(minRadius, maxRadius)
            obj = cmd.polySphere(name = "RockFragment", radius = randomRadius,
            subdivisionsX = self.getXSubDiv(), subdivisionsY = self.getYSubDiv())
        
            # Move fragment
            x = random.uniform(-minRadius, minRadius)
            y = random.uniform(-minRadius, minRadius)
            z = random.uniform(-minRadius, minRadius)
            cmd.move(x, y, z)
        
            # Rotate fragment
            rx = random.randint(0, 360)
            ry = random.randint(0, 360)
            rz = random.randint(0, 360)
            cmd.rotate(rx, ry, rz, relative = True)
            
            # Scale fragment
            sx = random.uniform(0, minRadius)
            sy = random.uniform(0, minRadius)
            sz = random.uniform(0, minRadius)
            cmd.scale(sx, sy, sz)
            
            objGroup.append(obj[0])
            
        # Merge and delete history
        if self.getMergeHistory() == 1:
            cmd.select(objGroup)
            combined = cmd.polyCBoolOp(operation = 1, preserveColor = 0, name = "Rock")
            cmd.delete(combined, constructionHistory = 1)
            
        # Group fragments
        else:
            cmd.group(objGroup, name = "Rock")
        
    # Exit window
    def exit(self, *args):
        """[Closes the Rock Generator window UI]
        """
        cmd.deleteUI(self.myRockWindow)
    
# Create window
# If a window is already open, close it and open a new on
# If no window is already open, open one
try:
    cmds.deleteUI(app.myRockWindow)
    app = RockWindow()
except:
    app = RockWindow()
