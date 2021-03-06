#!/bin/bash
# Generate a private key and public key pair

# Pair name (default "blank")
NAME=${1:-blank}

# Key size (default 4096)
SIZE=${2:-4096}

# Key pair destination. Change this to your own home directory
DEST=${3:-/tmp/Keys/}

mkdir "/tmp/Keys/"

# Public/Private key files
PRIK=$DEST$NAME.pem
PUBK=$DEST$NAME.pub

# If either exists, avoid overwrite
if [ -f "$PRIK" ] || [ -f "$PUBK" ]; then
	echo "A key by that name already exists"
	exit 0
fi

# Generate password encrypted private key and plain public key

# This will prompt for a password which will be used to encrypt the 
# private key
openssl genrsa -aes256 -out $PRIK $SIZE &&
openssl rsa -in $PRIK -out $PUBK -pubout

exit

# You'll have to repeat the password when encrypting the key and again 
# to output the public key. DO NOT FORGET THE PASSWORD

# Call this file with : sh genkeys.sh

# For key pair named "keyname"
# sh genkeys.sh keyname

# For 3248 bit keys:
# sh genkeys.sh keyname 3248

# For a keypair saved to /tmp
# sh genkeys.sh keyname 4096 /tmp/

