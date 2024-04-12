$a = Get-Content radical.yaml

$a | ForEach-Object {
    $units = $_ -split '\t'
    $unit = $units[1] -split ' '
    if ($unit.length -eq 1) {
        continue
    }
    if (($unit | select -Unique).length -eq 1){
        $_ >> dz.txt
    }
}