## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

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
  - utter_bot_challenge

## greet
* greet
  - utter_greet

## thank
* thank
  -utter_noworries

## goodbye
* bye
  -utter_bye

## Some question from FAQ
* faq
    - respond_faq

## sales form
* contact_sales
    - sales_form
    - form{"name":"sales_form"}
    - form{"name":null}

## greet+botchallenge+what do i know+developed_by+bye
* greet
    - utter_greet
* bot_challenge
    - utter_bot_challenge
* everything_i_know
    - utter_everything_i_know
* developed_by
    - utter_developed_by
* bye
    - utter_bye

## greet+botchallenge+what do i know+developed_by+browser_support+bye
* greet
    - utter_greet
* bot_challenge
    - utter_bot_challenge
* everything_i_know
    - utter_everything_i_know
* developed_by
    - utter_developed_by
* browser_support
    - utter_browser_support
    - browser_form
    - form{"name":"browser_form"}
    - form{"name":null}
* bye
    - utter_bye
    
## greet+botchallenge+what do i know+developed_by+browser_support+bye
* greet
    - utter_greet
* browser_support{"browser_type":"chrome","browser_version":"20","platform_type":"windows"}
    - utter_browser_support
    - browser_form
    - form{"name":"browser_form"}
    - form{"name":null}
* bot_challenge
    - utter_bot_challenge
* bye
    - utter_bye
    
## v2_ greet+browser_support+bye
* greet
    - utter_greet
* browser_support{"browser_type":"chrome","platform_type":"windows"}
    - utter_browser_support
    - browser_form
    - form{"name":"browser_form"}
    - form{"name":null}
* bot_challenge
    - utter_bot_challenge
* bye
    - utter_bye

## ************client support**********greet+botchallenge+what do i know+developed_by+client_support+bye
* greet
    - utter_greet
* bot_challenge
    - utter_bot_challenge
* everything_i_know
    - utter_everything_i_know
* developed_by
    - utter_developed_by
* client_support
    - utter_client_support
    - client_form
    - form{"name":"client_form"}
    - form{"name":null}
* bye
    - utter_bye
    
## greet+botchallenge+what do i know+developed_by+client_support+bye
* greet
    - utter_greet
* client_support{"platform_type":"windows","client_type":"pc"}
    - utter_client_support
    - client_form
    - form{"name":"client_form"}
    - form{"name":null}
* bot_challenge
    - utter_bot_challenge
* bye
    - utter_bye
    
## v2_ greet+client_support+bye
* greet
    - utter_greet
* client_support{"platform_type":"unix","client_type":"PowerCenter Client 32bit 2"}
    - utter_client_support
    - client_form
    - form{"name":"client_form"}
    - form{"name":null}
* bot_challenge
    - utter_bot_challenge
* bye
    - utter_bye

## stop but continue path
* greet
    - utter_greet
* stop
    - utter_ask_continue
* thank
    - utter_noworries
