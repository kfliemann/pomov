<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/kfliemann/pomov/assets/39403385/bd9f84d4-cbca-4f4a-9ad3-f4d08ecc3aec">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/kfliemann/pomov/assets/39403385/1cbd415d-da02-429a-af9a-0fc274261ba0">
  <img alt="Shows the word Pomov with a tomato for the first o" src="https://github.com/kfliemann/pomov/assets/39403385/1cbd415d-da02-429a-af9a-0fc274261ba0">
</picture>
<div align="center">

# Pomov
<b>Pomodoro meets Movement</b> - A Pomodoro inspired timer to notify you, when it's time to move your body.
</div>
        
## 🍅 What is Pomov? 
Have you ever been so absorbed in a project that time flew by and you suddenly realized you haven't moved in hours? If only there was an App to remind you to get up and move periodically to prevent health issues.<br><br>
Look no further!<br><br>
**Pomov** is your little helper that ensures you don't forget to take breaks and stay active.<br>
With the ability to start on Windows Boot, you don't have to worry about forgetting to set the Timer. The App and the Timer will by default automatically start!<br><br>
When the timer runs out, <b>Pomov</b> sends a Windows Notification featuring a GIF animation of a simple exercise you can do during your break.<br><br>
**Stay healthy and keep moving with Pomov!**

## ⭐ Features
* Timer / Break functionality with customizable times
* Autostart App on Windows Boot / Autostart Timer on App start
* Autorestart Timer after Break
* Windows Notifications containing a little exercise animation, which you can perform during break
* Preview Alarm sounds and choose your favorite.
* Choose to minimize to Taskbar or to System Tray, if you want the App to run in the background

## 💻 Interface  
![layout](https://github.com/user-attachments/assets/8ba325e3-3f06-40b0-9cc2-f2d150ace9a0)


## 💬 FAQ
**Why is the Timer limited to 120 minutes and the Break limited to 20 minutes?**
- I believe both the time you are working for and the break you are taking should be realistic. Setting the Timer to 8 hours and the Break to 6 hours would defeat the whole purpose of this App. So i restricted us to much more reasonable durations.

**There is a list of default sound files. How do i set my own custom alarm sound?**
- Short answer: you can't. Long answer: Windows Toasts cannot read custom files from an [absolute path](https://github.com/MicrosoftDocs/windows-dev-docs/issues/1593#issuecomment-483412701). While there is a way to do this in a C# project, the effort required to implement a custom workaround in Python just for a custom audio file does not justify the result. I tried for an entire day because I was stubborn and thought there had to be a way, but no, there isn't (at least not an easy one). Sorry!

**I changed the volume setting of the alarm sound, but when the Notification sound plays, it is louder / quieter than what I set it to. Why?**
- The volume slider is for sound preview only. The actual volume of the Windows Notification is tied to your system's current volume setting.

**Can i add new gif animations, i am tired of the current ones.**
- Yes you can! Just add the .gif files into the \media\img\movement_gif folder and the app will pick an animation at random.

**Which operating systems are supported?**
- Since i am using the library win11toast i am focusing on Windows. The App is tested using Win10, i hope Win11 is working aswell. Currently no support for Mac / Linux. I don't know what happens, if you run the App on those systems.

**Why do i have to create a shortcut myself and why does the app not create one itself?**
- I found out when trying to release v1.0 that automatically creating shortcuts in the autostart folder is apparently something malware often does and my app got flagged as "Trojan:Script/Wacatac.H!ml" because of that (whoops, lol!). 

**My Question is not listed here, what do i do?**
- No problem! You can open up a new issue containing your question and i will help you out! 😊

## 🙏 Credits
This project was made using:<br>
- PyQt6
- [zhiyiYo](https://github.com/zhiyiYo)'s [PyQt-Frameless-Window](https://github.com/zhiyiYo/PyQt-Frameless-Window)
- [zhiyiYo](https://github.com/zhiyiYo)'s [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)
- [GitHub30](https://github.com/GitHub30)'s [win11toast](https://github.com/GitHub30/win11toast)
- [pygame](https://github.com/pygame)'s [pygame](https://github.com/pygame/pygame)

## 💖 Thanks
Thank you for using the App.<br>
If you find any bugs / have feature request, please feel free to open an issue and i will look into it!
<br><br><br>
ironically, i spent a lot of time sitting around to complete this project, so this app was much needed for me 😁
