Feature: registration of user

  Scenario: register user basic flow
    Given registration page
    When fill correctly all required fields
    Then user is successfully registrated

  @negative
  Scenario: register user - not filling any field
    Given starting registration page
    When just click next button without filling any field
    Then user can't proceed to step 2
    And info/error message are written below required fields

  @wip
  Scenario: register user - invalid passowrd
    Given starting with registration page
    When fill password field with '<invalid password>'
     | invalid password |
     | Sh0rt     |
     | 1234567890ToLong   |
     | OnlyLetters! |

    Then verify that user got info/error message about invalid password