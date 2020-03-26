from typing import Dict, Text, Any, List, Union

from rasa_sdk.events import SlotSet, AllSlotsReset, EventType
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import scripts.RetrieveFromPAM as pamDetails


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    # name of the action goes here. This should be mentioned in stories and domain.yml
    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict[Text, Any]]]:
        return {
            "use_case": self.from_text(intent="inform"),
            "email": [
                self.from_entity(entity="email"),
                self.from_text(intent="enter_data"),
            ]
        }


class BrowserForm(FormAction):
    """Collects browser information"""

    # name of the action goes here. This should be mentioned in stories and domain.yml
    def name(self):
        """Unique identifier of the form"""
        return "browser_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["browser_type", "platform_type"]

    def slot_mappings(self) -> Dict[Text, List[Any]]:
        """defines how to extract slot values from possible user responses and maps them to a specific slot"""
        return {"browser_type": [self.from_entity(entity="browser_type", intent=["browser_support"]),
                                 self.from_text()
                                 ],
                # "browser_version": self.from_entity(entity="browser_version",
                #                                     intent=["browser_support"]),
                "platform_type": [self.from_entity(entity="platform_type", intent=["browser_support"]),
                                  self.from_text()]
                }

    """Code for taking an action when all the slots are filled"""

    @staticmethod
    def get_browser_support(self, tracker: Tracker):
        print("Inside get_browser_support********************************************")
        print("Browser type slot", tracker.get_slot('browser_type'))
        print("Platform type slot", tracker.get_slot('platform_type'))
        obj = pamDetails.BrowserRetrieve()
        df = pamDetails.edc_browsers
        print("Data frame..........", df)
        col = tracker.get_slot('platform_type')
        index_type = tracker.get_slot('browser_type')
        # version = 'All'
        return obj.get_value_from_df(df, index_type, col)

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        print("Running*******************************")
        obj = pamDetails.BrowserRetrieve()
        if tracker.get_slot('browser_type') is None:
            print("Browser type question?????????????????????????")
            dispatcher.utter_message(template="utter_ask_browser_type", browsers=obj.get_browsers())
        elif tracker.get_slot('platform_type') is None:
            print("Platform type question?????????????????????????")
            dispatcher.utter_message(template="utter_ask_platform_type", platforms=obj.get_platforms())
        else:
            self.submit(dispatcher, tracker, domain)
        return []

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print("Submitting the action.......")
        result = BrowserForm.get_browser_support(self, tracker)
        dispatcher.utter_message(result)
        return [SlotSet("browser_type", None),
                SlotSet("platform_type", None)]


class ClientForm(FormAction):
    """Collects browser information"""

    # name of the action goes here. This should be mentioned in stories and domain.yml
    def name(self):
        """Unique identifier of the form"""
        return "client_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["platform_type", "client_type"]

    def slot_mappings(self) -> Dict[Text, List[Any]]:
        """defines how to extract slot values from possible user responses and maps them to a specific slot"""
        return {"platform_type": [self.from_entity(entity="platform_type", intent=["client_support"]),
                                  self.from_text()
                                  ],
                # "client_version": self.from_entity(entity="client_version",
                #                                     intent=["client_support"]),
                "client_type": [self.from_entity(entity="client_type", intent=["client_support"]),
                                self.from_text()]
                }

    """Code for taking an action when all the slots are filled"""

    @staticmethod
    def get_client_support(self, tracker: Tracker):
        print("Inside get_client_support********************************************")
        print("Platform type slot", tracker.get_slot('platform_type'))
        print("Client type slot", tracker.get_slot('client_type'))
        obj = pamDetails.ClientRetrieve()
        df = pamDetails.edc_clients
        print("Data frame..........\n", df)
        index_type = tracker.get_slot('platform_type')
        col = tracker.get_slot('client_type')
        # version = 'All'
        return obj.get_value_from_df(df, index_type, col)

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        print("Running*******************************")
        obj = pamDetails.ClientRetrieve()
        if tracker.get_slot('platform_type') is None:
            print("Platform type question?")
            dispatcher.utter_message(template="utter_ask_platform_type", platforms=obj.get_platforms())
        elif tracker.get_slot('client_type') is None:
            print("Client type question?")
            dispatcher.utter_message(template="utter_ask_client_type", clients=obj.get_clients())
        else:
            self.submit(dispatcher, tracker, domain)
        return []

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        print("Submitting the action.......")
        result = ClientForm.get_client_support(self, tracker)
        dispatcher.utter_message(result)
        return [SlotSet("platform_type", None),
                SlotSet("client_type", None)]
