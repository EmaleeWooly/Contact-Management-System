class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        return sum(ord(char) for char in key) % self.size

    def insert(self, key: str, number: str):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        node = self.data[index]

        if node is None:
            self.data[index] = Node(key, new_contact)
        else:
            current = node
            while current:
                if current.key == key:
                    current.value.number = number  # Update existing contact
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, new_contact)

    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.data[i]
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Test your hash table implementation here.
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    table.insert("Angeleena", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    contact = table.search("Angeleena")
    print("\nSearch result:", contact)

    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print(table.search("Chris"))  

"""The hash function is beneficial and quick when you need to
find something. Instead of scrolling through and trying to 
find that one piece of information, you can use the hash function
and see exactly where the data should be. Not only is it helpful
when you need to find something, it's helpful when you need to 
input something as well. You don't have to scroll through to find
where a piece of information belongs, you can use the hash. For 
this particular assignment, collisions were taken care of using 
separate chaining. For example, if two contacts hash to the same 
index, then they're stored as a list within that index. If a name 
already exists within that chain, then I go and update the number. 
If it doesn't exist within the chain, then I go in and add a new 
node to the end of the list instead. This keeps things clean and 
readable with so many contacts to keep track of. When you need fast
access, a hash is the way to go. If you have a long list like a 
contacts list, then a tree could take longer and lose you time. 
Hash is ideal for quick access."""