# Introduction to CyberSecurity 
Different Cipher method have been implemented to Encrypt and Decrypt the text  

I have learned and understood few cipher when I was undergoing through cybersecurity course and want to share my experience in implementation of various cipher. I hope you guys would like it and feel free for any suggestion towards improvement of any code.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Atbash-Cipher">Atbash Cipher</a></li>
    <li><a href="#Caesar-cipher">Caesar cipher</a></li>
    <li><a href="#Diffie–Hellman">Diffie–Hellman</a></li>
    <li><a href="#Keyword-Cipher">Keyword Cipher</a></li>
    <li><a href="#Mix-Cipher">Mix Cipher</a></li>
    <li><a href="#RSA">RSA</a></li>
    <li><a href="#Rail-Fence-Cipher">Rail Fence Cipher</a></li>
    <li><a href="#Verman-Cipher">Verman Cipher</a></li>
    <li><a href="#Vigenere-Cipher">Vigenere Cipher</a></li>
  </ol>
</details>

## Atbash Cipher
Atbash  is a simple substitution cipher originally for the Hebrew alphabet, but possible with any known alphabet.
It is considered 'complex'. But, it has a possible key, and it is a simple monoalphabetic substitution cipher. However, this may not have been an issue at the time when the cipher was first devised.
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: ZYXWVUTSRQPONMLKJIHGFEDCBA

## Caesar cipher
a Caesar cipher is also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
E_{n}(x)=(x+n)\mod {26}.

## Diffie–Hellman
Diffie–Hellman key exchange (D–H) is a specific method of securely exchanging cryptographic keys over a public channel and was one of the first protocols as originally conceptualized by Ralph Merkle and named after Whitfield Diffie and Martin Hellman. D–H is one of the earliest practical examples of public key exchange implemented within the field of cryptography
1.	Alice and Bob agree to use a modulus p = 23 and base g = 5 (which is a primitive root modulo 23).
2.	Alice chooses a secret integer a = 6, then sends Bob A = ga mod p
•	A = 56 mod 23 = 8
3.	Bob chooses a secret integer b = 15, then sends Alice B = gb mod p
•	B = 515 mod 23 = 19
4.	Alice computes s = Ba mod p
•	s = 196 mod 23 = 2
5.	Bob computes s = Ab mod p
•	s = 815 mod 23 = 2
6.	Alice and Bob now share a secret (the number 2).
Both Alice and Bob have arrived at the same value s, because, under mod p.


## Keyword Cipher
A keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A,B,C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.
Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Encrypted:   K R Y P T O S A B C D E F G H I J L M N Q U V W X Z

Plaintext:   K N O W L E D G E  I S  P O W E R
Encoded:     D G H V E T P S T  B M  I H V T L

## Mix Cipher
I/P= R  I  T  E S  H

For example Key is +3,-2,+5

O/P= U  G  Y  H  Q  M

E_{n}(x)=(x+n)\mod {26

## RSA
RSA was first described in 1977 by Ron Rivest, Adi Shamir and Leonard Adleman of the Massachusetts Institute of Technology. Public-key cryptography, also known as asymmetric cryptography, uses two different but mathematically linked keys, one public and one private. The public key can be shared with everyone, whereas the private key must be kept secret. In RSA cryptography, both the public and the private keys can encrypt a message; the opposite key from the one used to encrypt a message is used to decrypt it. This attribute is one reason why RSA has become the most widely used asymmetric algorithm: It provides a method of assuring the confidentiality, integrity, authenticity and non-reputability of electronic communications and data storage.

A simple, worked example
Alice generates her RSA keys by selecting two primes: p=11 and q=13. The modulus n=p×q=143. The totient of n ϕ(n)=(p−1)x(q−1)=120. She chooses 7 for her RSA public key e and calculates her RSA private key using the Extended Euclidean Algorithm which gives her 103.

## Rail Fence Cipher
The rail fence cipher (also called a zigzag cipher) is a form of transposition cipher. It derives its name from the way in which it is encoded. 
In the rail fence cipher, the plaintext is written downwards and diagonally on successive "rails" of an imaginary fence, then moving up when we reach the bottom rail. When we reach the top rail, the message is written downwards again until the whole plaintext is written out. The message is then read off in rows. For example, if we have 3 "rails" and a message of 'WE ARE DISCOVERED. FLEE AT ONCE', the cipherer writes out.

PROCEDURE:
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .

WECRL TEERD SOEEF EAOCA IVDEN

## Verman Cipher

As introduction to stream ciphers, and to demonstrate that a perfect cipher does exist, we describe the Vernam Cipher, also known as the one-time-pad.
Gilbert Vernam invented and patented his cipher in 1917 while working at AT&T. The teletype had been recently introduced, and along with this the commerical Baudot code. Now messages were uniformly thought of as streams of zero's and one's (But the word "bit" was not yet invented. This is due to Shannon in the 40's.)
Vernam proposed a bit-wise exclusive or of the message stream with a truely random zero-one stream which was shared by sender and receipient.
   
   SENDING
   
   message: 0 0 1 0 1 1 0 1 0 1 1 1 ...
   
   pad:     1 0 0 1 1 1 0 0 1 0 1 1 ...
   
   XOR      ---------------------------
   
   cipher:  1 0 1 1 0 0 0 1 1 1 0 0 ...

   RECEIVING
   
   cipher:  1 0 1 1 0 0 0 1 1 1 0 0 ...
   
   pad:     1 0 0 1 1 1 0 0 1 0 1 1 ...
   
   XOR      ---------------------------
   
   message: 0 0 1 0 1 1 0 1 0 1 1 1 ...
   
  
  
## Vigenere Cipher
The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form ofpolyalphabetic substitution.
 















