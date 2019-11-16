formatter = "{} {} {} {}"

# put integers in the formatter
print(formatter.format(1,2,3,4))

#put string in the formatter
print(formatter.format("one", "two", "three", "four"))

# print true or false per entrey in formatter
print(formatter.format(True, False, False, True))

# duplicate formatter with formatter
print(formatter.format(formatter, formatter, formatter, formatter))

# put string in the formatter but different presentation with enters. After 4 entry everything gets denied.
print(formatter.format(
    "Try your",
    "Own text",
    "Maybe a poem",
    "Or a song about fear",
    "bal"
))
