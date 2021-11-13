password = 'a123456'
i = 3 # 不知道要假設 i
while True:
	pwd = input('請輸入密碼: ') # 不能重複用 password
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i-1
		i = int(i)
		if i == 0:
			print('沒有機會了！')
			break
		print('密碼錯誤！還有', i , '次機會！')
		