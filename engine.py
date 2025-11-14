import json

with open('locations_info.json', 'r', encoding='utf-8') as locs:
    loc_info = json.load(locs)

current_location = "location_start"

print("Нажмите ENTER чтобы начать")
input()

while "ending" not in current_location:

    current_location_info = loc_info[current_location]

    print(current_location_info["lore"])
    input()

    if current_location_info["question"] == "None":
        current_location = current_location_info["next_location"]

    elif current_location_info["question"] == "boss":
        print("тут пока ничего нет(")

    else:
        print(current_location_info["question"])
        print(*current_location_info["answers"], sep="\n")

        answer = input()
        while answer not in ["1", "2"]:
            print("Введите 1 или 2.")
            answer = input()
        
        answer = int(answer)
        if answer == current_location_info["true_answer"]:
            current_location = current_location_info["next_location_true"]
        else:
            current_location = current_location_info["next_location_false"]

print(loc_info[current_location]["lore"])
