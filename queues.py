class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        else:
            return None

    def read(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return None


class PrintManager:
    def __init__(self):
        self.queue = Queue()

    def queue_print_job(self, document):
        self.queue.enqueue(document)

    def run(self):
        while self.queue.read():
            self.print_document(self.queue.dequeue())

    def print_document(self, document):
        # code to run the actual printer goes here
        # for demo purposes print to the terminal
        print(document)


print_manager = PrintManager()
print_manager.queue_print_job("First document")
print_manager.queue_print_job("Second document")
print_manager.queue_print_job("Third document")
print_manager.run()
