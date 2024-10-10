## Command : 

#### Dissamble apk or build 

```
apktool d <fichier>
apktool b <fichier> -o output.apk
```

#### Outils code et reverse

```
jd-gui <fichier jar> &
ghidra &
```

#### Convertir .apk to .jar

```
d2j-dex2jar.sh -d <fichier>
```

#### Futur outils importants

```
Frida
```

#### Aide

Apktool pour rebuild dl la latest version !
```
sudo nano /usr/local/bin/apktool2
#!/bin/bash
java -jar /workspace/apktool2.jar "$@"
```

```
chmod +x /usr/local/bin/apktool2
```

Voir installer Docker sinon kali ! 
Installer Android Studio (Emulateur) : https://www.youtube.com/watch?v=MCviSJz-fyY
