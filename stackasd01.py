class ToplesCokelat:
    def __init__(self):
        self.toples = []

    def push(self, cokelat):
        self.toples.append(cokelat)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.toples.pop()

    def is_empty(self):
        return len(self.toples) == 0

# Contoh penggunaan
toples_cokelat = ToplesCokelat()
toples_cokelat.push("Cokelat Klasik")
toples_cokelat.push("Cokelat Kacang")
toples_cokelat.push("Cokelat Mint")

print(toples_cokelat.pop()) # Output: "Cokelat Mint"
print(toples_cokelat.pop()) # Output: "Cokelat Kacang"
print(toples_cokelat.pop()) # Output: "Cokelat Klasik"
print(toples_cokelat.pop()) # Output: None (toples sudah kosong)
