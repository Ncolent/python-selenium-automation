# Created by jblai at 9/15/2023
Feature: Check order page


  Scenario: Open Sign-in page via orders button
    Given Open Amazon Page
    When Click Orders
    Then Verify Sign-in page is opened