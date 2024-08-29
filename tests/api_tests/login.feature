# Description: i want to test jwt login
Feature: Login

  Scenario Outline: Login with valid credentials
    Given I have the following user:
      | email | password |
      | test@testi.fi  | test     |
    When I login with "<email>" and "<password>"
    Then I should get a jwt token

    Examples:
      | email | password |
      | test@testi.fi  | test     |