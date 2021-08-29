import datetime
import pytz

available_zones = {'1': "America/Chicago",
                   '2': "America/Detroit",
                   '3': "America/Boise",
                   '4': "Asia/Tokyo",
                   '5': "Europe/Rome",
                   '6': "Pacific/Guam",
                   '7': "Europe/Moscow",
                   '8': "Pacific/Auckland",
                   '9': "Asia/Seoul"}

print("Please choose a timezone (or 0 to quit)")
for place in available_zones:
    print("{}. {}".format(place, available_zones[place]))

choice = '10'
while choice != '0':
    choice = input()
    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        localtime = datetime.datetime.now(tz=tz_to_display)
        utctime = datetime.datetime.utcnow()
        print("The time in {} is {} {}".format(available_zones[choice], localtime, localtime.tzname()))
        print("UTC time is {}".format(utctime))
    else:
        print("Please choose a valid timezone from the choices below:")
        for place in available_zones:
            print("{}. {}".format(place, available_zones[place]))

# I thought this was a really cool way to do the challenge that another user did:

# import datetime
# import pytz
# import random
#
# tz_dict = {'0': 'Quit'}
# random_tz = []
# for tz in range(10):
#     y = random.choice(pytz.all_timezones)
#     random_tz.append(y)
# for index, x in enumerate(random_tz):
#     tz_dict[str(index + 1)] = x
# for key, value in (tz_dict.items()):
#     print(key, value, sep=": ")
# print()
# chosen_tz = input("Select the number of the timezone you want to view: ")
# print()
# while chosen_tz != '0':
#     while chosen_tz not in tz_dict.keys():
#         for key, value in tz_dict.items():
#             print(key, value, sep=": ")
#         print()
#         chosen_tz = input("Invalid choice, can only choose a number from the menu: ")
#         print()
#     else:
#         while chosen_tz != '0':
#             chosen_key = tz_dict[chosen_tz]
#             print(f"You chose: {chosen_key}")
#             print()
#             zone_to_show = pytz.timezone(tz_dict[chosen_tz])
#             disp_selected_tz = datetime.datetime.now(tz=zone_to_show)
#             print(f"Time in {chosen_key} is {disp_selected_tz}")
#             print(f"Local time is {datetime.datetime.now()}")
#             print(f"UTC time now is {datetime.datetime.utcnow()}")
#             break
#         break
