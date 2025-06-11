; installer.iss - Inno Setup script
[Setup]
AppName=My LLM Assistant
AppVersion=1.0
DefaultDirName={pf}\MyLLMAssistant
DefaultGroupName=My LLM Assistant
OutputDir=D:\Cod\nullm\myproject\installer
OutputBaseFilename=MyLLMAssistantInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "D:\Cod\nullm\myproject\dist\run_desktop\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\My LLM Assistant"; Filename: "{app}\run_desktop.exe"
Name: "{group}\Uninstall My LLM Assistant"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\run_desktop.exe"; Description: "Launch My LLM Assistant"; Flags: nowait postinstall skipifsilent
