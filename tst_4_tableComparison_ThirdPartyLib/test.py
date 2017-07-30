import xlrd
import sys
source(findFile("scripts", "common.py"))

def init():
    launchApp()

def cleanup():
    test.log("Reached end")


def main():
    try:
       if object.exists(":SwingSet2_JFrame"):
           
           #Extract data From AUT
           mouseClick(waitForObject(":Table Toggle"))
           table = waitForObject(":JavaTable")
           model = table.getModel()
           rowsInJTable = table.rowcount
           colsInJTable = table.columncount
           
           #Extract data from Excel
           book = xlrd.open_workbook("testdata\\expectedTableContents.xls")
           sheet = book.sheet_by_index(0)
           rowsInExcel=sheet.nrows
           colsInExcel=sheet.ncols
           
           #Row Count should be same
           test.compare(rowsInJTable, rowsInExcel, "Row count in Excel and Table should match")
           
           #Column Count should be same
           test.compare(colsInJTable, colsInExcel, "Column count in Excel and Table should match")
           
           ##Data should be same
           for row in range(rowsInJTable):
               xlRow = sheet.row(row)
               for col in range(colsInJTable):
                   valueFromAUT=str(model.getValueAt(row,col))
                   valueFromXL=str(sheet.cell(row,col).value)
                   if(col==5):
                       test.verify(valueFromAUT.find(valueFromXL)>0, "Value in AUT and Excel should match at " + str(row) + "," + str(col))
                   else:
                       test.compare(valueFromAUT, valueFromXL, "Value in AUT and Excel should match at " + str(row) + "," + str(col))
       else:
            test.fatal("Application not launched")
    except Exception, e:
        test.fail("Exception occurred - " + str(sys.exc_info()[0]) + " - " + str(sys.exc_info()[1])+ " at Line no. " + str(sys.exc_info()[2].tb_lineno))
    finally:
        book.release_resources()