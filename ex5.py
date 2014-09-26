name = 'Zed A. Shaw'
age = 35 # not a lie
height = float (raw_input("height in cm\n")) #194
weight = float (raw_input("Weight in Kilos\n"))#85
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# convert KG into pounds
weight_in_pounds = weight * 2.2

print "you entered", weight, "kg, that comes to %.2f pounds" % weight_in_pounds

# convert cm into inches
length_in_inches = height * 0.393700787

print "you entered", height, "cm, that comes to %.2f inches." % length_in_inches

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)    
