import requests  
import json
import hashlib
from colorama import init,Fore,Back  

print("欢迎使用!")
print("阅读材料(type=5)链接获取器\n作者:cyhLen\n声明:本程序为msykanswer的扩展，为了弥补msykanswer无法获取阅读材料URL的不足\n版本:sy v1.0_20240218")
init(autoreset=True)


def string_to_md5(string):
	md5_val = hashlib.md5(string.encode('utf8')).hexdigest()
	return md5_val


def cyhLen_login():
	userName=input("请输入\n账号:")
	pwd=input("密码:")
	sn=input("sn:")
	password=string_to_md5(userName+pwd+"HHOO")
	loginurl='https://padapp.msyk.cn/ws/app/padLogin?userName='+userName+'&auth='+password+'&sn='+sn
	login_get = requests.get(loginurl)
	login_first = login_get.text 
	login_last = json.loads(login_first).get('InfoMap') 
	schoolId=json.loads(login_first).get('schoolId')
	userid= login_last['id']
	print(login_last)
	print("姓名:",login_last['realName'])
	print("学校:",login_last['schoolName'])
	print("年级:",login_last['gredeName'])
	print("班级:",login_last['groupName'])
	print("学号:",login_last['studentNumber'])
	print("头像链接:",login_last['avatarUrl'])
	print("学校ID:",schoolId)
	print("用户ID:",userid)
	return userid,schoolId


def get_id(id_1,id_2):
	print("id_1",id_1)
	print("id_2",id_2)
	homeworkid=input(Fore.RED+"请输入作业ID:")
	url = "https://padapp.msyk.cn/ws/common/homework/homeworkStatus?homeworkId="+homeworkid+"&modifyNum=0&userId="+id_1+"&unitId="+id_2
	response = requests.get(url)  
	# 从响应中获取内容，并将其转换为JSON（如果响应是JSON格式的话）  
	content = response.text
	json_content = response.json() 
	#print("JSON内容已解析并存储在json_content变量中。")  
	#print("原始内容已存储在content变量中。")  
	#print(json_content)
	resourceList = json.loads(content).get('resourceList')  
	#print(resourceList)


  
	# 使用循环和动态变量名来分别赋值给100个变量  
	for i, d in enumerate(resourceList):  
	# 使用f-string来创建动态变量名  
		variable_name = f'url_{i}'  
	# 执行赋值操作  
		exec(f'{variable_name} = d')  
  
	# 现在你可以通过变量名来访问这些字典，例如：  

	#print(url_0['resourceUrl'])  # 输出：{'key1': 'value1'}  
	#print(url_1)  # 输出：{'key2': 'value2'}  


	w=resourceList[0]
	#print(w)
	q=w['resourceUrl']
	resTitle=w['resTitle']
	doHomework=w['doHomework']
	readTime=w['readTime']
	#print(resTitle)
	#print(q)
	# 现在你可以使用content或json_content变量了
	for w in q:
		if str(q).lower().startswith('http'):
			file_url=q
		elif str(q).lower().startswith('//'):
			file_url="https://msyk.wpstatic.cn"+q
		elif str(q).lower().startswith('/'):
			file_url="https://msyk.wpstatic.cn"+q
		else:
			file_url="https://msyk.wpstatic.cn/"+q
	#print(file_url)
		
	first_type1='htm'
	first_type2='html'
	type6='doc'
	type7='docx'
	if type7 in resTitle:
		if first_type2 in file_url:
			new_str = file_url.replace("html", "docx")
		else:
			new_str = file_url.replace("htm", "docx")
		file_type=type7
	elif type6 in resTitle:
		if first_type2 in file_url:
			new_str = file_url.replace("html", "doc")
		else:
			new_str = file_url.replace("htm", "doc")
		file_type=type6
	elif 'pdf' in resTitle:
		file_type='pdf'
		new_str=file_url
	else:
		print("链接并非文档类型")
		new_str=file_url
		file_type="other"
		
	if doHomework==1:
		do_return='已开始'
	else:
		do_return='未开始'
	print("作业名称:",resTitle)
	print("状态:",do_return)
	print("用时:",readTime,"s")
	print("文件个数:",len(resourceList))
	print("文件类型:",file_type)
	#print(new_str)"


	# 使用循环和动态变量名来分别赋值给100个变量  
	for i, d in enumerate(resourceList):  
		# 使用f-string来创建动态变量名  
		variable_name = f'url_{i}'  
		# 执行赋值操作  
		exec(f'{variable_name} = d')  
  
	# 现在你可以通过变量名来访问这些字典，例如：  

	#print(url_0['resourceUrl'])  # 输出：{'key1': 'value1'}  
	#print(url_1)  # 输出：{'key2': 'value2'}  


	resource_num=0
	num_all=i+1

	for resource_num in range(len(resourceList)):
	
		if str(resourceList[i]['resourceUrl']).lower().startswith('http'):
			file_url=resourceList[i]['resourceUrl']
		elif str(resourceList[i]['resourceUrl']).lower().startswith('//'):
			file_url="https://msyk.wpstatic.cn"+resourceList[i]['resourceUrl']
		elif str(resourceList[i]['resourceUrl']).lower().startswith('/'):
			file_url="https://msyk.wpstatic.cn"+resourceList[i]['resourceUrl']
		else:
			file_url="https://msyk.wpstatic.cn/"+resourceList[i]['resourceUrl']
		print("第",i+1,"个链接(共",num_all,"个)\n",file_url)
		#print(f"url_{i}: {resourceList[i]['resourceUrl']}")
		i-=1


'''
r=requests.get(new_str)
print(r)
with open('r.docx','rb') as f:
	f.write(r.content)
	f.close
'''
'''
myfile=requests.get(new_str,allow_redirects=True)
open('c:123/456/789/test.docx','wb').write(myfile.content)
'''
'''
if q!=None or len(q)!=0:
    down = input(Fore.BLUE+"是否要下载文件 y/N:")
    down=="Y" or down=="y":
               with open(file_url, "wb") as f, q:
                    f.write(res.content)
'''


def menu():
	data=cyhLen_login()
	#print("123",data)
	userid=data[0]
	schoolld=data[1]
	print(userid,schoolld)
	
	get_id(userid,schoolld)	
	
menu()