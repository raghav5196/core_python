# basic file

file = open("test.txt","w")
file.close()

file = open("test.txt","w")
file.write("hello raghav bhai kya haal hai \n ")
file.write("bs badiya bhai aap sunao")
file.close()

file = open("test.txt","r")
text = file.read()
print(text)
file.close()


file = open("sample.txt","w")
file.write("hello sir i am raghav patidar i'm from""\n"
           "petlawad distrc jabhua and i doing my BBA ""\n"
           "from davv university and I also completed ""\n"
           "python advance from RAYS technology  ")
file.close()

file = open("sample.txt","r")
raghav =file.read()
print(raghav)
file.close()





