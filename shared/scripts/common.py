# -*- coding: utf-8 -*-

def launchApp():
    test.log("Application Path is " + getTestSetting("appPath"))
    startApplication(getTestSetting("appPath"))
    waitForObject(":SwingSet2_JFrame").setExtendedState(java_awt_Frame.MAXIMIZED_BOTH)
    testSettings.logScreenshotOnFail = True
    testSettings.logScreenshotOnError = True
    testSettings.throwOnFailure = True

def getTestSetting(settingname):
    dataset = testData.dataset(findFile("testdata","testsettings.tsv"))
    for row in dataset:
        if(testData.field(row, "setting")==settingname):
            return testData.field(row, "value")
    return "Not Found"