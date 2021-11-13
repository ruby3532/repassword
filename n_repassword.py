# 若今天不要寫 while true 怎麼辦？
# 改檢查「還剩餘幾次機會」，若還有機會就可以繼續輸入
# 新的程式碼為：
password = 'a123456'
i = 3 
while i > 0:
	pwd = input('請輸入密碼: ') # 不能重複用 password
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i-1
		i = int(i)
		if i == 0:
			print('沒有機會了')
			break
		print('密碼錯誤！還有', i , '次機會！')
