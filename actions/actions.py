# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from asyncore import dispatcher
import datetime as dt
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker #, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)

        if not current_place:
            msg = f"{dt.datetime.now()}"
            dispatcher.utter_message(text=msg)

        return []

class ActionRemeberWhere(Action):

    def name(self) -> Text:
        return "action_remember_where"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)

        if not current_place:
            msg = "I do not know where you live"
            dispatcher.utter_message(text=msg)

        else:
            msg = "{place} is a great place to live."
            dispatcher.utter_message(text=msg)

        return []

# class ValidateNameForm(FormValidationAction):

#     def name(self) -> Text:
#         return "validate_name_form"

#     def validate_first_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#         ) -> List[Dict[Text, Any]]:
#         """Validate `first_name` value"""
#         # If the name is super short, it might be wrong.
#         if len(slot_value) <= 2:
#             dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled it.")
#             return {"first_name": None}
#         else:
#             return {"first_name": slot_value}

#     def validate_last_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: DomainDict,
#         ) -> List[Dict[Text, Any]]:
#         """Validate `first_name` value"""
#         # If the name is super short, it might be wrong.
#         if len(slot_value) <= 2:
#             dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled it.")
#             return {"last_name": None}
#         else:
#             return {"last_name": slot_value}

# class ActionSayFirstName(Action):

#     def name(self) -> Text:
#         return "action_say_first_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         first_name = tracker.get_slot("first_name")
#         if not first_name:
#             dispatcher.utter_message(text="I don't know your first name.")
#         else:
#             dispatcher.utter_message(text=f"Your first name is {first_name}!")
#         return []

class ActionService(Action):

    def name(self) -> Text:
        return "action_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload": '/docs{"content_type":"blogs"}', "title": "Documentation"},
            {"payload": '/video{"content_type": "video"}', "title": "Documentation"}
        ]
        dispatcher.utter_message(text="How would you like to learn?", buttons=buttons)

        return []
