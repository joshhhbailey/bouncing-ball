How to open and use my Rock Generator and Staircase Generator.

How to open:
- Open Maya
- Open Maya Script Editor (bottom right)
- Inside the Script Editor, click File -> Open Script
- Locate the desired script ("Rock_Generator.py" or "Staircase_Generator.py")
- Left click the desired script in the explorer prompt, click "Open"
- Inside the Script Editor, click "ExecuteAll" to run the script


Rock Generator Options:
Number of Fragments - The total number of rock-like shapes you wish to generate
Median Fragment Radius - The median radius of all fragments
Radius Variation % - The percentage of differentiation for fragment radius sizes, based off of the
		     Median Fragment Radius
Fragment X divisions - The number of X-axis divisions each fragment has
Fragment Y divisions - The number of Y-axis divisions each fragment has
Merge / Delete History - Yes = Combine all fragments into a single object and erase their history
			 No = Keep the fragments as seperate objects and maintain their history
Create - Generates the geometry
Exit - Closes the Rock Generator window



Staircase Generator Options:
Number of Stairs - The total number of stairs you wish to generate within your staircase
Width - The width of each step
Depth - The depth of each step
Height - The height of each step
Width Divisions - The number of width divisions each stair has
Depth Divisions - The number of depth divisions each stair has
Height Divisions - The number of height divisions each stair has
Type - Open = The underside of each stair is hollow, creating an empty space under the staircase
       Closed = Have each stair extend to the ground, filling in the underside of the staircase
Merge / Delete History - Yes = Combine all stairs into a single object and erase their history
			 No = Keep the stairs as seperate objects and maintain their history
Create - Generates the geometry
Exit - Closes the Staircase Generator window