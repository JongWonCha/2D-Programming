; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{127C730F-482B-46AA-BBFE-59FA2E24F7FE}
AppName=FarThrowing_2014182043_Setup
AppVersion=1.5
;AppVerName=FarThrowing_2014182043_Setup 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.example.com/
AppSupportURL=http://www.example.com/
AppUpdatesURL=http://www.example.com/
DefaultDirName={pf}\FarThrowing_2014182043_Setup
DisableProgramGroupPage=yes
OutputDir=C:\Users\JONG\Desktop
OutputBaseFilename=Farthrowing_2014182043_Setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "E:\2dgp\far_throwing\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\2dgp\far_throwing\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\FarThrowing_2014182043_Setup"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\FarThrowing_2014182043_Setup"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,FarThrowing_2014182043_Setup}"; Flags: nowait postinstall skipifsilent

