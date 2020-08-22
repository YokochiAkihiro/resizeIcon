#1024から他のサイズのアイコンの作成をする。
import cv2
#ファイルサイズ
size = [167,152,180,120,87,80,76,60,58,40,29,20]
for n in range(len(size)):
	if n == 0:
		#ファイル読み込み
		img = cv2.imread("1024.png")
		#リサイズ
		img2=cv2.resize(img,(size[n],size[n]))
		#保存
		cv2.imwrite("Icon%s.png"%size[n],img2)
	else:
		#ファイル読み込み
		img = cv2.imread("Icon%s.png"%size[n-1])
		#リサイズ
		img2=cv2.resize(img,(size[n],size[n]))
		#保存
		cv2.imwrite("Icon%s.png"%size[n],img2)
