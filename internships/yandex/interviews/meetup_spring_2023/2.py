def seat_passengers(n, passengers):
    # Parse input
    seats = {}
    for i in range(n):
        ai, seat = passengers[i].split()
        seats[seat] = int(ai)

    # Sort passengers by seat number
    passenger_list = sorted(seats.keys())

    # Initialize blocked seats
    blocked_seats = []

    # Initialize time taken
    time_taken = 0

    # Iterate through each passenger
    for i in range(n):
        seat = passenger_list[i]
        ai = seats[seat]

        # Check if seat is available
        if seat not in blocked_seats:
            # Seat passenger immediately
            time_taken += ai
        else:
            # Find first available blocked seat passenger
            blocked_passengers = []
            for blocked_seat in blocked_seats:
                if blocked_seat != seat:
                    blocked_passengers.append(
                        (seats[blocked_seat], blocked_seat))
            blocked_passengers.sort(reverse=True)
            time_to_move = 0
            while blocked_passengers:
                # Check if all blocked passengers can move
                can_move = True
                for _, blocked_seat in blocked_passengers:
                    if blocked_seat in blocked_seats:
                        can_move = False
                        break
                if not can_move:
                    # Wait until all blocked passengers can move
                    max_time_to_move, max_blocked_seat = blocked_passengers[0]
                    blocked_passengers = [(t - max_time_to_move, s)
                                          for t, s in blocked_passengers[1:]]
                    time_to_move += max_time_to_move
                else:
                    # Move all blocked passengers
                    for _, blocked_seat in blocked_passengers:
                        blocked_seats.remove(blocked_seat)
                    blocked_seats.append(seat)
                    time_taken += ai + time_to_move
                    break

    return time_taken


n = int(input())
passengers = []

for i in range(n):
    passengers.append(input())

print(seat_passengers(n, passengers))
