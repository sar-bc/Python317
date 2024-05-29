time_all = [
    '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
    '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
    '18:00', '18:30', '19:00', '19:30', '20:00'
]
# , '19:30'
# На выходе дожны получить #
# time_group = [
# #     ['08:00', '08:30', '09:00', '09:30'],
# #     ['10:00', '10:30', '11:00', '11:30'],
# #     ['12:00', '12:30', '13:00', '13:30'],
# #     ['14:00', '14:30','15:00', '15:30'],
# #     ['16:00', '16:30', '17:00', '17:30'],
# #     ['18:00', '18:30', '19:00']
# # ]
print(f"time_al:{len(time_all) // 4}")


def group(t):
    time_row = []
    time_group = []
    for i in t:
        time_row.append(i)
        if len(time_row) == 4:
            time_group.append(time_row)
            time_row = []
    if time_row:
        time_group.append(time_row)

    return time_group


print(group(time_all))

# time_group = []
# count = 20
# time_group.append([time_all[x] if x < len(time_all) else time_all[x-1] for x in range(count, count + 4)])
# print(time_group)
####################################
# time_group = [
#     ['08:00', '08:30', '09:00', '09:30'],
#     ['10:00', '10:30', '11:00', '11:30'],
#     ['12:00', '12:30', '13:00', '13:30'],
#     ['14:00', '14:30', '15:00', '15:30'],
#     ['16:00', '16:30', '17:00', '17:30'],
#     ['18:00', '18:30', '19:00', '19:30'],
#     ['20:00', False, False, False]
# ]
#
# print(time_group)
def group_time_slots(time_list):
    grouped_times = []
    temp_group = []
    for time_slot in time_list:
        temp_group.append(time_slot)
        if len(temp_group) == 4:
            grouped_times.append(temp_group)
            temp_group = []
    if temp_group:
        grouped_times.append(temp_group)
    return grouped_times


# time_all = [
#     '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
#     '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
#     '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
#     '18:00', '18:30', '19:00'
# ]

time_group = group_time_slots(time_all)
# print(time_group)
