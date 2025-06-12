class ArrayList:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            raise ValueError(f"Value {value} not found in ArrayList.")

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range.")

    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError("Index out of range.")

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

# Example usage
if __name__ == "__main__":
    arr = ArrayList()
    arr.add(1)
    arr.add(2)
    arr.add(3)
    print("ArrayList:", arr)
    arr.remove(2)
    print("After removing 2:", arr)
    print("Element at index 1:", arr.get(1))
    arr.set(0, 10)
    print("After setting index 0 to 10:", arr)
    print("Size:", arr.size())
