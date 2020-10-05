# put your code here.

#fish = ["shark", "ray", "halibut", "
"""fish = {
    "anglerfish": "deep ocean", "candiru": "amazon river",
    "trout": "shallow river", "bass": "lake", "shark": "Atlantic Ocean"
    } """

"""for key, value in fish():
    print("key = {}, value = {}".format(key, value))
"""

"""for key, value in my_dict.items():
    print("key = {}, value = {}".format(key, value))"""

#for fish in fish.keys(),fish.values(): 
    #print('hello')
    #print(fish)

#for key, value in fish.items():
    #print("key= {}, value = {}".format(key,value))

'''for fish in fish.keys(),fish.values():
    #print(fish)
    print("key = {}, value = {}".format(fish, fish.values()))'''

def word_count(filename):

    log_file = open(filename)
    count = {}

    
    for line in log_file:
        line = line.rstrip()
        words = line.split()

        for word in words:
            count[word] = count.get(word,0) + 1
            #print(count[word])

    for count, word in count.items():       
        print("{} {}".format(word, count))

    #f = open("test.txt")
    #print(f)

#for key, value in test.

    #for t in text:
        #print(text)

