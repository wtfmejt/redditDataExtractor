# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Wed Jul 16 23:10:37 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(573, 394)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.defaultSubredditListLabel = QtGui.QLabel(SettingsDialog)
        self.defaultSubredditListLabel.setObjectName(_fromUtf8("defaultSubredditListLabel"))
        self.horizontalLayout.addWidget(self.defaultSubredditListLabel)
        self.defaultSubredditListComboBox = QtGui.QComboBox(SettingsDialog)
        self.defaultSubredditListComboBox.setObjectName(_fromUtf8("defaultSubredditListComboBox"))
        self.horizontalLayout.addWidget(self.defaultSubredditListComboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(SettingsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.subLimitTextEdit = QtGui.QLineEdit(SettingsDialog)
        self.subLimitTextEdit.setCursorPosition(2)
        self.subLimitTextEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.subLimitTextEdit.setObjectName(_fromUtf8("subLimitTextEdit"))
        self.horizontalLayout_4.addWidget(self.subLimitTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.getExternalContentCheckBox = QtGui.QCheckBox(SettingsDialog)
        self.getExternalContentCheckBox.setObjectName(_fromUtf8("getExternalContentCheckBox"))
        self.horizontalLayout_6.addWidget(self.getExternalContentCheckBox)
        self.avoidDuplCheckBox = QtGui.QCheckBox(SettingsDialog)
        self.avoidDuplCheckBox.setChecked(True)
        self.avoidDuplCheckBox.setObjectName(_fromUtf8("avoidDuplCheckBox"))
        self.horizontalLayout_6.addWidget(self.avoidDuplCheckBox)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.defaultUserListLabel = QtGui.QLabel(SettingsDialog)
        self.defaultUserListLabel.setObjectName(_fromUtf8("defaultUserListLabel"))
        self.horizontalLayout_5.addWidget(self.defaultUserListLabel)
        self.defaultUserListComboBox = QtGui.QComboBox(SettingsDialog)
        self.defaultUserListComboBox.setObjectName(_fromUtf8("defaultUserListComboBox"))
        self.horizontalLayout_5.addWidget(self.defaultUserListComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(SettingsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.hotBtn = QtGui.QRadioButton(SettingsDialog)
        self.hotBtn.setChecked(True)
        self.hotBtn.setObjectName(_fromUtf8("hotBtn"))
        self.horizontalLayout_3.addWidget(self.hotBtn)
        self.newBtn = QtGui.QRadioButton(SettingsDialog)
        self.newBtn.setChecked(False)
        self.newBtn.setObjectName(_fromUtf8("newBtn"))
        self.horizontalLayout_3.addWidget(self.newBtn)
        self.topBtn = QtGui.QRadioButton(SettingsDialog)
        self.topBtn.setObjectName(_fromUtf8("topBtn"))
        self.horizontalLayout_3.addWidget(self.topBtn)
        self.risingBtn = QtGui.QRadioButton(SettingsDialog)
        self.risingBtn.setObjectName(_fromUtf8("risingBtn"))
        self.horizontalLayout_3.addWidget(self.risingBtn)
        self.controversialBtn = QtGui.QRadioButton(SettingsDialog)
        self.controversialBtn.setObjectName(_fromUtf8("controversialBtn"))
        self.horizontalLayout_3.addWidget(self.controversialBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.line_2 = QtGui.QFrame(SettingsDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)
        self.line_3 = QtGui.QFrame(SettingsDialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.getSubmissionContentCheckBox = QtGui.QCheckBox(SettingsDialog)
        self.getSubmissionContentCheckBox.setChecked(True)
        self.getSubmissionContentCheckBox.setObjectName(_fromUtf8("getSubmissionContentCheckBox"))
        self.verticalLayout.addWidget(self.getSubmissionContentCheckBox)
        self.getCommentDataCheckBox = QtGui.QCheckBox(SettingsDialog)
        self.getCommentDataCheckBox.setObjectName(_fromUtf8("getCommentDataCheckBox"))
        self.verticalLayout.addWidget(self.getCommentDataCheckBox)
        self.line = QtGui.QFrame(SettingsDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.filterExternalContentCheckBox = QtGui.QCheckBox(SettingsDialog)
        self.filterExternalContentCheckBox.setObjectName(_fromUtf8("filterExternalContentCheckBox"))
        self.horizontalLayout_7.addWidget(self.filterExternalContentCheckBox)
        self.filterCommentContentCheckBox = QtGui.QCheckBox(SettingsDialog)
        self.filterCommentContentCheckBox.setObjectName(_fromUtf8("filterCommentContentCheckBox"))
        self.horizontalLayout_7.addWidget(self.filterCommentContentCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.filterTable = QtGui.QTableWidget(SettingsDialog)
        self.filterTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.filterTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.filterTable.setObjectName(_fromUtf8("filterTable"))
        self.filterTable.setColumnCount(5)
        self.filterTable.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.filterTable.setHorizontalHeaderItem(4, item)
        self.filterTable.horizontalHeader().setVisible(True)
        self.filterTable.horizontalHeader().setDefaultSectionSize(110)
        self.filterTable.verticalHeader().setVisible(False)
        self.filterTable.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.filterTable)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.dialogButtonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.dialogButtonBox.setObjectName(_fromUtf8("dialogButtonBox"))
        self.verticalLayout.addWidget(self.dialogButtonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.dialogButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings", None))
        self.defaultSubredditListLabel.setToolTip(_translate("SettingsDialog", "The subreddit list that will display on starting the application.", None))
        self.defaultSubredditListLabel.setText(_translate("SettingsDialog", "Default Subreddit List", None))
        self.label_2.setToolTip(_translate("SettingsDialog", "The number of posts to retrieve from the subreddit. A max of 100 can be downloaded at a time. Download again at a later date to get the next (most recent) 100.", None))
        self.label_2.setText(_translate("SettingsDialog", "Max Posts Retrieved in Subreddit Content Download [1-100]", None))
        self.subLimitTextEdit.setText(_translate("SettingsDialog", "10", None))
        self.getExternalContentCheckBox.setToolTip(_translate("SettingsDialog", "Select to attempt to download images / gifs / gfys linked to by a reddit submission.", None))
        self.getExternalContentCheckBox.setText(_translate("SettingsDialog", "Download External Content of Submission", None))
        self.avoidDuplCheckBox.setToolTip(_translate("SettingsDialog", "Attempt to avoid downloading images, gifs, or gfys that have already been downloaded for the same user or subreddit.", None))
        self.avoidDuplCheckBox.setText(_translate("SettingsDialog", "Avoid Downloading Duplicate Images If Possible", None))
        self.defaultUserListLabel.setToolTip(_translate("SettingsDialog", "The user list that will display on starting the application.", None))
        self.defaultUserListLabel.setText(_translate("SettingsDialog", "Default User List", None))
        self.label.setToolTip(_translate("SettingsDialog", "When downloading subreddit content, this determines the types of posts that are downloaded. E.g. to get the top 10 new posts in the subreddits, select \"New\".", None))
        self.label.setText(_translate("SettingsDialog", "Sort Subreddit Content by: ", None))
        self.hotBtn.setText(_translate("SettingsDialog", "Hot", None))
        self.newBtn.setText(_translate("SettingsDialog", "New", None))
        self.topBtn.setText(_translate("SettingsDialog", "Top", None))
        self.risingBtn.setText(_translate("SettingsDialog", "Rising", None))
        self.controversialBtn.setText(_translate("SettingsDialog", "Controversial", None))
        self.getSubmissionContentCheckBox.setToolTip(_translate("SettingsDialog", "Select to download the title, self-text, comments, upvote statistics, and other information in a json-encoded text file.", None))
        self.getSubmissionContentCheckBox.setText(_translate("SettingsDialog", "Download Submission Content", None))
        self.getCommentDataCheckBox.setToolTip(_translate("SettingsDialog", "Select to attempt to download images, gifs, and gfys from the comments in a submission.", None))
        self.getCommentDataCheckBox.setText(_translate("SettingsDialog", "Download External Content In Comments", None))
        self.filterExternalContentCheckBox.setToolTip(_translate("SettingsDialog", "Dowload external images / gifs / gfys only if the following criteria are met.", None))
        self.filterExternalContentCheckBox.setText(_translate("SettingsDialog", "Only download external content when:", None))
        self.filterCommentContentCheckBox.setToolTip(_translate("SettingsDialog", "Download json encoded submission data only if the following criteria are met.", None))
        self.filterCommentContentCheckBox.setText(_translate("SettingsDialog", "Only download submission content when:", None))
        self.filterTable.setToolTip(_translate("SettingsDialog", "Select the filters you would like to apply to the download. Will download the content only if the submission or a comment within the submission has the matching criteria.", None))
        item = self.filterTable.verticalHeaderItem(0)
        item.setText(_translate("SettingsDialog", "New Row", None))
        item = self.filterTable.horizontalHeaderItem(0)
        item.setText(_translate("SettingsDialog", "Content Type", None))
        item.setToolTip(_translate("SettingsDialog", "The type of content to filter by. Either submissions or comments within a submission.", None))
        item = self.filterTable.horizontalHeaderItem(1)
        item.setText(_translate("SettingsDialog", "Property", None))
        item.setToolTip(_translate("SettingsDialog", "The property of the content. E.g. the author of a submission (the redditor), or the score of a comment in the submission.", None))
        item = self.filterTable.horizontalHeaderItem(2)
        item.setText(_translate("SettingsDialog", "Operator", None))
        item.setToolTip(_translate("SettingsDialog", "The operator to search the property with. E.g. contains means a download will occur if the string in the value column is in the property of the submssion / comment.", None))
        item = self.filterTable.horizontalHeaderItem(3)
        item.setText(_translate("SettingsDialog", "Value", None))
        item.setToolTip(_translate("SettingsDialog", "The value to match by using the operator. If you want a boolean, enter True or False.", None))
        item = self.filterTable.horizontalHeaderItem(4)
        item.setText(_translate("SettingsDialog", "And / Or / Xor", None))
        item.setToolTip(_translate("SettingsDialog", "If you want multiple filters, select this box and select the operator to group the filters by. The filters must be the same. E.g. submission author equals \"foo\" AND comment score greater than 100.", None))

