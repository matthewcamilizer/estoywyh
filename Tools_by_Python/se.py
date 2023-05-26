import subprocess, os, datetime, win32api
from NewFile import newfile

ct=datetime.datetime.now()
ff=ct.strftime("%Y-%m-%d")

aa=win32api.GetLogicalDriveStrings()
a=aa.split('\000')[:-1]
enter=input("输入忘记位置的文件: ")
file, fmt = os.path.splitext(enter)
p=r"C:\Users\Administrator\Desktop"
log=newfile(p, f"{ff}找文件 \u2022 '{file}'.txt")

found=[]
for ss in a:
	for root,dirs,files in os.walk(ss):
		for f in files:
			filename, filefmt = os.path.splitext(f)
			if filename ==file:
				here=os.path.join(root,f)
				found.append(here)
				print(f"\n第{len(found)}个(要复制就复制单引号里的内容): '{here}'\n因为是全电脑搜索, 所以不要手动关闭. 搜索完会问“按回车关闭, 如果你觉得卡了也可以按回车, 但可能会闪退")
				with open (log, 'a', encoding='utf-8') as lf:
					if lf.tell()==0:
						lf.write(f"{ff}\n找这个文件: {enter}\n\n打开方式: 先打开'我的电脑' \n再把每行的文件路径复制粘贴到'我的电脑'上面那个长框框中, 然后按回车\n下面列出的是文件路径\n\n")
					here=here.replace("\\\\", "\\")
					lf.write(f"\n\n{here}\n\n")

input(f"一共找到{len(found)}个可能的 {enter} 文件, 按回车退出")

				

