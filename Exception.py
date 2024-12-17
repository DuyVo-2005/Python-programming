try:
    numb = int(input())
    print(1/numb)
except (ZeroDivisionError):
    print("Zero division error")
#asign many error: (ValueError, ZeroDivisionError)
except:#ValueError,...
    print("An exception occurred!")
