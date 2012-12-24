#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import sys
import webbrowser

import programme


class JVNewsGui(QtGui.QWidget):
    def __init__(self): 
        super(JVNewsGui, self).__init__()

        self.launchWin()
    
    def launchWin(self):
        self.layout = QtGui.QGridLayout()
        
    
        self.layout.addWidget(self.categories_box(), 0, 0) 

        self.setLayout(self.layout)
        self.setWindowTitle("PyJV NEWS")
        self.show()

    def categories_box(self):
        groupBox = QtGui.QGroupBox("Categories")
        self.liste_categories = QtGui.QListWidget()

        for categorie in programme.categories:
            self.liste_categories.addItem(categorie)

        self.connect(self.liste_categories, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.itemDoubleClicked)


        vBox = QtGui.QVBoxLayout()
        vBox.addWidget(self.liste_categories)

        groupBox.setLayout(vBox)
        return groupBox
    
    def itemDoubleClicked(self):
        self.categorie = self.liste_categories.currentItem().text() 
        self.newsDialog()

    def newsDialog(self):
        diaLayout = QtGui.QVBoxLayout()
        self.news = programme.genNews(self.categorie)

        self.newsBox = QtGui.QGroupBox("News")
        liste_lab_news = []
        
        dialog = QtGui.QDialog()

        for new, link in self.news:
            liste_lab_news.append(QtGui.QPushButton(new))

        grid = QtGui.QGridLayout()

        for i, buttons in enumerate(liste_lab_news):
            buttons.clicked.connect(self.openInBrowser)
            grid.addWidget(buttons, i, 0)
        
        self.newsBox.setLayout(grid)

        diaLayout.addWidget(self.newsBox)
        dialog.setLayout(diaLayout)
        dialog.setWindowTitle("News de %s" % self.categorie)

        dialog.exec_()

    def openInBrowser(self):
        for new, link in self.news:
            if unicode(self.sender().text()) == new:
                webbrowser.open(link)


def main():
    app = QtGui.QApplication(sys.argv)
    jvne = JVNewsGui()
    sys.exit(app.exec_())


if __name__ == '__main__': main()
