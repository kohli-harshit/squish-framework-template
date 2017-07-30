# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import __builtin__



@Given("I'm on the home window")
def step(context):
    startApplication("SwingSet2.jar")
    waitForObject(":SwingSet2_JFrame").setExtendedState(java_awt_Frame.MAXIMIZED_BOTH)
    snooze(2)

@Given("the background color of the Frame Demo window is not '|integer|'")
def step(context,colorcode):
    test.log("Color Value",str(waitForObjectExists(":SwingSet2_JTabbedPane").background.colorspace))
    test.xcompare(waitForObjectExists(":SwingSet2_JTabbedPane").background.rgb, colorcode)
    snooze(1)

@When("I select the theme '|word|'")
def step(context,menuItemToSelect):
    activateItem(waitForObjectItem(":SwingSet2_JMenuBar", "Themes"))
    activateItem(waitForObjectItem(":Themes_JMenu", menuItemToSelect))

@Then("the background color of the Frame Demo window should become '|integer|'")
def step(context,colorcode):
    snooze(1)
    test.log("Color Value",str(waitForObjectExists(":SwingSet2_JTabbedPane").background.colorspace))
    test.compare(waitForObjectExists(":SwingSet2_JTabbedPane").background.rgb, colorcode)
