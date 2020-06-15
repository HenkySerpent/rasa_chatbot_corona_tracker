# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# from rasa_core.events import SlotSet


class ActionCorona(Action):

    def name(self) -> Text:
        return "action_corona"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp = requests.get(
            "https://covid19-server.chrismichael.now.sh/" +
            "api/v1/IndiaCasesByStates"
        ).json()
        respon = resp["data"]
        response = respon[0]
        print(response)
        entities = tracker.latest_message['entities']
        # print("last message now ", entities)
        state = None
        table = "table"
        type(response)
        for e in entities:
            if e['entity'] == "state":
                state = e['value']
        message = "Please enter correct name."

        if state == "India":
            state = "Total"

        for data in response[table]:
            if data['state'] == state.title():
                print(data)
                message = "Active :" + data["active"] + " Confirmed :" + data["confirmed"] + " Deaths :" + data["deaths"] + " Lastupdate :" + data["lastupdatedtime"] + " " + data["statenotes"]
        print(message)
        dispatcher.utter_message(message)
        return []
