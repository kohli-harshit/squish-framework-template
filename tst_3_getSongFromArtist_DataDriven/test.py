import sys
source(findFile("scripts", "common.py"))

def init():
    launchApp()

def cleanup():
    test.log("Reached end")


def main():
    try:
       #Checking if the main window exists using Symbolic name     
       if object.exists(":SwingSet2_JFrame"):
       #Opening the Jtree template            
           mouseClick(waitForObject(":JTreeToggleButton"))
           if not object.exists(":MusicTree"):
               #Stopping the case if the main tree node is not available using test.fatal                
               test.fatal("Music Tree not Found")
               return
           musicTree = findObject(":MusicTree")
           
           #Fetching data values from the artists.tsv file in Test Data folder
           dataset = testData.dataset(findFile("testdata","artists.tsv"))
           #Iterating through the values in the data set            
           for row in dataset:
                #Fetching values from a row according to the column name passed in parameters                 
                genrePath = "Music." + testData.field(row, "Genre")
                artistPath = genrePath + "." + testData.field(row, "Artist")
                try:
                    expand(waitForObjectItem(musicTree,genrePath,5))
                    artistNode =waitForObjectItem(musicTree,artistPath,5) 
                    expand(artistNode)                    
                    artistSongCount=0
                    #Fetching the number of songs for an 'artist'                       
                    for child in object.children(artistNode):
                         expand(child)
                         artistSongCount = artistSongCount + len(object.children(child))
                    test.compare(testData.field(row, "Songs"), str(artistSongCount))
                except Exception, e:
                    test.fail("Error = " + str(e) + ". Artist - " + testData.field(row, "Artist"))           
       else:
            test.fatal("Application not launched")
    except Exception, e:
        test.fail("Exception occurred - " + str(sys.exc_info()[0]) + " - " + str(sys.exc_info()[1])+ " at Line no. " + str(sys.exc_info()[2].tb_lineno))