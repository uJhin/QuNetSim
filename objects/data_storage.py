import time
import csv

EVENTS = ["epr_created", "epr_received"]

class DataStorage(object):
    '''
    Stores statistics of a host.
    '''

    def __init__(self):
        self._events = []
        self._amount_epr_created = 0
        self._amount_epr_received = 0

    @property
    def amount_epr_created(self):
        return self._amount_epr_created

    @property
    def amount_epr_received(self):
        return self._amount_epr_received

    def dump_as_csv(self, path):
        """
        Writes the data storage into a CSV file.
        """
        with open(path, 'w') as f:
            f.write("Amount EPR created: %d\n" % self._amount_epr_created)
            f.write("Amount EPR received: %d\n" % self._amount_epr_received)
            fnames = ['time', 'event']
            writer = csv.DictWriter(f, fieldnames=fnames)
            writer.writeheader()
            for entry in self._events:
                writer.writerow({'time':str(entry[0]), 'event': str(entry[1])})

    def log_epr_created(self):
        self._amount_epr_created += 1
        self.log_event("epr_created")

    def log_epr_received(self):
        self._amount_epr_received += 1
        self.log_event("epr_received")

    def log_event(self, event):
        if event not in EVENTS:
            raise ValueError("This event does not exist!")
        t = time.time()
        self._events.append([t, event])

    def log_custom_event(self, event):
        t = time.time()
        self._events.append([t, "custom: %s" % event])
