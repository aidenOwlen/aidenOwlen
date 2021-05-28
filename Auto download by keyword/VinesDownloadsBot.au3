#include<GuiConstantsEx.au3>
#include<FileConstants.au3>
#include<File.au3>
#include<Inet.au3>
#include<InetConstants.au3>
#include<StringConstants.au3>
#include<Ie.au3>
#include<AutoitConstants.au3>
#include<StaticConstants.au3>
#include<misc.au3>
#include<WindowsConstants.au3>
#include<FontConstants.au3>
#include<ColorConstants.Au3>
#include<EditConstants.Au3>


Global $i, $p, $string[101], $z, $Download, $read, $trim

opt("GuiOnEventMode", 1)


$gui = GuiCreate("", 400, 320, -1, -1, $WS_POPUP)
GuiSetOnEVent($GUI_EVENT_CLOSE, "fermer")
GuiSetBkColor(0x52BEF9)


GuiCtrlCreateLabel("Vine.co", 152, 30, 400, 100)
GuiCtrlSetFont(-1, 16, $FW_EXTRABOLD)
GuiCtrlSetColor(-1, $COLOR_RED)


GuiCtrlCreateLabel("Exclussively on fiverr", 85, 130, 400, 100)
GuiCtrlSetFont(-1, 16, "", "", "Mv boli")
;GuiCtrlSetColor(-1, $COLOR_RED)



$add = GuiCtrlCreateButton("Read Me", 245, 245, 120)
GuiCtrlSetBkColor(-1, $COLOR_BLACK)
GuiCtrlSetColor(-1, $COLOR_GREEN)
GuiCtrlSetFont(-1, -1, $FW_EXTRABOLD)
GuiCtrlSetOnEvent($add, "add")

$start = GuiCtrlCreateButton("Start the bot", 245, 275, 120)
GuiCtrlSetBkColor(-1, $COLOR_BLACK)
GuiCtrlSetColor(-1, $COLOR_GREEN)
GuiCtrlSetFont(-1, -1, $FW_EXTRABOLD)
GuiCtrlSetOnEvent($start, "start")

GuiCtrlCreateLabel("=>", 370, 280)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD)






GuiSetState(@SW_SHOW, $gui)



While 1
   sleep(300)
Wend

func start()
;############# CREATE MULTIPLE FOLDERS ##########################################"
for $p = 1 to 20
If FileExists(@DESKTOPDIR & "\vinedownload\channel" & $p & "\" ) = False then
_FileCreate(@DESKTOPDIR & "\vinedownload\channel" & $p & "\")
endif
next
;############# CREATE MULTIPLE FOLDERS ##########################################"

;WAIT A LITTLE :
Sleep(20000)
;WAIT A LITTLE

;############# DOWNLOAD JSON FILES ##########################################"
If FileExists(@DESKTOPDIR & "\VIDEOSVINE\FirstOfEachPage\") = False then
 _FileCreate(@DESKTOPDIR & "\VIDEOSVINE\FirstOfEachPage\")
 EndIf
for $p = 1 to 20
     If FileExists(@DESKTOPDIR & "\VIDEOSVINE\channel" & $p & "\") = False then
   _FileCreate(@DESKTOPDIR & "\VIDEOSVINE\channel" & $p & "\")
   endif
for $i = 1 to 20
   If FileExists(@DESKTOPDIR & "\VIDEOSVINE\channel" & $p & "\page" & $i & "\") = False then
   _FileCreate(@DESKTOPDIR & "\VIDEOSVINE\channel" & $p & "\page" & $i & "\")
   endif
$Download = InetGet("https://vine.co/api/timelines/channels/" & $p & "/popular?page=" & $i & "&anchor=&size=20",@DESKTOPDIR & "\vinedownload\channel" & $p & "\" & $i & ".json", "", 0)
sleep(3000)

;++ SCRAP URL AND DOWNLOAD ++
$read = FileRead(@DESKTOPDIR & "\vinedownload\channel" & $p & "\" & $i & ".json")
$string = StringRegExp($read, "http://v.cdn.vine.co/r/videos[0123456789AZERTYUIOPM#LKJHGF><DSQWç^X¨¨CVBN.azertyu+[{}@i_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}/[0123456789AZERTYUIOPMLKJHGFDSQWXCVBN.azertyui_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}", $STR_REGEXPARRAYMATCH)
If Isarray($string) then
InetGet($string[0], @DESKTOPDIR & "\VIDEOSVINE\FirstOfEachPage\" & $i & $p & ".mp4")
endif
for $z = 1 to 100
If isarray($string) then
$trim = StringTrimLeft($read, StringInStr($read, $string[0]))
endif
$string = StringRegExp($trim, "http://v.cdn.vine.co/r/videos[0123456789AZERTYUIOPMLKJHGFDSQWXCVBN.azertyui_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}/[0123456789AZERTYUIOPMLKJHGFDSQWXCVBN.azertyui_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}", $STR_REGEXPARRAYMATCH)

If isarray($string) then
InetGet($string[0], @DESKTOPDIR & "\VIDEOSVINE\channel" & $p & "\page" & $i & "\" & $z & ".mp4")
endif
next
;++ SCRAP URL AND DOWNLOAD ++

next
next
;############# DOWNLOAD JSON FILES !#########################################
endfunc

;
;$read = FileRead(@DESKTOPDIR & "\1.json")
;$string = StringRegExp($read, "http://v.cdn.vine.co/r/videos[0123456789AZERTYUIOPM#LKJHGF><DSQWç^X¨¨CVBN.azertyu+[{}@i_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}/[0123456789AZERTYUIOPMLKJHGFDSQWXCVBN.azertyui_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}", $STR_REGEXPARRAYMATCH)
;InetGet($string[0], @DESKTOPDIR & "\first.mp4")


;for $z = 1 to 100
;$trim = StringTrimLeft($read, StringInStr($read, $string[0]))
;$string = StringRegExp($trim, "http://v.cdn.vine.co/r/videos[0123456789AZERTYUIOPMLKJHGFDSQWXCVBN.azertyui_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}/[0123456789AZERTYUIOPMLKJHGFDSQWXCVBN.azertyui_-²&é!:;,?/§\'~(-è_çà)=,|opmlkjhgfdsqwxcvbn]{1,400}", $STR_REGEXPARRAYMATCH)
;InetGet($string[0], @DESKTOPDIR & "\" & $z & ".mp4")
;next

func add()
   _FileCreate(@DESKTOPDIR & "\ReadMeVine.txt")
   Shellexecute(@DESKTOPDIR & "\ReadMeVine.txt")
   sleep(3000)
   send("Hello" & @CRLF & "It will download all vines, chanel by chanel, page by page" & @CRLF & "if you face any problem with it => teamviewer support !" & @CRLF & "If you like my work => feel free to let a good review" & @CRLF & @CRLF & "Regards & good luck !")
EndFunc

func fermer()
   Exit
endfunc