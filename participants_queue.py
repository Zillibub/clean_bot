from typing import List
from datetime import date


class ParticipantsQueue:
    class __ParticipantsQueue:
        def __init__(self, participants_list, start_index=0):
            self.participants_list = participants_list
            self.current_index = start_index
            self.current_day = date.today().day

        def get(self):
            if self.current_day != date.today().day:
                self._update_index()
            if self.current_index >= len(self.participants_list):
                self.current_index = 0
            return self.participants_list[self.current_index]

        def _update_index(self):
            self.current_index += 1
            self.current_day = date.today().day

    instance = None

    def __init__(self, participants_list=List[str], start_index=0):
        if not self.instance:
            ParticipantsQueue.instance = self.__ParticipantsQueue(participants_list, start_index)

    def __getattr__(self, name):
        return getattr(self.instance, name)
