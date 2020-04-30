


def produce_summary(files):

    day_count = 0

    for file in files:
        day_count +=1
        print("Day ", day_count)
        the_file = open(file)
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]

            print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))
        the_file.close()

produce_summary(["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]
)