#include<AutoITConstants.Au3>
#include<GuiConstantsEx.Au3>
#include<ColorConstants.Au3>
#include<EditConstants.Au3>
#include<StaticConstants.au3>
#include<_Startup.au3>
#include <Date.au3>
#include<WindowsConstants.au3>
#include<misc.au3>
#include<FileConstants.au3>
#include<File.au3>
#include<FontConstants.au3>


opt("GuiOnEventMode", 1)


$gui = GuiCreate("", 400, 320, -1, -1, $WS_POPUP)
GuiSetOnEVent($GUI_EVENT_CLOSE, "fermer")
GuiSetBkColor(0x52BEF9)
$combo1 = GuiCtrlCreateCombo("00", 90, 5, 60)
for $i = 0 to 9
GuiCtrlSetData($combo1, "0" & $i)
next

for $i = 10 to 23
   GuiCtrlSetData($combo1, $i)
next

$combo2 = GuiCtrlCreateCombo("00", 90, 35, 60)
for $i = 0 to 9
GuiCtrlSetData($combo2, "0" & $i)
next
for $i = 10 to 59
   GuiCtrlSetData($combo2, $i)
next

GuiCtrlCreateLabel("Hour", 55, 7)
GuiCtrlSetColor(-1, $COLOR_YELLOW)
GuiCtrlSetFont(-1, 10, "", "", "Mv boli")

GuiCtrlCreateLabel("Min", 55, 35)
GuiCtrlSetColor(-1, $COLOR_YELLOW)
GuiCtrlSetFont(-1, 10, "", "", "Mv boli")


$Sunday = GuiCtrlCreateRadio("Sunday", 5, 85, 75)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$Monday = GuiCtrlCreateRadio("Monday", 125, 85, 75)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$Tuesday = GuiCtrlCreateRadio("Tuesday", 245, 85, 75)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$Wednesday = GuiCtrlCreateRadio("Wednesday", 5, 115, 95)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$Thursday = GuiCtrlCreateRadio("Thursday", 125, 115, 95)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$Friday = GuiCtrlCreateRadio("Friday", 125, 145, 95)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$Saturday = GuiCtrlCreateRadio("Saturday", 245, 145, 95)
GuiCtrlSetFont(-1, 10, $FW_EXTRABOLD, "", "Mv boli")

$add = GuiCtrlCreateButton("Add Post", 245, 245, 120)
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



func add()
   $ReadCombo1 = GuiCtrlRead($combo1)
   $ReadCombo2 = GuiCtrlRead($combo2)
   If GuiCtrlRead($Monday) = $GUI_CHECKED then
 _FileCreate(@DESKTOPDIR & "\Monday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(300)
		If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
		_FileCreate(@DESKTOPDIR & "\Monday\hour.ini")
		endif
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Monday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Monday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".jpg")

		ShellExecute(@DESKTOPDIR & "\Monday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
	endif
	If GuiCtrlRead($Sunday) = $GUI_CHECKED then
	 _FileCreate(@DESKTOPDIR & "\Sunday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(300)
		If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
		_FileCreate(@DESKTOPDIR & "\Sunday\hour.ini")
		EndIf
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Sunday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Sunday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".jpg")

		ShellExecute(@DESKTOPDIR & "\Sunday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
	endif
	If GuiCtrlRead($Tuesday) = $GUI_CHECKED then
	 _FileCreate(@DESKTOPDIR & "\Tuesday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(300)
		If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
		_FileCreate(@DESKTOPDIR & "\Tuesday\hour.ini")
		endif
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Tuesday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Tuesday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".jpg")

		ShellExecute(@DESKTOPDIR & "\Tuesday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
	endif
	If GuiCtrlRead($Saturday) = $GUI_CHECKED then
	    _FileCreate(@DESKTOPDIR & "\Saturday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(300)
		If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
		_FileCreate(@DESKTOPDIR & "\Saturday\hour.ini")
		endif
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Saturday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Saturday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".jpg")

		ShellExecute(@DESKTOPDIR & "\Saturday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
	endif
	If GuiCtrlRead($Friday) = $GUI_CHECKED then
	   If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
 _FileCreate(@DESKTOPDIR & "\Friday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
 endif
		sleep(300)
		_FileCreate(@DESKTOPDIR & "\Friday\hour.ini")
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Friday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Friday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".jpg")

		ShellExecute(@DESKTOPDIR & "\Friday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
	endif
	If GuiCtrlRead($Wednesday) = $GUI_CHECKED then
		 _FileCreate(@DESKTOPDIR & "\Wednesday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(300)
		If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
		_FileCreate(@DESKTOPDIR & "\Wednesday\hour.ini")
		endif
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Wednesday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Wednesday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 ".jpg")

		ShellExecute(@DESKTOPDIR & "\Wednesday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
endif
	If GuiCtrlRead($Thursday) = $GUI_CHECKED then
	    _FileCreate(@DESKTOPDIR & "\Thursday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(300)
		If fileexists(@DESKTOPDIR & "\Sunday\hour.ini") = False then
		_FileCreate(@DESKTOPDIR & "\Thursday\hour.ini")
		endif
		sleep(300)
		$op = FileOpen(@DESKTOPDIR & "\Thursday\hour.ini", 1)
		FileWrite($op, $ReadCombo1 & ":" & $ReadCombo2 & @CRLF)
		FileClose($op)
		sleep(500)
		$File = FileOpenDialog("Please select a picture to post", @DESKTOPDIR , "All (*.*)")
		FileCopy($File, @DESKTOPDIR & "\Thursday\" & $ReadCombo1 & $Readcombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".jpg")

		ShellExecute(@DESKTOPDIR & "\Thursday\" & $ReadCombo1 & $ReadCombo2 & "\" & $ReadCombo1 & $ReadCombo2 & ".ini")
		sleep(200)
		MsgBox(0, "Subject", "Please enter your post here")
	endif
endfunc

func start()
  $day = _DateDayOfweek(@WDAY)
  If FileExists(@DESKTOPDIR & "\" & $day & "\hour.ini") then
	 $op = FileOpen(@DESKTOPDIR & "\" & $day & "\hour.ini", 0)
	 $line = _FileCountLines(@DESKTOPDIR & "\" & $day & "\hour.ini")
	 for $i = 1 to $line
	  $radL = FileReadLine($op, $i)
	  splashtexton("Updates of the day at : ", $radL, 200, 65)
	  sleep(1000)
	  splashoff()
   Next

   While 1
	  $line = _FileCountLines(@DESKTOPDIR & "\" & $day & "\hour.ini")
	  $op = FileOpen(@DESKTOPDIR & "\" & $day & "\hour.ini", 0)
	   for $i = 1 to $line
	  $radL = FileReadLine($op, $i)
	  if @HOUR & ":" & @MIN = $radL then
		 $split = StringSplit($radL, ":")
		 Shellexecute("www.facebook.com")
		 $Read = FileOpen(@DESKTOPDIR & "\" & $day & "\" & $split[1] & $split[2] & "\" & $split[1] & $split[2] & ".ini")
		 WinWaitActive("Facebook - Google Chrome")
		 sleep(2000)
		 MouseClick("LEFT", 481, 169)
		 sleep(2000)
		 $line2 = _FileCountLines(@DESKTOPDIR & "\" & $day & "\" & $split[1] & $split[2] & "\" & $split[1] & $split[2] & ".ini")
		 for $i = 1 to $line2
		 $Reaad = FileReadLine($Read, $i)
		 send($Reaad)
		 send("{ENTER}")
	  next

		 sleep(2000)
		 MouseClick("LEFT", 481, 169)
		 sleep(1000)
		 Send("{TAB}")
		 sleep(2000)
		 send("{ENTER}")
		 sleep(1000)
		 MouseClick("LEFT", 67, 142)
		 sleep(300)
		 mouseclick("LEFT", 401, 415)
		 sleep(1000)
		 send($day)
		 sleep(500)
		 send("{ENTER}")
		 sleep(1000)
		 send($split[1] & $split[2])
		 sleep(1000)
		 send("{ENTER}")
		 sleep(1000)
		 send($split[1] & $split[2] & ".jpg")
		 sleep(1000)
		 send("{ENTER}")
		 sleep(9000)
		  MouseClick("LEFT", 559, 174)
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 send("{TAB}")
		 sleep(2000)
		 send("{ENTER}")

	  endif
   Next
   If _DateDayOfWeek(@WDAY) <> $day then ExitLoop
   If _IsPressed("1B") then ExitLoop
   Wend


   Else
	 msgbox(0, "", "no")
   Endif
endfunc


func fermer()
   Exit
endfunc