import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')
output = []
network = {}

data = input_file.read().splitlines()
max_power = int(data[0])
max_bill = int(data[1])  # long
n = int(data[2])

m_index = n + 1
m = int(data[m_index])
output_file.write('{}\n'.format(m))

for i in range(m_index + 1, m_index + m + 1):
    entry = data[i].split(' ')
    task_id, power, start_interval, end_interval = int(
        entry[0]), int(entry[1]), int(entry[2]), int(entry[3])
    cheapest, cheapest_index = int(data[start_interval + 1]), start_interval
    # print(int(data[start_interval + 1]), cheapest, cheapest_index)
    for i in range(start_interval + 1, end_interval + 2):
        val = int(data[i])
        if val < cheapest:
            cheapest = val
            cheapest_index = i - 1
        # print(val, cheapest, cheapest_index)

    output_file.write('{} {} {}\n'.format(task_id, cheapest_index, power))


output_file.close()
input_file.close()
