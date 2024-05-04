# C:\Program Files\Alibre Design 27.0.0.27038\Program
# AlibreAddOn.tlb
# AlibreAddOn_64.tlb
# AlibreX.tlb
# AlibreX_64.tlb
# alibre-api.dll
# AlibreAddOn.dll
# AlibreX.dll
$sourceFolder = "C:\Program Files\Alibre Design 27.0.0.27038\Program"
$destinationFolder = "J:\Testbed-For-Alibre-Design\nuget\27.0.0.27038\libraries"
$filesToCopy = @(
    "AlibreAddOn.tlb",
    "AlibreAddOn_64.tlb",
    "AlibreX.tlb",
    "AlibreX_64.tlb",
    "alibre-api.dll",
    "AlibreAddOn.dll",
    "AlibreX.dll"
)
foreach ($file in $filesToCopy) {
    $sourcePath = Join-Path -Path $sourceFolder -ChildPath $file
    $destinationPath = Join-Path -Path $destinationFolder -ChildPath $file
    if (Test-Path $sourcePath) {
        Copy-Item -Path $sourcePath -Destination $destinationPath -Force
        Write-Host "Copied $file to $destinationPath"
    } else {
        Write-Host "File $file not found in $sourceFolder"
    }
}
