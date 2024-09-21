$ErrorActionPreference="Stop"

Write-Host "It's going to use:"
pip -V
Write-Host "Enter Anything To Confirm: " -NoNewline
[Console]::ReadLine()

pip install --upgrade setuptools build twine

Copy-Item -Path "./csfile/__init__.py" -Destination "./csfile/__init__.pyi"
Copy-Item -Path "./csdir/__init__.py" -Destination "./csdir/__init__.pyi"
Remove-Item "./dist" -Recurse
Remove-Item "./csharp_like_file.egg-info" -Recurse

python -m build

Remove-Item "./csfile/__init__.pyi"
Remove-Item "./csdir/__init__.pyi"

twine upload dist/*
