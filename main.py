def average_temperature(values):
    return sum(values) / len(values)

temps = [21.3, 22.1, 20.8, 23.0, 21.7]
avg = average_temperature(temps)
print(f"Átlaghőmérséklet: {avg:.2f} °C")