previous = "" # For when the first two nums = 0

while True:
    nums = input() # Has to be string because there can be 0 in the beginning
    if nums == "99999":
        break
    choice = int(nums[0]) + int(nums[1]) # Adds the first two nums of the input
    direction = ""
    if choice == 0:
        direction = previous # Because the 00___ only occurs after another number that is not 00___, the direction variable would have already been updated, meaning we can just use that.
    elif choice % 2 != 0: # Odd nums
        direction = "left"
    elif choice % 2 == 0: # Even nums
        direction = "right"
    previous = direction # The previous variable needs to be updated when we loop again, because the "direction" variable is reset everytime we loop. If this line wasn't here, both the previous and direction variables would be empty.
    print(direction + " " + nums[2:])
