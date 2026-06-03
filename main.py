class SparseArray:
    def __init__(self, initial_list):
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

    # Werte abrufen mit sa[index]
    def __getitem__(self, index):
        # Wenn der Index außerhalb der erlaubten Länge liegt -> Fehler!
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        # Hole den Wert aus dem Dict. Wenn er nicht existiert, gib 0 zurück
        return self._data.get(index, 0)
