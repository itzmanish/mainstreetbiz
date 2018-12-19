from django.test import TestCase

# Create your tests here.

string = '<p>some</p>'
test = string.strip('<p>/')
print(test)
