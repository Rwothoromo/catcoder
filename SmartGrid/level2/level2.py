import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
output = []
network = {}

data = input_file.read().splitlines()
n = int(data[0])
m_index = n + 1
m = int(data[m_index])
output_file.write('{}\n'.format(m))

for i in range(m_index + 1, m_index + m + 1):
    entry = data[i].split(' ')
    task_id, duration = int(entry[0]), int(entry[1])

    # determine cheapest interval
    this_interval = [int(x) for x in data[1: duration + 1]]
    price, start_index = sum(this_interval), 0
    # print(price, start_index, this_interval)

    for j in range(2, n + 2 - duration):
        this_interval = [int(x) for x in data[j: duration + j]]
        this_price = sum(this_interval)
        # print(this_price, j - 1, this_interval)

        if this_price < price:
            price, start_index = this_price, j - 1

    output_file.write('{} {}\n'.format(task_id, start_index))


output_file.close()
input_file.close()
