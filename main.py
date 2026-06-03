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

    # werte setzen mit sa[index] = value
    def __setitem__(self, index, value):
        # Auch hier: Index-Kontrolle!
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        if value == 0:
            # Wenn der Benutzer eine 0 setzt, löschen wir den Eintrag aus dem Dict (Speicher sparen!)
            if index in self._data:
                del self._data[index]
        else:
            # Nur echte Werte ungleich Null belegen Speicherplatz
            self._data[index] = value

    # Elemente löschen mit del sa[index]
    def __delitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        new_data = {}
        # Wir wandern durch unser aktuelles Dictionary und verschieben die Indizes
        for k, v in self._data.items():
            if k < index:
                # Element VOR dem gelöschten Index bleiben gleich
                new_data[k] = v
            elif k > index:
                # Elemente NACH dem gelöschten Index rutschen einen Platz nach links (-1
                new_data[k -1] = v

        self._data = new_data
        # Da ein Element komplett weg ist, schrumpft unsere virtuelle Länge um 1
        self._length -= 1
