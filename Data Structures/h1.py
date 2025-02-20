rows , people = map(int, input().split())
people_on_left_window = 0
people_on_right_window = 0

leftwindow_window = []
rightwindow_window = []
leftwindow_aisle = []
rightwindow_aisle = []
person = 1
# populate windows
for i in range(2*rows):
    if person <= people:
        if i % 2 == 0:
            leftwindow_window.append(person)
        else:
            rightwindow_window.append(person)
        person += 1

# populate aisles
for i in range(2*rows):
    if person <= people:
        if i % 2 == 0:
            leftwindow_aisle.append(person)
        else:
            rightwindow_aisle.append(person)
        person += 1

order = []

# get off people
while person > 1:
    if leftwindow_aisle != []:
        order.append(leftwindow_aisle.pop(0))
        person -= 1
    if leftwindow_window != []:
        order.append(leftwindow_window.pop(0))
        person -= 1
    if rightwindow_aisle != []:
        order.append(rightwindow_aisle.pop(0))  
        person -= 1
    if rightwindow_window != []:
        order.append(rightwindow_window.pop(0))
        person -= 1

print(" ".join(map(str, order)))