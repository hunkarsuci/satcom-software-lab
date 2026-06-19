# Day 3 - Doppler Shift Estimator
# Satellite Communication Systems Software Lab

SPEED_OF_LIGHT_M_PER_S = 299_792_458

def calculate_doppler_shift(radial_velocity_m_per_s, carrier_frequency_hz):
    doppler_shift_hz = -(radial_velocity_m_per_s / SPEED_OF_LIGHT_M_PER_S) * carrier_frequency_hz
    return doppler_shift_hz

carrier_frequencies_hz = {
    "S-band": 2.2e9,
    "X-band": 8.4e9,
}

radial_velocity_m_per_s = -7_500  # satellite approaching ground station

print("Doppler Shift Comparison")
print("------------------------")

for band_name, carrier_frequency_hz in carrier_frequencies_hz.items():
    doppler_shift_hz = calculate_doppler_shift(
        radial_velocity_m_per_s,
        carrier_frequency_hz
    )

    print(
        f"{band_name}: "
        f"frequency = {carrier_frequency_hz / 1e9:.2f} GHz | "
        f"Doppler shift = {doppler_shift_hz / 1000:.2f} kHz"
    )

