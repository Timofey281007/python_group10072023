some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]


def check_data(num: int | float) -> bool:
    if not any([type(num) == int, type(num) == float]) or num <= 500:
        return False
    return True


filtered_list = list(filter(check_data, some_data))
# print(filtered_list)
