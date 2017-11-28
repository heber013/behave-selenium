
Feature: Verify I can navigate to selenium page

@Example1
Scenario: Go to selenium page and verify it is open in the browser
  When I go to "http://www.google.com"
  And I type "Seleniumhq" in the searchbox
  And I press "ENTER" in the searchbox
  And I click on "www.seleniumhq.org/" link
  Then I am on "seleniumhq" Page


@Example2
Scenario: Go to selenium page and verify it is open in the browser
  When I go to "http://www.google.com"
  And I type "Seleniumhq" in the searchbox
  And I press "ENTER" in the searchbox
  And I click on "Selenium - Web Browser Automation" by link text
  Then I am on "seleniumhq" Page
