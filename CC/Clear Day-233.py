rainy,cloudy = map(int,input().split())
if(rainy+cloudy <= 7):
  print(f"{7-(rainy+cloudy)}")
else:
  print("This is not a valid input")


