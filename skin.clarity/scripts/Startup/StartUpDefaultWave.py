import shutil
 
new_StartUp = 'Q://skin/rapier-clarity-mod/scripts/Startup/Startup.xml'
old_StartUp = 'Q://skin/rapier-clarity-mod/720p/Startup.xml'

new_sounds = 'Q://skin/rapier-clarity-mod/scripts/Startup/sounds.xml'
old_sounds = 'Q://skin/rapier-clarity-mod/sounds/sounds.xml'

######################################################################################
##############################  REPLACE FILES  #######################################
######################################################################################

shutil.copyfile(new_StartUp,old_StartUp)
shutil.copyfile(new_sounds,old_sounds)
