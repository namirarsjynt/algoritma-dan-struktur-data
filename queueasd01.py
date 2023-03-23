class AntrianMainan:
    def __init__(self):
        self.antrian = []

    def enqueue(self, mainan):
        self.antrian.append(mainan)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.antrian.pop(0)

    def is_empty(self):
        return len(self.antrian) == 0

# Contoh penggunaan
antrian_mainan = AntrianMainan()
antrian_mainan.enqueue("Boneka Barbie")
antrian_mainan.enqueue("Lego Star Wars")
antrian_mainan.enqueue("Action Figure Spiderman")

print(antrian_mainan.dequeue()) # Output: "Boneka Barbie"
print(antrian_mainan.dequeue()) # Output: "Lego Star Wars"
print(antrian_mainan.dequeue()) # Output: "Action Figure Spiderman"
print(antrian_mainan.dequeue()) # Output: None (antrian sudah kosong)
