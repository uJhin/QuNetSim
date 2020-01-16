import time
import csv


class DataStorage(object):
    '''
    Stores statistics of a host.
    '''

    def __init__(self):
        self._events = []
        self._amount_epr_created = 0
        self._amount_epr_received = 0

    def dump_as_csv(self, path):
         f = open(path, 'w')
         with f:
             fnames = ['time', 'event']
             writer = csv.DictWriter(f, fieldnames=fnames)
             writer.writeheader()
             for entry in self._events:
                 writer.writerow({'time':entry[0], 'event': entry[1]})


    def add_custom_event(self, event):
        t = time.time()
        self._events.append((t, event))
