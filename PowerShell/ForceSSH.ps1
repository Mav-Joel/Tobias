Set-ExecutionPolicy Unrestricted
(Get-Command New-PSSession).ParameterSets.Name | Select-String -Pattern "SSH"
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Get-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
Write-Output $(whoami)
$NewPwdText = "Joel"
$NewPwd = $NewPwdText | ConvertTo-SecureString -AsPlainText -Force
Get-LocalUser -Name "admin" | Set-LocalUser -Password $NewPwd