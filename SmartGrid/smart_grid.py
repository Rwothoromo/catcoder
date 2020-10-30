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

m_index = n + 3
m = int(data[m_index])
output_file.write('{}\n'.format(m))


def get_cheapest(start_interval, end_interval, used_cheapest_values):
    cheapest, cheapest_index = int(data[start_interval + 1]), start_interval
    for i in range(start_interval + 1, end_interval + 2):
        val = int(data[i])
        if val < cheapest and val not in used_cheapest_values:
            cheapest = val
            cheapest_index = i - 3
    return ((cheapest, cheapest_index))

used_minute_indices, used_cheapest_values = [], []
for i in range(m_index + 1, m_index + m + 1):
    entry = data[i].split(' ')
    task_id, power, start_interval, end_interval = int(
        entry[0]), int(entry[1]), int(entry[2]), int(entry[3])

    to_use = []
    result_tuple = get_cheapest(start_interval, end_interval, used_cheapest_values)
    cheapest, cheapest_index = result_tuple[0], result_tuple[1]
    used_minute_indices.append(cheapest_index)
    used_cheapest_values.append(cheapest)
    print(used_minute_indices, used_cheapest_values)

    power_used, extra_power = power, 0
    if power > max_power:
        power_used = max_power
        extra_power = power - power_used
    else:
        power_used = power
    to_use.append((cheapest_index, power_used))

    if extra_power > 0:
        result_tuple = get_cheapest(start_interval, end_interval, used_cheapest_values)
        cheapest, cheapest_index = result_tuple[0], result_tuple[1]
        used_minute_indices.append(cheapest_index)
        used_cheapest_values.append(cheapest)

        power = extra_power
        if power > max_power:
            power_used = max_power
            extra_power = power - power_used
        else:
            power_used = power
        to_use.append((cheapest_index, power_used))

    print(used_minute_indices, used_cheapest_values)
    tuple_str_list = []
    for x in to_use:
        tuple_str_list.append(str(x[0]) + " " + str(x[1]))
    tuple_list_str = ' '.join(tuple_str_list)
    output_file.write('{} {}\n'.format(task_id, tuple_list_str))
    # taskId minuteId power minuteId2 power2 ...


output_file.close()
input_file.close()
