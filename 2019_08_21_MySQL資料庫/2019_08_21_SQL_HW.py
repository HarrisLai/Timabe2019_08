import os
import pymysql

os.system("cls")
# print("(0) 離開程式")
# print("(1) 顯示會員列表")
# print("(2) 新增會員資料")
# print("(3) 更新會員資料")
# print("(4) 刪除會員資料")
# print("(5) 新增會員電話")
# print("(6) 刪除會員電話")


conn=pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	db="2019-08-21",
	charset="utf8"
)
cmd=conn.cursor()

while True:
	print("(0) 離開程式")
	print("(1) 顯示會員列表")
	print("(2) 新增會員資料")
	print("(3) 更新會員資料")
	print("(4) 刪除會員資料")
	print("(5) 新增會員電話")
	print("(6) 刪除會員電話")
	x=input("指令:")

	if x=="0":
		conn.close()
		exit()

	elif x=="1":
		os.system("cls")
		cmd.execute("SELECT A.`id`, A.`name`, A.`birthday`, A.`address`,B.`tel` FROM `member` AS `A` LEFT JOIN `tel` AS `B` ON `A`.`id`=`B`.`member_id`")
		x=cmd.fetchall()
		for i in x:
			print(i)	

	elif x=="3":
		name=input("請輸入姓名 ")
		birthday=input("請輸入生日: ")
		address=input("請輸入地址: ")
		cmd.execute("INSERT INTO `member`(`name`,`birthday`,`address`) VALUES(%s,%s,%s)",
			(name,birthday,address)
		)
		conn.commit()

	elif x=="4":
		os.system("cls")
		cmd.execute("SELECT * FROM `member`")
		x=cmd.fetchall()
		for i in x:
			print(i)

		number=input("請選擇刪除的編號: ")
		cmd.execute("DELETE FROM `member` WHERE `id`=(%s)", (number))
		conn.commit()

	elif x=="5":
		os.system("cls")
		cmd.execute("SELECT A.`id`, A.`name`, A.`birthday`, A.`address`,B.`tel` FROM `member` AS `A` LEFT JOIN `tel` AS `B` ON `A`.`id`=`B`.`member_id`")
		x=cmd.fetchall()
		for i in x:
			print(i)

		id=input("請選擇要新增電話的會員編號: ")
		tel=input("請入電話號碼: ")
		cmd.execute("INSERT INTO `tel` (`member_id`, `tel`) VALUES (%s, %s)", (id, tel)
		) 

		conn.commit()
		os.system("cls")

	elif x=="6":
		os.system("cls")
		cmd.execute("SELECT A.`id`, A.`name`, A.`birthday`, A.`address`,B.`tel` FROM `member` AS `A` LEFT JOIN `tel` AS `B` ON `A`.`id`=`B`.`member_id`")
		x=cmd.fetchall()
		for i in x:
			print(i)

		id=input("請選擇要刪除電話的會員編號: ")
		cmd.execute("UPDATE `tel` SET `tel` = '' WHERE `tel`.`member_id` = %s", id) 

		conn.commit()
		os.system("cls")

	else:
		continue

