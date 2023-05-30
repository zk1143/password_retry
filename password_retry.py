password = 'a123456'
x = 3
while True:
	pw = input('請輸入你的密碼:')
	if pw == password:
		print('登入成功!!')
		break
	else:
		x = x - 1
		print('密碼不正確還有',(x), '次機會')
		if x == 0:
			print('想好在來')
			break

	