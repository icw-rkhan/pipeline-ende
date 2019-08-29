# pipeline-ende

Open SSL based Encryptor/Decryptor for Jenkins pipeline hook

Better credential management in pipileine based automation trigger. Such as auto applying the DB script or running batch tash with some credentials. 
It dynamically generate a offline-certificate on host system and all encryption/decryption only valid on that host system where pipeline build running.

_(** It is highly recomended to install this application on system where pipleline build will be runing, and all generated encryption will be valid to that host system only)._

* Installation:

    ```./install.sh```


* Uses:
    * Encrypt:
        
        ``./ende.sh --encr <some-credentails>``
        
    * Decrypt:
        
        ``./ende.sh --decr <decrypted-key>``