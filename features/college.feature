Feature: Create a student
  In order to create a student,
  As a student
  I want create a student


  Scenario: create a student
    Given the student does not exist
     When I create a student
     Then the student is created

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
     When attacked by Chuck Norris
     Then the ninja should run for his life