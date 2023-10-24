$folderPath = "C:\test\qwe"
$encryptionPassword = "1234"

$securePassword = ConvertTo-SecureString $encryptionPassword -AsPlainText -Force
$folder = Get-Item -LiteralPath $folderPath

if (-not $folder.PSIsContainer) {
    Write-Host "Specified path is not a folder."
    exit
}

Enable-BitLocker -MountPoint $folderPath -Password $securePassword
