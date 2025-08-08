def sum_list(numbers):
    """Tính tổng các số trong một list.

    Args:
        numbers (list): Một list các số.

    Returns:
        int: Tổng của các số trong list.

    Raises:
        TypeError: Nếu đầu vào không phải là một list.
        TypeError: Nếu một phần tử trong list không phải là một số.
    """
    # Kiểm tra xem đầu vào có phải là một list không
    if not isinstance(numbers, list):
        raise TypeError("Đầu vào phải là một list.")

    # Khởi tạo tổng bằng 0
    total = 0

    # Lặp qua các số trong list
    for number in numbers:
        # Kiểm tra xem phần tử có phải là một số không
        if not isinstance(number, (int, float)):
            raise TypeError("Tất cả các phần tử trong list phải là số.")
        # Cộng số vào tổng
        total += number

    # Trả về tổng
    return total


# test
if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4, 5]))
    