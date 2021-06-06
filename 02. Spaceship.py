from math import floor
ss_width = float(input())
ss_length = float(input())
ss_height = float(input())
average_astro_height = float(input())
cabin_volume = 2.00 * 2.00 * (average_astro_height + 0.40)
ss_volume = ss_height * ss_length * ss_width
astro_count = int(floor(ss_volume / cabin_volume))
if 1.00 <= ss_width <= 10.00 and 1.00 <= ss_length <= 10.00 and 1.00 <= ss_height <= 20.00 and 1.50 <= average_astro_height <= 1.90:
    if 3 <= astro_count <= 10:
        print(f"The spacecraft holds {astro_count} astronauts.")
    elif astro_count < 3:
        print("The spacecraft is too small.")
    elif astro_count > 10:
        print("The spacecraft is too big.")
