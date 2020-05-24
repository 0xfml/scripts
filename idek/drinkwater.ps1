Add-Type -AssemblyName System.Windows.Forms
$global:balmsg = New-Object System.Windows.Forms.NotifyIcon
while ($true) 
{
$path = (Get-Process -id $pid).Path
$balmsg.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon($path)
$balmsg.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Warning
$balmsg.BalloonTipText = ‘Drink some water idiot'
#$balmsg.BalloonTipTitle = "oi! $Env:USERNAME"
$balmsg.BalloonTipTitle = "oi!"
$balmsg.Visible = $true
$balmsg.ShowBalloonTip(10000)

Start-Sleep -seconds 900 # alert ever 15 mins
}
