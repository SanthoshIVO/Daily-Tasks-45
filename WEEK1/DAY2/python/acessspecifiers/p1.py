class Person:
    def __init__(self, name, age):
        self.name = name       # Public
        self._age = age        # Protected
        self.__email = None    # Private

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Email: {self.__email or 'Not provided'}")

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be positive.")