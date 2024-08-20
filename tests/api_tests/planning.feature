Feature: Planning diet
  As a user
  I want to plan my diet
  so that I can eat according to nutritional recommendations for a week

    Scenario Outline: Plan a diet for a day
      Given I plan a diet for a day with <meal_count> meals
      When I add a meal "aamiainen", "lounas" and "päivällinen" to the diet
      Then I should see the diet plan for <day_of_week> with <meal_count> meals

      Examples:
        | meal_count | day_of_week |
        | 3          | Today      |
    
    