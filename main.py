import random
print("数あてゲームよ！by二乃")
print("1~100まで選びなさいよ！by二乃")

answer = random.randrange(start=1, stop=100)
guess = int(input("当てて見なさいよby二乃:"))
tries = 1

while(guess != answer):
  if(guess > answer):
    print("大きいわよ！数字を小さくしなさい！")
  else:
    print("小さいわよ！数字を大きくしなさい！")
  
  tries = tries + 1
  guess = int(input("当てて見なさいよby二乃"))

print("やるじゃない！{}よ!by二乃".format(answer))
print("あんたの試行回数は{}よ!".format(tries))

