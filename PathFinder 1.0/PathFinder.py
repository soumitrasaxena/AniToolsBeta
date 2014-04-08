import maya.cmds as cmds

selection = cmds.ls(selection = True)
print selection

startTime = cmds.playbackOptions(query = True , minTime = True)
endTime = cmds.playbackOptions(query = True , maxTime = True)

cmds.currentTime(startTime)

i_x = cmds.getAttr(selection[0]+'.translateX')
i_y = cmds.getAttr(selection[0]+'.translateY')
i_z = cmds.getAttr(selection[0]+'.translateZ')

cmds.curve(d=3 , n = 'curve1' , p = [(i_x , i_y , i_z)])

for time in range(startTime+1 , endTime+1):
	cmds.currentTime(time)
	tX = cmds.getAttr(selection[0]+'.translateX')
	tY = cmds.getAttr(selection[0]+'.translateY')
	tZ = cmds.getAttr(selection[0]+'.translateZ')
	
	cmds.curve('curve1' , a = True , p = [(tX , tY , tZ)])	