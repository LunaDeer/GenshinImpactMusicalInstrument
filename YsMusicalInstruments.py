import ctypes
import datetime
import os
import sys
import time
import pydirectinput
import win32con

noteDict = {
    '0':'',

    '1..':'',
    '2..':'',
    '3..':'',
    '4..':'',
    '5..':'',
    '6..':'',
    '7..':'',

    '1.':'z',
    '2.':'x',
    '3.':'c',
    '4.':'v',
    '5.':'b',
    '6.':'n',
    '7.':'m',

    '1':'a',
    '2':'s',
    '3':'d',
    '4':'f',
    '5':'g',
    '6':'h',
    '7':'j',

    '.1':'q',
    '.2':'w',
    '.3':'e',
    '.4':'r',
    '.5':'t',
    '.6':'y',
    '.7':'u',
    
    '..1':'',
    '..2':'',
    '..3':'',
    '..4':'',
    '..5':'',
    '..6':'',
    '..7':'',
}

majorTremoloHarmonicaGamut = ['5..','2.','1.','4.','3.','6.','5.','7.','1','2','3','4','5','6','.1','7','.3','.2','.5','.4','..1','.6','..3','.7']
'''大调复音口琴音阶
'''

minorTremoloHarmonicaGamut = ['3..','7..','6..','2.','1.','4.','3.','5.','6.','7.','1','2','3','4','6','5','.1','7','.3','.2','.6','.4','..1','.5']
'''小调复音口琴音阶
'''

class YsMusicalInstruments:
    __bpm:int
    __notesList:list
    __harmonicaGamut:list
    '''复音口琴音阶
    '''
    __blowHoleList: list
    '''吹气孔列表
    '''
    isPlaying:bool = False
    def __init__(self,bpm,harmonicaGamut = majorTremoloHarmonicaGamut):
        '''
        bpm 就是bpm
        harmonicaGamut 用什么音阶minorTremoloHarmonicaGamut|majorTremoloHarmonicaGamut
        '''
        pydirectinput.PAUSE = 0
        self.__bpm = bpm
        self.__notesList = []
        self.__harmonicaGamut = harmonicaGamut
        self.__blowHoleList = harmonicaGamut[0:6][::2]
        self.__blowHoleList = [i.replace('.','') for i in self.__blowHoleList]
    def __addChord(self,beat:int,note:str,holeNum:int,useRootNote:bool = True):
        chordList =  self.__getChordList(note,holeNum)
        if(useRootNote == False):
            chordList.pop()
        self.__notesList.append({"notes":chordList,"beat":beat})
    def addNote(self,beat:int,notes:list,holeNum:int or None = None,useRootNote:bool = True):
        """添加音符

        beat 几分音符 int|list [4,8,16,32 ...],浮点:比如4分音符浮点，请写成[4,8]；
        notes 音符列表；
        holeNum 吹或者吸和旋孔的个数，比如吹135就传3，2467就传4；
        useRootNote 是否吹根音，默认为吹；
        """
        if(not holeNum):
            self.__notesList.append({"notes":notes,"beat":beat})
        else:
            self.__addChord(beat,notes[0],holeNum,useRootNote)
    def __getChordList(self,rootNote:str,holeNum:int):
        isBlow = rootNote.replace('.','') in self.__blowHoleList
        tempList = []
        if(isBlow):
            tempList = self.__harmonicaGamut[::2]
        else:
            tempList = self.__harmonicaGamut[1::2]

        start = tempList.index(rootNote)-holeNum+1
        start = max(0,start)
        return tempList[start:tempList.index(rootNote)+1]
    def addMordent(self,beats,note):
        '''添加波音
        '''
        if(isinstance(beats,list)):
            for beat in beats:
                for i in range(int(64/beat)):
                    if(i % 2 == 0):
                        self.addNote(64,[note[0]])
                    else:
                        self.addNote(64,[note[1]])
        else:
            for i in range(int(64/beats)):
                if(i % 2 == 0):
                    self.addNote(64,[note[0]])
                else:
                    self.addNote(64,[note[1]])
    def play(self):
        '''播放
        '''
        if(len(self.__notesList) == 0):
            return
        self.isPlaying = True
        for notes in self.__notesList:
            if(not self.isPlaying):
                break
            for index,note in enumerate(notes["notes"]):
                delay = 0
                if(isinstance(notes["beat"],list)):
                    for beat in notes["beat"]:
                        delay += (60/self.__bpm)/(beat/4)
                else:
                    delay += (60/self.__bpm)/(notes["beat"]/4)
                pydirectinput.press(noteDict[note])
            time.sleep(delay)
    def stop(self):
        '''停止播放
        '''
        self.isPlaying = False
    def cutPlayState(self):
        '''切换播放状态
        '''
        if(self.isPlaying):
            self.stop()
        else:
            self.play()
