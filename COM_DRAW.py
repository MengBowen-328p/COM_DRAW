### Python lib requirement：
### array 
import array
import pyserial
import threading
import numpy as np
import time
import pyqtgraph as pg


i = 0
def Serial():
    while(True):
        n = mSerial.inWaiting()
        if(n):
            if data!=" ":
                dat = int.from_bytes(mSerial.readline(1),byteorder='little')    #转换数据格式
                n=0
                global i;
                if i < historyLength:
                    data[i] = dat
                    i = i+1
                else:
                    data[:-1] = data[1:]
                    data[i-1] = dat

def plotData():
    curve.setData(data)


if __name__ == "__main__":
    app = pg.mkQApp()
    win = pg.GraphicsWindow()
    win.setWindowTitle(u'COM_Drawer')    #窗口标题
    win.resize(800, 500)    #窗口大小
    data = array.array('i')
    historyLength = 200
    a = 0
    data=np.zeros(historyLength).__array__('d')
    p = win.addPlot()   #生成绘图区域
    p.showGrid(x=True, y=True)
    p.setRange(xRange=[0, historyLength], yRange=[0, 255], padding=0)
    p.setLabel(axis='left', text='y / V')
    p.setLabel(axis='bottom', text='x / point')
    p.setTitle('COMX')  #图像标题
    curve = p.plot()
    curve.setData(data)
    portx = 'COM2'  #端口号
    bps = 9600  #波特率
    mSerial = serial.Serial(portx, int(bps))
    if (mSerial.isOpen()):
        print("open success")
        mSerial.write("hello".encode())
        mSerial.flushInput()
    else:
        print("open failed")
        serial.close()
    th1 = threading.Thread(target=Serial)
    th1.start()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(plotData)
    timer.start(1)  #采样时间(单位ms)
    app.exec_()
