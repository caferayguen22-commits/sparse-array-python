class SparseArray:
    def __init__(selfself, initial_list):
        # Wir speichern die virtuelle Gesamtlänge
        self._length = len(initial_list)
        # Hier landen nur die Werte, die NICHT Null sind
        self._data = {}

        # Wir gehen durch die Liste und picken uns die echten Werte raus
        for index, value in enumerate(initial_list):
            if value != 0:
                self._data[index] = value

    def __len__(self):
        # Gibt die virtuelle Länge (inklusive der Nullen) zurück
        return self._length