Feature: Search foods
  As a user
  I want to search for foods
  So that I can find foods that I want to eat

  Scenario Outline: Search for a food
    Given I search for a <search_term>
    When search should succeed
    Then content should not be empty

    Examples:
      | search_term |
      | chorizo     |

  Scenario Outline: Nutrition information for a food
    Given I search for a chorizo
    When I select the food Chorizo, paistettu ilman rasvaa
    Then I should see the food details "<food_name>" "<energy_kcal>" "<carbs>" "<sugar>" "<fat>" "<fat(saturated)>" "<protein>"

    Examples:
      | search_term | food_name                       | energy_kcal       | carbs            | sugar             | fat              | fat(saturated)   | protein          |
      | chorizo     | Chorizo, paistettu ilman rasvaa | 296.0040436989488 | 1.43773907917881 | 0.951666095862538 | 22.9035243686814 | 8.79153664332839 | 21.3451531742459 |
