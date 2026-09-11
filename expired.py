items=["milk","bread","eggs","butter"]
expired=["eggs","butter"]
for item in items:
    if item in expired:
        print(item,"is expired.")
    else:
        print(item,"is not expired.")