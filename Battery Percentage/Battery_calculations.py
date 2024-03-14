# test code for battery percentage calculations

def voltage_to_percentage(voltage, max_voltage, min_voltage):
    """
    Convert voltage to battery percentage.

    Args:
    - voltage: The current voltage reading of the battery.
    - max_voltage: The maximum voltage when the battery is fully charged.
    - min_voltage: The minimum voltage when the battery is fully discharged.

    Returns:
    - The battery percentage.
    """
    voltage_range = max_voltage - min_voltage
    percentage_per_volt = 100 / voltage_range
    percentage = ((voltage - min_voltage) * percentage_per_volt)
    # Ensure percentage is within 0-100 range
    return max(0, min(100, percentage))


def main():
    max_voltage = 4.2  # Example: Maximum voltage when battery is fully charged
    min_voltage = 3.0  # Example: Minimum voltage when battery is fully discharged

    # Example voltage readings
    voltage_readings = [3.6, 3.8, 4.0, 4.2, 3.2]

    for voltage in voltage_readings:
        percentage = voltage_to_percentage(voltage, max_voltage, min_voltage)
        print(f"Voltage: {voltage}V => Percentage: {percentage}%")

if __name__ == "__main__":
    main()
