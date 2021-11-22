def solution(numbers, hand):
    result = ""
    left = "*"
    right = "#"
    left_number = [1, 4, 7]
    right_number = [3, 6, 9]
    num_pos = {1:(0,0), 2:(0,1), 3:(0,2),
                4:(1,0), 5:(1,1), 6:(1,2),
                7:(2,0), 8:(2,1), 9:(2,2),
                "*":(3,0), 0:(3,1), "#":(3,2)}

    for x in numbers:
        if x in left_number:
            result += "L"
            left = x
        elif x in right_number:
            result += "R"
            right = x
        else:
            left_pos = num_pos[left]
            right_pos = num_pos[right]
            in_num_pos = num_pos[x]

            l_dif = abs(in_num_pos[0] - left_pos[0]) + abs(in_num_pos[1] - left_pos[1])
            r_dif = abs(in_num_pos[0] - right_pos[0]) + abs(in_num_pos[1] - right_pos[1])

            if l_dif < r_dif:
                result += "L"
                left = x
            elif l_dif > r_dif:
                result += "R"
                right = x
            else:
                if hand == "left":
                    result += "L"
                    left = x
                elif hand == "right":
                    result += "R"
                    right = x

    answer = result
    return answer


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")