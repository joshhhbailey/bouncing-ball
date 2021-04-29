# Author: [REDACTED]
# Last Modified: 04/01/21
# Title: Staircase Generator
# Description: Allows the user to specify the dimensions and
#              subdivisions of each stair, the number of stairs they wish to
#              generate, and whether the staircase is open or closed.

import maya.cmds as cmd

class StaircaseWindow():
    def __init__(self):
        """[Initialises the Staircase Generator window UI]
        """
        self.myStaircaseWindow = cmd.window(title = "Staircase Generator", widthHeight = (400, 293), sizeable = False)
        layout = cmd.columnLayout(adjustableColumn = True)
      
        # Quantity
        self.stairs = cmd.intSliderGrp(label = "Number of Stairs:", value = 1, minValue = 1, maxValue = 10, field = True, fieldMaxValue = 100)
        cmds.separator(height = 10, style = 'none')
        
        # Dimensions
        self.width = cmd.floatSliderGrp(label = "Stair Width:", value = 1, minValue = 0, maxValue = 10, field = True, fieldMaxValue = 100, precision = 4)
        self.depth = cmd.floatSliderGrp(label = "Stair Depth:", value = 1, minValue = 0, maxValue = 10, field = True, fieldMaxValue = 100, precision = 4)
        self.height = cmd.floatSliderGrp(label = "Stair Height:", value = 1, minValue = 0, maxValue = 10, field = True, fieldMaxValue = 100, precision = 4)
        cmds.separator(height = 10, style = 'none')
        
        # Divisions
        self.widthSubDiv = cmd.intSliderGrp(label = "Stair Width divisions:", value = 1, minValue = 1, maxValue = 50, field = True, fieldMaxValue = 100)
        self.depthSubDiv = cmd.intSliderGrp(label = "Stair Depth divisions:", value = 1, minValue = 1, maxValue = 50, field = True, fieldMaxValue = 100)
        self.heightSubDiv = cmd.intSliderGrp(label = "Stair Height divisions:", value = 1, minValue = 1, maxValue = 50, field = True, fieldMaxValue = 100)
        cmds.separator(height = 10, style = 'none')
        
        # Staricase Type
        self.type = cmd.radioButtonGrp(numberOfRadioButtons = 2, label = "Staircase Type: ", labelArray2 = ["Open", "Closed"], select = 1)
        cmds.separator(height = 10, style = 'none')
        
        # Merge / History
        self.mergeHistory = cmd.radioButtonGrp(numberOfRadioButtons = 2, label = "Merge / Delete History? ", labelArray2 = ["Yes", "No"], select = 1)
        cmds.separator(height = 10, style = 'none')
        
        # Buttons
        cmd.button(label = "Create", width = 100, command = self.createGeometry)
        cmd.button(label = "Exit", width = 100, command = self.exit)
        
        cmd.showWindow()
    
    # Getters  
    def getStairs(self):
        """[Return the Number of Stairs, input by the user]

        Returns:
            [integer]: [Number of Stairs]
        """
        _stairs = cmd.intSliderGrp(self.stairs, query = True, value = True)
        return _stairs
        
    def getWidth(self):
        """[Return the Width, input by the user]

        Returns:
            [float]: [Width of each step]
        """
        _width = cmd.floatSliderGrp(self.width, query = True, value = True)
        return _width
        
    def getDepth(self):
        """[Return the Depth, input by the user]

        Returns:
            [float]: [Depth of each step]
        """
        _depth = cmd.floatSliderGrp(self.depth, query = True, value = True)
        return _depth
        
    def getHeight(self):
        """[Return the Height, input by the user]

        Returns:
            [float]: [Height of each step]
        """
        _height = cmd.floatSliderGrp(self.height, query = True, value = True)
        return _height
        
    def getWidthSubDiv(self):
        """[Return the Width Divisions, input by the user]

        Returns:
            [integer]: [Width divisions of each step]
        """
        _widthSubDiv = cmd.intSliderGrp(self.widthSubDiv, query = True, value = True)
        return _widthSubDiv
        
    def getDepthSubDiv(self):
        """[Return the Depth Divisions, input by the user]

        Returns:
            [integer]: [Depth divisions of each step]
        """
        _depthSubDiv = cmd.intSliderGrp(self.depthSubDiv, query = True, value = True)
        return _depthSubDiv
    
    def getHeightSubDiv(self):
        """[Return the Height Divisions, input by the user]

        Returns:
            [integer]: [Height divisions of each step]
        """
        _heightSubDiv = cmd.intSliderGrp(self.heightSubDiv, query = True, value = True)
        return _heightSubDiv
        
    def getType(self):
        """[Return the staircase Type, input by the user]

        Returns:
            [integer]: [Type of staircase, 0 = Open, 1 = Closed]
        """
        _type = cmd.radioButtonGrp(self.type, query = True, select = True)
        return _type
        
    def getMergeHistory(self):
        """[Return the Merge / Delete History, input by the user]

        Returns:
            [integer]: [Merge / Delete History]
        """
        _mergeHistory = cmd.radioButtonGrp(self.mergeHistory, query = True, select = True)
        return _mergeHistory
        
        
    # Create geometry
    def createGeometry(self, *args):
        """[Creates and iterates through all stairs applying the user specified inputs.]
        """
        objGroup = []
        # Open
        if self.getType() == 1:
            for i in range(self.getStairs()):
                obj = cmd.polyCube(name = "stair_1", width = self.getWidth(), height = self.getHeight(),
                                   depth = self.getDepth(), subdivisionsX = self.getWidthSubDiv(),
                                   subdivisionsY = self.getHeightSubDiv(), subdivisionsZ = self.getDepthSubDiv())  
                cmd.move(0, (i * self.getHeight()) + self.getHeight() / 2, i * self.getDepth())
                objGroup.append(obj[0])
        
        # Closed
        else:
            for i in range(self.getStairs()):
                obj = cmd.polyCube(name = "stair_1", width = self.getWidth(), height = self.getHeight() * (i + 1),
                                   depth = self.getDepth(), subdivisionsX = self.getWidthSubDiv(),
                                   subdivisionsY = self.getHeightSubDiv() * (i + 1), subdivisionsZ = self.getDepthSubDiv())  
                cmd.move(0, (i * self.getHeight() - ((self.getHeight() / 2) * i)) + self.getHeight() / 2, i * self.getDepth())
                objGroup.append(obj[0])
        
        # Merge and delete history
        if self.getMergeHistory() == 1:
            cmd.select(objGroup)
            combined = cmd.polyCBoolOp(operation = 1, preserveColor = 0, name = "Staircase")
            cmd.delete(combined, constructionHistory = 1)
            
        # Group stairs
        else:
            cmd.group(objGroup, name = "Staircase")
            
    # Exit window
    def exit(self, *args):
        """[Closes the Staircase Generator window UI]
        """
        cmd.deleteUI(self.myStaircaseWindow)
    
# Create window
# If a window is already open, close it and open a new on
# If no window is already open, open one
try:
    cmds.deleteUI(app.myStaircaseWindow)
    app = StaircaseWindow()
except:
    app = StaircaseWindow()
