rectangle_lengths = [5,8,10,3]

length_sorted = sorted(range(len(rectangle_lengths)), key = lambda k:rectangle_lengths[k])

numbering_map = {length_sorted[i]: i+1 for i in range (len(length_sorted))}

for original_index, assigned_number in sorted(numbering_map.items()):
    print(f"Rectangle {original_index + 1} : {assigned_number}")