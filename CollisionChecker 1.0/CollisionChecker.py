import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

def collisioncheck(*pArgs):
	
	coll_frames = []
	
	def goThroughMesh(iter):
		lix =[]
		liz =[]
		liy = []
		while(meshIter.isDone() == 0):
			pt = OpenMaya.MPoint()
			pt = meshIter.position(OpenMaya.MSpace.kWorld)
			vertIndex = meshIter.index()
			lix.append(pt.x)
			liy.append(pt.y)
			liz.append(pt.z)
			meshIter.next()
		return lix, liy, liz
	
	def maxMin(lix, liy, liz):
		maxpt = OpenMaya.MPoint()
		minpt = OpenMaya.MPoint()
		maxx = max(lix)
		maxy = max(liy)
		maxz = max(liz)
		minx = min(lix)
		miny = min(liy)
		minz = min(liz)
		maxpt.x = maxx 
		maxpt.y = maxy
		maxpt.z = maxz
		minpt.x = minx 
		minpt.y = miny
		minpt.z = minz 
		return maxpt, minpt


	
	startTime = cmds.playbackOptions(query = True , minTime = True)
	endTime = cmds.playbackOptions(query = True , maxTime = True)
	
	
	for time in range(startTime , endTime+1):
		cmds.currentTime(time)	
		
		intersects = False
		stat = OpenMaya.MStatus.kSuccess
		selection = OpenMaya.MSelectionList()
		OpenMaya.MGlobal.getActiveSelectionList( selection )
		dagPath = OpenMaya.MDagPath()
		component = OpenMaya.MObject()
		vertIndex = 0
			
		iter = OpenMaya.MItSelectionList(selection)
			
		while(iter.isDone() == 0):
			iter.getDagPath(dagPath,component)
			meshIter = OpenMaya.MItMeshVertex(dagPath, component)
			if stat == OpenMaya.MStatus.kSuccess:
				lix, liy, liz = goThroughMesh(iter)
				maxpt1, minpt1 = maxMin(lix, liy, liz)
				bbox1 = OpenMaya.MBoundingBox(maxpt1, minpt1)
				iter.next()
			iter.getDagPath(dagPath,component)
			meshIter = OpenMaya.MItMeshVertex(dagPath, component)
			lix, liy, liz = goThroughMesh(iter)
			maxpt2, minpt2 = maxMin(lix, liy, liz) 
			bbox2 = OpenMaya.MBoundingBox(maxpt2, minpt2)
			iter.next()
			
		intersects = OpenMaya.MBoundingBox.intersects(bbox1, bbox2)
		
		print time		
		print intersects
		if intersects is True:
			coll_frames.append(time)
		
	cmds.textField('CollisionFrames' , edit = True , tx = str([frame for frame in coll_frames]))

def createUI( pWindowTitle ):
	
	windowID = 'myWindowID'
	
	if cmds.window(windowID , exists = True):
		cmds.deleteUI(windowID)
		
	cmds.window(windowID , title = pWindowTitle , sizeable = False , resizeToFitChildren = True)
	
	cmds.rowColumnLayout( numberOfColumns = 3 , columnWidth =[(1,200) , (2,200) , (3,200)])
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.text(label = '1.Set the frame range')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.text(label = '2.Select the two meshes/bounding boxes')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.text(label = '3.Click the button')
	cmds.separator ( h = 20 , style = 'none')
		
	
	cmds.separator ( h = 30 , style = 'none')	
	cmds.button(label = 'Check Collisions' , command = collisioncheck)
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.text(label = 'Frames with Collisions : ')
	cmds.textField('CollisionFrames')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.showWindow()

createUI('CollisionChecker 1.0')