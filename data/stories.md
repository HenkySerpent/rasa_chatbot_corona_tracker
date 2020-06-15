## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## what
* what_can_you_do
  - utter_iamabot
  
## corona send me
* corona_checker
  - action_corona
* thanks
  - utter_welcome
## corona send me
* corona_state
  - action_corona
* thanks
  - utter_welcome

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
