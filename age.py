driving = input('請穩你有沒有開過車?')
if driving != '有' or driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗')
    else:
        print('你年齡不符 不應開車!')
elif driving == '沒有':
    if age >= 18:
        print('你已符合考駕照年齡')
    else:
        print('你尚未到考照年齡')
