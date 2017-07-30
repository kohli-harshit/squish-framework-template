# Behavior Driven Demo
Feature: Theme Updation feature in my Swing App

    As an app user, I want to be able to change the look and feel of my application by switching available themes

	@Smoke @Regression
    Scenario: Theme updation to Aqua

        Given I'm on the home window
          And the background color of the Frame Demo window is not '-6710887'
         When I select the theme 'Aqua'
         Then the background color of the Frame Demo window should become '-6710887'
         
    @Regression
    Scenario Outline: Multiple Themes Check
        Given I'm on the home window
        And the background color of the Frame Demo window is not '<themecolor>'
        When I select the theme '<theme>'
        Then the background color of the Frame Demo window should become '<themecolor>'
        Examples:
        	|theme	|themecolor	|
        	|Aqua	|-6710887	|