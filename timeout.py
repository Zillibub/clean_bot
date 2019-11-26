from time import time


class TimeOut:

    def __init__(self, threshold):
        self.current_time = 0
        self.threshold = threshold
        self.is_suspended = False

    def check(self, update, context):
        if time() - self.current_time < self.threshold:
            self.is_suspended = True
            chat_id = update.message.chat_id
            # for 5 minutes
            new_job = context.job_queue.run_once(self.realise_suspend, 2 * 60, context=chat_id)
            context.chat_data['job'] = new_job
            return False
        self.current_time = time()
        return True

    def realise_suspend(self, _):
        self.is_suspended = False
