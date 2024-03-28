def remove_every_other(my_list):
    final_list = []
    for i in range(0, len(my_list), 2):
        final_list.append(my_list[i])

    return final_list

