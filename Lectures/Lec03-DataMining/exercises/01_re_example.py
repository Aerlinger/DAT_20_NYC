"""
This is an intro to regular expressions

I use https://regex101.com/#python to check my work!
"""


import re

# Define a function to summarize the results of our search:
def summarize_regex(text, re_pattern, search_result):
  print "\nINPUT TEXT: ", text
  print "REGEX PATTERN: ", str(re_pattern.pattern)
  print "\tre.findall(pattern, text) == ", search_result


# flow:
# create a re pattern object
# search (or match) it against text
# orgnize the captures patterns in groups

# \d matches a number
text = "Hello! My name is Anthony. It is 2015 and it's amazing!"
pattern1 = re.compile("\d")
matching_digits = re.findall(pattern1, text) # == a search object
summarize_regex(text, pattern1, matching_digits)

# use group to get each instance in the regular expression
# \d is just ONE number, so it only finds the "2" in "2014"
search_result = re.search(pattern1, text).group(0)
print "First match", search_result


# adding a + means "at least one" but potentially more
pattern2 = re.compile("\d+")
matching_full_digit = re.findall(pattern2, text)   # == '2014'
summarize_regex(text, pattern2, matching_full_digit)


# use square brackets [] to match one of the items present
alphabet = 'abcdefg'
pattern3 = re.compile('[cfg]')
matching_characters = re.findall(pattern3, alphabet)
summarize_regex(alphabet, pattern3, matching_characters)

mystery_pattern = re.compile("\d+-\d+-\d+")
# take a few minutes, and discuss, what application could this mystery_pattern have
matching_phone_number = re.search(mystery_pattern, "my phone number is 805-403-6404 dude").group(0)
summarize_regex(alphabet, pattern3, matching_phone_number)


# . matches ANYTHING
all_of_the_text = "dmzhvbekuhvbc     dfljghwco87rc6geinsr6t4gi7rgwefiuvbekuhvbdfljghwco87rc6geinsr6t4gi7rgwefiu ywgsfybcstzvgbrtybte"
anything_pattern = re.compile(".+")
matching_anything = re.findall(anything_pattern, all_of_the_text).group(0)
summarize_regex(alphabet, pattern3, matching_anything)

# \w matches any word character, alphanumeric
# if you want to match an actual period, do \.
email_pattern = re.compile("[\w\.]+@\w+\.com")
matching_email = re.findall(email_pattern, "my email address is sinan.u.ozdemir@gmail.com").group(0)
summarize_regex(alphabet, pattern3, matching_email)
