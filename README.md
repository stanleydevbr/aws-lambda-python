## Instruções do curso

Recursos:
* https://pypi.org/project/virtualenv/
* https://pypi.org/project/chalice/
* https://awspolicygen.s3.amazonaws.com/policygen.html
* 


```powershell
    set-executionpolicy remotesigned
```
## Criar virutal env
```powershell
    virtualenv aws-lambda-scheduled
```

## Ativar virtual env
```powershell
    .\aws-lambda-scheduled\Scripts\activate
```
## Instalar chalice
```powershell
    pip install chalice
```
## Criar projeto chalice
```powershell
    chalice new-project aws-lambda-scheduled
```

## Deploy função lambda
```powershell
    chalice deploy
```

## Gerar arquivo requirements.txt
```powershell
    pip freeze > requirements.txt
```

