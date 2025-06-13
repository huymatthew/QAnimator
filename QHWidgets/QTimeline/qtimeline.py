from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint, QLine, QRect, QRectF, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPalette, QPen, QPolygon, QPainterPath, QPixmap
from PyQt5.QtWidgets import QApplication, QBoxLayout, QGraphicsLayout, QHBoxLayout, QLabel, QLayout, QPushButton, QSizePolicy, QWidget, QFrame, QScrollArea, QVBoxLayout
import sys

__textColor__ = QColor(187, 187, 187)
__backgroudColor__ = QColor(10, 10, 10)
__font__ = QFont('Decorative', 10)


class QTimeLineKey():
    onSelection = pyqtSignal(bool)
    def __repr__(self) -> str:
        return repr(f"QTimeLineKey({self.timePos})")
    def __init__(self,time,data,parent):
        self.selected = False
        self.p = parent
        self.onDrag = None
        self.keyPosY = 60
        self.timePos = time
        self.position = time * self.p.scale * self.p.sizePerSecond + 5
        self.rect = QRect(self.position -3,
                            self.keyPosY,
                            17,
                            17)
    def paintEvent(self, painter:QPainter) -> None:
        #super().paintEvent(event)
        o = self.p.offsetX

        if self.selected:
            painter.setPen(QPen(QColor(255,255,0)))
            painter.setBrush(QBrush(QColor(255,200,0)))
        else:
            painter.setPen(QPen(QColor(0,200,0)))
            painter.setBrush(QBrush(QColor(0,255,0)))

        poly = QPolygon([
            QPoint(self.rect.x()   ,self.rect.y() +8),
            QPoint(self.rect.x() +8,self.rect.y()),
            QPoint(self.rect.x() +16,self.rect.y()+8),
            QPoint(self.rect.x() +8,self.rect.y()+16)
        ])

        painter.drawPolygon(poly)

    
    def selection(self):
        self.selected = not self.selected
        if self.selected:
            self.p.selectedKeys.append(self)
        else:
            self.p.selectedKeys.remove(self)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        posMouse =  event.pos()
        if event.button() == Qt.MouseButton.LeftButton:
            if self.rect.contains(posMouse) and self.selected:
                self.p.startDragKeys(self.position)
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        try:
            posMouse =  event.pos()
            if event.button() == Qt.MouseButton.LeftButton:
                if self.rect.contains(posMouse):
                    self.selection()
        except Exception as e:print(e)
    def mouseMoving(self, pos) -> None:
        try:
            if self.onDrag is not None:
                self.position = pos-self.onDrag
                self.move(self.position,self.keyPosY)
        except Exception as e:print(e)
    def move(self,x,y):
        self.rect.setRect(x - 3,y,17,17)
        
class VideoSample:

    def __init__(self, duration, color=Qt.darkYellow, picture=None, audio=None):
        self.duration = duration
        self.color = color  # Floating color
        self.defColor = color  # DefaultColor
        if picture is not None:
            self.picture = picture.scaledToHeight(45)
        else:
            self.picture = None
        self.startPos = 0  # Inicial position
        self.endPos = self.duration  # End position


class QTimeLine(QFrame):

    positionChanged = pyqtSignal(int)
    timeChanged = pyqtSignal(float)
    selectionChanged = pyqtSignal(VideoSample)
    onAddKeys = pyqtSignal(list)
    onDeleteKeys = pyqtSignal(list)

    def __init__(self,x=0,y=0,w=600,h=200,parent=None):
        super(QFrame, self).__init__(parent=parent)
        self.duration = 1000
        self.length = 1000
        self.scale = 3
        self.offsetX = 10
        self.sizePerSecond = 50

        # Keys
        self.keys = []#[QTimeLineKey(1,"",self),QTimeLineKey(3,"",self)]
        self.selectedKeys = []
        
        #for key in self.keys:
        #    self.layout().addWidget(key)

        self.setGeometry(x,y,w,h)

        # Set variables
        self.backgroundColor = __backgroudColor__
        self.textColor = __textColor__
        self.font = __font__
        self.pos = None
        self.pointerPos = None
        self.pointerTimePos = None
        self.selectedSample = None
        self.clicking = False  # Check if mouse left button is being pressed
        self.is_in = False  # check if user is in the widget
        self.videoSamples = []  # List of videos samples

        self.selectZone = None

        self.setMouseTracking(True)  # Mouse events
        self.setAcceptDrops(True)
        self.setStyleSheet("QFrame{border:1px solid;border-color:rgb(150,150,150)}")
        #self.setAutoFillBackground(True)  # background

        self.initUI()


    def initUI(self):

        self.setWindowTitle("TESTE")

        # Set Background
        pal = QPalette()
        pal.setColor(QPalette.Background, self.backgroundColor)
        self.setPalette(pal)

    def paintEvent(self, event):
        o = self.offsetX
        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.textColor)
        qp.setFont(self.font)
        qp.setRenderHint(QPainter.Antialiasing)
        w = 0
        # Draw time
        scale = self.getScale()
        if self.scale == 1:
            while w <= self.width():
                qp.drawText(o + w - 40, 5, 100, 100, Qt.AlignHCenter, self.get_time_string(w/self.scale/self.sizePerSecond))
                w += self.sizePerSecond * self.scale * 5
        else:
            while w <= self.width():
                qp.drawText(o + w - 40, 5, 100, 100, Qt.AlignHCenter, self.get_time_string(w/self.scale/self.sizePerSecond))
                w += self.sizePerSecond * self.scale
        # Draw down line
        qp.setPen(QPen(Qt.darkCyan, 5, style=Qt.SolidLine))
        qp.drawLine(2, 45, self.width(), 45)

        # Draw dash lines
        point = 0
        qp.setPen(QPen(self.textColor,1))
        #qp.drawLine(0, 40, self.width(), 40)
        while point <= self.width():
            if point % self.sizePerSecond != 0:
                qp.setPen(QPen(QColor(150,150,150,255),1))
                qp.drawLine(o + self.scale * point, 40, o + self.scale * point, 30)
                qp.drawLine(o + self.scale * point, self.size().height(), o + self.scale * point, 50)
            else:
                qp.setPen(QPen(QColor(255,255,255,255),1))
                qp.drawLine(o + self.scale * point, 40, o + self.scale * point, 20)
                qp.drawLine(o + self.scale * point, self.size().height(), o + self.scale * point, 50)
            point += 10

        if self.pos is not None and self.is_in:
            qp.setPen(QColor(40,40,40))
            qp.drawLine(self.pos.x(), 0,self.pos.x(), self.size().height())

        if self.pointerPos is not None:
            line = QLine(QPoint(o + self.pointerTimePos * self.scale * self.sizePerSecond, 40),
                         QPoint(o + self.pointerTimePos * self.scale * self.sizePerSecond, self.height()))
            poly = QPolygon([QPoint(o + self.pointerTimePos * self.scale * self.sizePerSecond - 10, 20),
                             QPoint(o + self.pointerTimePos * self.scale * self.sizePerSecond + 10, 20),
                             QPoint(o + self.pointerTimePos * self.scale * self.sizePerSecond, 40)])
        else:
            line = QLine(QPoint(o + 0, 0), QPoint(o + 0, self.height()))
            poly = QPolygon([QPoint(o + -10, 20), QPoint(o + 10, 20), QPoint(0, 40)])

        # Draw samples
        t = 0
        for sample in self.videoSamples:
            # Clear clip path
            path = QPainterPath()
            path.addRoundedRect(QRectF(o + t / scale, 50, sample.duration / scale, 200), 10, 10)
            qp.setClipPath(path)

            # Draw sample
            path = QPainterPath()
            qp.setPen(sample.color)
            path.addRoundedRect(QRectF(o + t/scale, 50, sample.duration/scale, 50), 10, 10)
            sample.startPos = o + t/scale
            sample.endPos = o + t/scale + sample.duration/scale
            qp.fillPath(path, sample.color)
            qp.drawPath(path)

            # Draw preview pictures
            if sample.picture is not None:
                if sample.picture.size().width() < sample.duration/scale:
                    path = QPainterPath()
                    path.addRoundedRect(QRectF(o + t/scale, 52.5, sample.picture.size().width(), 45), 10, 10)
                    qp.setClipPath(path)
                    qp.drawPixmap(QRect(o + t/scale, 52.5, sample.picture.size().width(), 45), sample.picture)
                else:
                    path = QPainterPath()
                    path.addRoundedRect(QRectF(o + t / scale, 52.5, sample.duration/scale, 45), 10, 10)
                    qp.setClipPath(path)
                    pic = sample.picture.copy(o + 0, 0, sample.duration/scale, 45)
                    qp.drawPixmap(QRect(o + t / scale, 52.5, sample.duration/scale, 45), pic)
            t += sample.duration

        # Clear clip path
        path = QPainterPath()
        path.addRect(o + self.rect().x(), self.rect().y(), self.rect().width(), self.rect().height())
        qp.setClipPath(path)

        #Draw Select Zone
        if self.selectZone is not None:
            dashPen = QPen(QColor(255,255,255,255),1,Qt.DashLine)
            dashPen.setDashPattern([7,5])
            qp.setPen(dashPen)
            qp.drawRect(self.selectZone.x()
            ,self.selectZone.y()
            ,self.pos.x() - self.selectZone.x()
            ,self.pos.y() - self.selectZone.y())

        #Draw keys
        for key in self.keys:
            key.paintEvent(qp)

        # Draw pointer
        qp.setPen(Qt.red)
        qp.setBrush(QBrush(Qt.red))

        qp.drawPolygon(poly)
        qp.drawLine(line)

        qp.end()


    def keepRange(self, value, min_value, max_value):
        """Keep value in range [min_value, max_value]"""
        return max(min(value, max_value), min_value)

    # Mouse movement
    def mouseMoveEvent(self, e):
        self.pos = e.pos()
        localMousePos = self.keepRange(e.pos().x()-5,0,self.width())
        for key in self.selectedKeys:
            key.mouseMoving(localMousePos)

        # if mouse is being pressed, update pointer
        if self.clicking:
            x = self.pos.x()
            self.pointerPos = x - self.offsetX
            self.pointerPos = self.keepRange(self.pointerPos,0,self.size().width())
            self.positionChanged.emit(x)
            self.checkSelection(x)
            self.pointerTimePos = self.pointerPos/self.scale/self.sizePerSecond
            self.pointerTimePos = round(self.pointerTimePos,1)
            self.timeChanged.emit(self.pointerTimePos)

        self.update()

    # Mouse pressed
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            x = e.pos().x()
            self.pointerPos = x - self.offsetX
            self.pointerPos = self.keepRange(self.pointerPos,0,self.size().width())
            self.positionChanged.emit(x)
            self.pointerTimePos = self.pointerPos/self.scale/self.sizePerSecond
            self.pointerTimePos = round(self.pointerTimePos,1)
            self.timeChanged.emit(self.pointerTimePos)

            self.checkSelection(x)

            self.update()
            self.clicking = True  # Set clicking check to true
        elif e.button() == Qt.RightButton:
            self.selectZone = e.pos()
        for key in self.keys:
            key.mousePressEvent(e)
        self.update()

    # Mouse release
    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        if e.button() == Qt.LeftButton:
            self.clicking = False  # Set cliking check to false
            self.endDragKeys()
        if e.button() == Qt.RightButton:
            
            
            if self.selectZone is not None:
                sRect = QRect(self.selectZone.x()
                ,self.selectZone.y()
                ,e.pos().x() - self.selectZone.x()
                ,e.pos().y() - self.selectZone.y())
                self.selectZone = None
                
                for key in self.keys:
                    if sRect.contains(key.rect):
                        key.selection()

                self.update()
        for key in self.keys:
            key.mouseReleaseEvent(e)
        self.update()
            
    # Enter
    def enterEvent(self, e):
        self.is_in = True

    # Leave
    def leaveEvent(self, e):
        self.is_in = False
        self.update()
    
    def dragEnterEvent(self, event):

        if event.mimeData().hasFormat("application/x-icon-and-text"):

            event.accept() 
        else:

            event.ignore()

    def wheelEvent(self,e:QtGui.QWheelEvent):
        self.scale += e.angleDelta().y()/120
        self.scale = self.keepRange(self.scale,1,5)
        for key in self.keys:
            key.position = key.timePos * self.scale * self.sizePerSecond + 5
            key.move(key.position,key.keyPosY)

        self.update()

    # check selection
    def checkSelection(self, x):
        # Check if user clicked in video sample
        for sample in self.videoSamples:
            if sample.startPos < x < sample.endPos:
                sample.color = Qt.darkCyan
                if self.selectedSample is not sample:
                    self.selectedSample = sample
                    self.selectionChanged.emit(sample)
            else:
                sample.color = sample.defColor

    # Get time string from seconds
    def get_time_string(self, seconds):
        m, s = divmod(seconds, 60)
        return "%02d:%02d" % (m, s)

    # Get scale from length
    def getScale(self):
        return self.scale

    # Get duration
    def getDuration(self):
        return self.duration

    # Get selected sample
    def getSelectedSample(self):
        return self.selectedSample

    # Set background color
    def setBackgroundColor(self, color):
        self.backgroundColor = color

    # Set text color
    def setTextColor(self, color):
        self.textColor = color

    # Set Font
    def setTextFont(self, font):
        self.font = font

    # Get Keys Selected
    def getSelectedKeys(self):
        return self.selectedKeys

    def startDragKeys(self,pos):
        for key in self.selectedKeys:
            key.onDrag = pos - key.position

    def endDragKeys(self):
        for key in self.selectedKeys:
            key.onDrag = None
            key.timePos = round((key.position-5) / self.scale / self.sizePerSecond,1)
            key.position = key.timePos * self.scale * self.sizePerSecond + 5
            key.move(key.position,key.keyPosY)

    def addKeys(self,keys:list[QTimeLineKey]):
        self.onAddKeys.emit(keys)
        self._addKeys(keys)
    def _addKeys(self,keys):
        for key in keys:
            self.keys.append(key)
        self.update()

    def removeKeys(self):
        self.onDeleteKeys.emit(self.selectedKeys)
        self._removeKeys(self.selectedKeys)

    def _removeKeys(self,keys):
        
        for key in keys:
            self._removeKey(key)
        self.update()
    def _removeKey(self,key):
        self.keys.remove(key)

    def movePointer(self,time):
        self.pointerTimePos = time
        self.pointerPos = self.pointerTimePos * self.scale * self.sizePerSecond + self.offsetX
        self.update()
    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e: QtGui.QDropEvent):
        try:
            data = e.mimeData().text().split("\n")
            if len(data) > 1:
                data = data[:-1]
            time = e.pos().x() / self.scale / self.sizePerSecond
            time = round(time,1)
            self.addKeys([QTimeLineKey(time + i / 5,data[i],self) for i in range(len(data))])
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QTimeLine(500,500,1000,300)
    win.show()
    win.keys.append(QTimeLineKey(2,"",win))
    sys.exit(app.exec_())