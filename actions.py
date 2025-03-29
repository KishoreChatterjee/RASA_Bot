from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreetUser(Action):
    def name(self):
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        user_name = tracker.get_slot("name")  # Fetching a slot value (if needed)
        message = f"Hello {user_name}, how can I assist you today?" if user_name else "Hello! How can I help you?"
        dispatcher.utter_message(text=message)
        return []
