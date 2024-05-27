#!/usr/bin/env python3

class MyString:
    def __init__(self, initial_value=""):
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        cleaned_value = self.value.replace("!", ".").replace("?", ".")
        sentences = [s.strip() for s in cleaned_value.split('.') if s.strip()]
        return len(sentences)

# this is example usage and test
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  # Output should be 3

# this tests the implementation
import io
import sys

def test_value_string():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    string = MyString()
    string.value = 123
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "The value must be a string.\n"

#finally, this runs the test
if __name__ == "__main__":
    test_value_string()
