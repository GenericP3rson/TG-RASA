from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import pyTigerGraph as tg

class ActionAge(Action):

    def name(self) -> Text:
        self.conn = tg.TigerGraphConnection(host="https://test.i.tgcloud.io", graphname="MyGraph",
                                            username="tigergraph", password="tigergraph", apiToken="vqumfomk8e7rmq9og5ihe51hqd1131r9")
        return "action_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = self.conn.runInstalledQuery("ageDistribution")
        # print(text)
        dispatcher.utter_message(text=str(text[0]["@@ageMap"]["4"]))
        return []


class ActionInfected(Action):

    def name(self) -> Text:
        self.conn = tg.TigerGraphConnection(host="https://test.i.tgcloud.io", graphname="MyGraph",
                                            username="tigergraph", password="tigergraph", apiToken="vqumfomk8e7rmq9og5ihe51hqd1131r9")
        return "action_infected"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = self.conn.runInstalledQuery(
            "listPatients_Infected_By", {"p": 6100000110}) # Sends question to graph; text is graph's response
        print(text) # Prints the graph's answer
        if (text[0]["Infected_Patients"] == []):
            dispatcher.utter_message(text="This patient infected no one!")
        else: 
            dispatcher.utter_message(text=text[0]["Infected_Patients"])
        return []
