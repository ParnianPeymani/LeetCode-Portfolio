def mynum(num: int) -> int:
    s = list(str(num))
    for i in range(len(s)):
        if s[i] == "6":
            s[i] = "9"
            break
    return int("".join(s))

print(mynum(6966))  # 9966