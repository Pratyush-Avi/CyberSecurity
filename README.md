# Introduction to CyberSecurity
Different Cipher method have been implemented to Encrypt and Decrypt the text

I have learned and understood few cipher when I was undergoing through cybersecurity course and want to share my experience in implementation of various cipher. I hope you guys would like it and feel free for any suggestion towards improvement of any code.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Atbash Cipher">Atbash Cipher</a></li>
    <li><a href="#home-screen-and-other-major-screens-snap">Home Screen and other major screens Snap</a></li>
    <li><a href="#function">Function</a></li>
    <li><a href="#license">License</a></li>
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
Both Alice and Bob have arrived at the same value s, because, under mod p,
