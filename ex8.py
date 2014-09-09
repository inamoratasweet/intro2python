formatter = "%r %r %r %r"
# this line defines the format of the string to be a list of four parts.
# date_format = "%d/%d/%d"
# time format = "%d:%2d:%d.%d %s"  % (10,4,12,80,"pm")
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
