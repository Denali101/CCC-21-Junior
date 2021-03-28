previous = ""

while True:
    nums = input()
    if nums == "99999":
        break
    choice = int(nums[0]) + int(nums[1])
    direction = ""
    if choice == 0:
        direction = previous
    elif choice % 2 != 0:
        direction = "left"
    elif choice % 2 == 0:
        direction = "right"
    previous = direction
    print(direction + " " + nums[2:])