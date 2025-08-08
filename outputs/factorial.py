def factorial(n):
    """Tính giai thừa của một số nguyên không âm.

    Args:
        n: Số nguyên không âm.

    Returns:
        Giai thừa của n. Trả về 1 nếu n = 0.

    Raises:
        ValueError: Nếu n là số âm.
    """
    if n < 0:
        raise ValueError("Không thể tính giai thừa của số âm")
    elif n == 0:
        return 1
    else:
        # Sử dụng đệ quy để tính giai thừa
        return n * factorial(n-1)