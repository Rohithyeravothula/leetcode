# Complete the pressAForCapsLock function below.
def pressAForCapsLock(message):
    lock = False
    ans = []
    for val in message:
        if val.lower() == "a":
            lock = not lock
        else:
            if lock and val.islower():
                ans.append(val.upper())
            elif lock and val.isupper():
                ans.append(val.lower())
            elif not lock:
                ans.append(val)
            else:
                ans.append(val)
    return "".join(ans)

print(pressAForCapsLock("aG"))