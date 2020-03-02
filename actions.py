from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, FollowupAction


# 'dispatcher' for sending msg to output
# 'tracker' for slots


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
        # return ["browser_type", "browser_version", "platform_type"]
        return ["browser_type", "platform_type"]

    # def slot_mappings(self) -> Dict[Text, Any]:
    #     """defines how to extract slot values from possible user responses and maps them to a specific slot"""
    #     return {"browser_type": self.from_entity(entity="browser_type",
    #                                              intent=["browser_support"]),
    #             "browser_version": self.from_entity(entity="browser_version",
    #                                                 intent=["browser_support"]),
    #             "platform_type": self.from_entity(entity="platform_type",
    #                                               intent=["browser_support"])
    #             }

    """Code for taking an action when all the slots are filled"""

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("We are glad to say that we do support your requirement.")
        return []
