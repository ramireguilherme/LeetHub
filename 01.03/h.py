def bus_get_off_order(n, m):
    # Create lists for window and non-window seat passengers
    window_seats = []
    non_window_seats = []

    # Fill window seats
    for i in range(n):
        if len(window_seats) < m:
            window_seats.append(i + 1)
        if len(window_seats) < m:
            window_seats.append(i + 1 + n)
    
    # Fill non-window seats if there are more than 2n passengers
    if m > 2 * n:
        for i in range(n):
            if len(non_window_seats) < m - 2 * n:
                non_window_seats.append(i + 1)
            if len(non_window_seats) < m - 2 * n:
                non_window_seats.append(i + 1 + n)
    
    # Combine the lists to follow the get-off pattern
    get_off_order = []
    for i in range(n):
        if i < len(non_window_seats):
            get_off_order.append(non_window_seats[i])
        if i < len(window_seats):
            get_off_order.append(window_seats[i])
        if i + n < len(non_window_seats):
            get_off_order.append(non_window_seats[i + n])
        if i + n < len(window_seats):
            get_off_order.append(window_seats[i + n])
    
    return get_off_order[:m]

# Read input
n, m = map(int, input().strip().split())

# Get the order in which passengers get off the bus
order = bus_get_off_order(n, m)

# Print the result
print(" ".join(map(str, order)))
