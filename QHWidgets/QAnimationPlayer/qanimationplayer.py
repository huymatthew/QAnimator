from PyQt5 import QtWidgets,QtCore,uic,QtGui
import sys

class QAnimationPlayer(QtWidgets.QWidget):
    onTimeUpdate = QtCore.pyqtSignal(float)
    def __init__(self,parent=None):
        super(QAnimationPlayer, self).__init__(parent=parent)
        uic.loadUi('QHWidgets/QAnimationPlayer/ui/main.ui', self)
        #self.show()
        self.sprites = []
        self.current_frame = 0
        self._timer = QtCore.QTimer(interval=100,timeout=self.update_animation)
        self.playing = False

        self.playIcon  = QtGui.QIcon(QtGui.QPixmap("QHWidgets/QAnimationPlayer/icon/play.png"))
        self.pauseIcon = QtGui.QIcon(QtGui.QPixmap("QHWidgets/QAnimationPlayer/icon/pause.png"))

        self.playBtn.clicked.connect(self.play)
    def load(self, image_path, sprite_width, sprite_height):
        pixmap = QtGui.QPixmap(image_path)
        width, height = pixmap.width(), pixmap.height()
        for x in range(0, width, sprite_width):
            for y in range(0, height, sprite_height):
                self.sprites.append(pixmap.copy(x, y, 
                                                sprite_width, sprite_height))
    
    def play(self):
        self.playing = not self.playing
        if not self.playing:
            self._timer.stop()
            self.playBtn.setIcon(self.playIcon)
        else:
            self._timer.start()
            self.playBtn.setIcon(self.pauseIcon)
    def setTime(self,time):
        try:
            self.current_frame = round(time * 10)
            if self.current_frame >= len(self.sprites):
                self.current_frame = 0
            self.player.setPixmap(self.sprites[self.current_frame])
            self.player.update()
        except Exception as e :print(e)
    def update_animation(self):
        self.player.setPixmap(self.sprites[self.current_frame])
        self.player.update()
        self.onTimeUpdate.emit(self.current_frame/10)
        
        self.current_frame += 1
        if self.current_frame >= len(self.sprites):
            self.current_frame = 0

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        super().resizeEvent(a0)
        pSize = a0.size()
        w = pSize.width() - 5
        h = pSize.height() - 50
        self.player.setGeometry(0,10,w,h)
        self.controller.setGeometry(0,h + 10,w,40)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = QAnimationPlayer()
    player.load("A.png",32,32)
    player.show()
    sys.exit(app.exec_())