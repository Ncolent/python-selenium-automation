# Created by jblai at 10/5/2023
Feature: Scenario: User can open and close Amazon Privacy Notice

 Scenario: open and interact with multiple windows
Given Open Amazon T&C page
 When Store original windows
 And Click on Amazon Privacy Notice link
# And Switch to the newly opened window
# Then Verify Amazon Privacy Notice page is opened
# And User can close new window and switch back to original