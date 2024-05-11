school_class = {}  # create empty dict. Name will be key, score will be tuples.

while True:  # create loop, will BREAK on the 'exit' condition
    name = input("Enter student name (or type exit to stop): ")  # read student name here
    if name == 'exit':
        break

    score = int(input("Enter the student score (0-10): "))  # ask for input of student score here

    if name in school_class:  # if name exists, lengthen tuple with new score
        school_class[name] += (score,)
    else:  # if new, create new entry. It's value is one-element tuple containing the score
        school_class[name] = (score,)

for name in sorted(school_class.keys()):  # Iterate through sorted students names:
    adding = 0  # initialize data needed to evaluate average (sum and counter)
    counter = 0
    for score in school_class[name]:  # iterate through the tuple, taking all scores and updating the sum,
        adding += score               # together with the counter:
        counter += 1

    print(school_class)

    print(name, ":", adding / counter)  # evaluate and print name and average of their scores
