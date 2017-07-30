import sys
source(findFile("scripts", "common.py"))
source(findFile("scripts", "global.py"))

def init():
    launchApp()

def cleanup():
    test.log("Reached end")


def main():    
    
    try:
       #Defining Real name of main window
       mainwindow = "{window=':SwingSet2_JFrame' type='javax.swing.JLayeredPane'}"
       if object.exists(mainwindow):
           
           #This count will determine total number of frames
           originalCount = 0
                       
           internalFrameDescription="{caption~='^Frame .*' container=':SwingSet2.Internal Frames Demo_TabProxy' type='javax.swing.JInternalFrame' visible='true'}"
           #Fetching all objects of the given real name using the method find_all_objects() from commom.py
           frameList = find_all_objects(internalFrameDescription)
           originalCount = len(frameList)
           
           #Adding a new frame 
           addFrame(0)
            
           frameList = find_all_objects(internalFrameDescription)
           updatedCount = len(frameList)
            
           #Checking if the number of frames increase by 1
           test.compare(originalCount+1,updatedCount)
           
           #Checking if the Resizable checkbox is already check and then unchecking it  
           if(findObject(":Internal Frame Generator.Resizable_JCheckBox").selected == True):
               mouseClick(waitForObject(":Internal Frame Generator.Resizable_JCheckBox"))

           #Checking if the Maximizable checkbox is already check and then unchecking it     
           if(findObject(":Internal Frame Generator.Maximizable_JCheckBox").selected == True):
               mouseClick(waitForObject(":Internal Frame Generator.Maximizable_JCheckBox"))
     
           addFrame(0)
           
           frameList = find_all_objects(internalFrameDescription)
           newUpdatedCount = len(frameList)
           
           test.compare(updatedCount+1,newUpdatedCount)
           
           #Fetching the latest frame included using descriptive programming 
           latestFrame = "{caption~='^Frame " + str(newUpdatedCount-1) + "*' container=':SwingSet2.Internal Frames Demo_TabProxy' type='javax.swing.JInternalFrame' visible='true'}"
           
           #The new frame added should not be resizable and maximizable  
           test.compare(findObject(latestFrame).resizable,False)
           test.compare(findObject(latestFrame).maximizable,False)
       else:
            test.fatal("Application not launched")
    except Exception, e:
        #Printing error log in case of any exception  
        test.fail("Exception occurred - " + str(sys.exc_info()[0]) + " - " + str(sys.exc_info()[1])+ " at Line no. " + str(sys.exc_info()[2].tb_lineno))

#Method defined to add a new frame
def addFrame(frameNumber):
    clickButton(waitForObject("{caption='' container=':Internal Frames Demo.Internal Frame Generator_JInternalFrame' occurrence='" + str(frameNumber) + "' type='javax.swing.JButton' visible='true'}"))