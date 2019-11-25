from typing import List
from datetime import date


class ParticipantsQueue:
    class __ParticipantsQueue:
        def __init__(self, participants_list):
            self.participants_list = participants_list
            self.current_index = 0
            self.current_day = date.today().day

        def get(self):
            if self.current_day != date.today().day:
                self._update_index()
            return self.participants_list[self.current_index]

        def _update_index(self):
            self.current_index += 1
            if self.current_index >= len(self.participants_list):
                self.current_index = 0

    instance = None

    def __init__(self, participants_list=List[str]):
        if not self.instance:
            ParticipantsQueue.instance = self.__ParticipantsQueue(participants_list)

    def __getattr__(self, name):
        return getattr(self.instance, name)
