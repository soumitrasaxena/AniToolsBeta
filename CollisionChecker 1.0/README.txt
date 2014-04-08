CollisionChecker1.0 
-----------------------------

CollisionChecker 1.0 is a plugin that is aimed at making collision checking a one click job. It checks for collision/intersection between any two meshes over a frame range. Just click on 
'Check' and the script does the rest. It uses the powerful Maya API ( OpenMaya) and uses functions like MBoundingBox , getDagPath , and other powerful functions for the job. It is aimed
at helping animators in getting accurate animations , and saves the time wasted in manually checking for collisions/intersections. 

This is especially useful for character animations , where one needs to check for intersecting meshes.

It works with any mesh shape.

How It Works :
---------------------

1. Select the two meshes you want to check for collisions/intersections.
2. Set the frame range over which you want to check for collisions.
3. Click on Check Collisions.
4. The script returns the frames in which intersection/collision occurs.

Coded in Python for Autodesk Maya. Tested on Maya 2012.

Blog Link : https://medium.com/p/a860267ddc31

Youtube Link : https://www.youtube.com/watch?v=pI4nC7vMrYE
