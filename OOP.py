class Person:
    def __init__(self, name):
        self.name = name

# Không cần phải khai báo biến trước như trong C++ hoặc Java
# Hoặc có thể
class Person:
    name: str
    def __init__(self, name: str):
        self.name = name

# Nếu muốn khai báo biến private thì thêm dấu gạch dưới
class Person:
    __name: str  # Biến private

    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

#Polymorphism
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

print(Animal().speak())  # Output: Some sound
print(Dog().speak())     # Output: Woof!

#Inheritance
class Animal:
    def speak(self):
        return "Some sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Abstract Class
from abc import ABC, abstractmethod 
# abc là viết tắt của Abstract Base Class, là một module trong Python cung cấp các công cụ để định nghĩa các lớp trừu tượng.
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Interface
class AnimalInterface:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(AnimalInterface):
    def speak(self):
        return "Woof!"


#Magic methods
# __init_ là phương thức khởi tạo của lớp, tương tự như constructor trong C++ hoặc Java
# __str__ là phương thức để định nghĩa cách hiển thị đối tượng khi in ra
# __repr__ là phương thức để định nghĩa cách hiển thị đối tượng khi gọi hàm repr()
# __len__ là phương thức để định nghĩa cách tính độ dài của đối tượng
# __eq__ là phương thức để định nghĩa cách so sánh hai đối tượng
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person({self.name})"

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name
        return False

Person1 = Person("Alice")
Person2 = Person("Bob")
print(Person1)          # Output: Person: Alice
print(repr(Person1))    # Output: Person(Alice)
print(len(Person1))      # Output: 5
print(Person1 == Person2)  # Output: False
# __add__ là phương thức để định nghĩa cách cộng hai đối tượng
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)

#static methods
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Static methods khác với class methods ở chỗ static methods không nhận tham số cls, và chúng không thể truy cập vào các thuộc tính hoặc phương thức của lớp.
# Ví dụ minh họa:
print(MathUtils.add(5, 3))       # Output: 8
print(MathUtils.multiply(5, 3))  # Output: 15

#instance variables and class variables
class Student:
    # Class variable
    school_name = "HCMUT"

    def __init__(self, name):
        # Instance variable
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")
print(s1.name)          # Output: Alice
print(s2.name)          # Output: Bob
print(Student.school_name)  # Output: HCMUT

# Class variables are shared among all instances of the class
print(s1.school_name)  # Output: HCMUT
print(s2.school_name)  # Output: HCMUT
# You can also change the class variable
Student.school_name = "New School"
print(s1.school_name)  # Output: New School
print(s2.school_name)  # Output: New School
# You can also access class variables using the class name
print(Student.school_name)  # Output: New School
