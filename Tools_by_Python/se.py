import subprocess, os, datetime, win32api, sys
from NewFile import newfile

sys.dont_write_bytecode=True

ct=datetime.datetime.now()
ff=ct.strftime("%Y-%m-%d")

aa=win32api.GetLogicalDriveStrings()
a=aa.split('\000')[:-1]
enter=input("输入忘记位置的文件: ")
file, fmt = os.path.splitext(enter)
p=input(r"输入保存日志的路径(如果什么都不输入就直接按回车, 默认保存在桌面, 路径输错了也保存在桌面):")
ToSaveRoot=ToSave=ep=FinalFile=''
if not p or not os.path.exists(p):
	if not os.path.exists(p):
		ep=p
		print(f"你输入的这个路径{p}电脑里没有, 日志默认保存在桌面")
	p=r"C:\Users\Administrator\Desktop"

ToSaveRoot=os.path.join(p, "找文件")
if not os.path.exists(ToSaveRoot):
	os.mkdir(ToSaveRoot)

ToSave=os.path.join(ToSaveRoot, ff)
if not os.path.exists(ToSave):
	os.mkdir(ToSave)

log=newfile(ToSave, f"{ff} - 找文件 \u2022 '{file}'.txt")

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
						lf.write(f"{ff}\n你输入的想找文件是这个: {enter}\n\n打开方式: 先打开'我的电脑' \n再把每行的文件路径复制粘贴到'我的电脑'上面那个长框框中, 然后按回车\n下面列出的是文件路径\n\n")
						if not os.path.exists(ep):
							lf.write(f"你的保存路径输的是这个: {ep} 电脑里没有\n所以默认存在桌面: {p}")
					here=here.replace("\\\\", "\\")
					lf.write(f"\n\n第{len(found)}个可能的 {enter} 文件:\n{here}\n\n")

input(f"一共找到{len(found)}个可能的 {enter} 文件, 按回车退出")

				

