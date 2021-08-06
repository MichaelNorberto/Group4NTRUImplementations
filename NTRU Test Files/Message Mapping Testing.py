import time
import secrets

emptyString = ""
spaceString = " "

overallTime = 0.0

for i in range(1,101):

    #Getting User Input
    plaintext = '''NTRU: A Ring-Based Public Key Cryptosystem
Jerey Hostein, Jill Pipher, Joseph H. Silverman
Abstract. We describe NTRU, a new public key cryptosystem. NTRU features
reasonably short, easily created keys, high speed, and low memory requirements.
NTRU encryption and decryption use a mixing system suggested by polynomial
algebra combined with a clustering principle based on elementary probability
theory. The security of the NTRU cryptosystem comes from the interaction of
the polynomial mixing system with the independence of reduction modulo two
relatively prime integers p and q.
Contents
0. Introduction
1. Description of the NTRU algorithm
1.1. Notation
1.2. Key Creation
1.3. Encryption
1.4. Decryption
1.5. Why Decryption Works
2. Parameter Selection
2.1. Notation and a norm estimate
2.2. Sample spaces
2.3. A Decryption Criterion
3. Security Analysis
3.1. Brute force attacks
3.2. Meet-in-the-middle attacks
3.3. Multiple transmission attacks
3.4. Lattice based attacks
4. Practical Implementations of NTRU
4.1. Specic Parameter Choices
4.2. Lattice Attacks | Experimental Evidence
5. Additional Topics
5.1. Improving Message Expansion
5.2. Theoretical Operating Specications
5.3. Other Implementation Considerations
5.4. Comparison With Other PKCS's
6. Appendix
x0. Introduction
There has been considerable interest in the creation of ecient and computationally inexpensive public key cryptosystems since Die and Hellman [3] explained how such systems could be created using one-way functions. Currently,
the most widely used public key system is RSA, which was created by Rivest,
Shamir and Adelman in 1978 [9] and is based on the diculty of factoring large
numbers. Other systems include the McEliece system [8] which relies on error
correcting codes, and a recent system of Goldreich, Goldwasser, and Halevi [4]
which is based on the diculty of lattice reduction problems.
In this paper we describe a new public key cryptosystem, which we call the
NTRU system. The encryption procedure uses a mixing system based on polynomial algebra and reduction modulo two numbers p and q, while the decryption
procedure uses an unmixing system whose validity depends on elementary probability theory. The security of the NTRU public key cryptosystem comes from
the interaction of the polynomial mixing system with the independence of reduction modulo p and q. Security also relies on the (experimentally observed)
fact that for most lattices, it is very dicult to nd extremely short (as opposed
to moderately short) vectors.
We mention that the presentation in this paper diers from an earlier, widely
circulated but unpublished, preprint [6] in that the analysis of lattice-based attacks has been expanded and claried, based largely on the numerous comments
received from Don Coppersmith, Johan Hastad, and Adi Shamir in person, via
email, and in the recent article [2]. We would like to take this opportunity to
thank them for their interest and their help.
NTRU ts into the general framework of a probabilistic cryptosystem as described in [1] and [5]. This means that encryption includes a random element,
so each message has many possible encryptions. Encryption and decryption
with NTRU are extremely fast, and key creation is fast and easy. See Section 5
for specics, but we note here that NTRU takes O(N2
) operations to encrypt
or decrypt a message block of length N, making it considerably faster than
the O(N3
) operations required by RSA. Further, NTRU key lengths are O(N),
which compares well with the O(N2
) key lengths required by other \fast" public
keys systems such as [8, 4].
x1. Description of the NTRU algorithm
x1.1. Notation. An NTRU cryptosystem depends on three integer parameters
(N ; p; q) and four sets Lf , Lg , L, Lm of polynomials of degree N  1 with
integer coecients. Note that p and q need not be prime, but we will assume
that gcd(p; q) = 1, and q will always be considerably larger than p. We work in
the ring R = Z[X]=(XN  1). An element F 2 R will be written as a polynomial
or a vector,
F =
N
X1
i=0
Fixi
= [F0; F1; : : : ; FN1]:
We write ~ to denote multiplication in R. This star multiplication is g
explicitly as a cyclic convolution product,
F ~ G = H with Hk = X
k
i=0
FiGki +
N
X1
i=k+1
FiGN+ki = X
i+jk (mod N)
FiGj :
When we do a multiplication modulo (say) q, we mean to reduce the coecients
modulo q.
Remark. In principle, computation of a product F ~ G requires N2 multiplications. However, for a typical product used by NTRU, one of F or G has small
coecients, so the computation of F ~ G is very fast. On the other hand, if N
is taken to be large, then it might be faster to use Fast Fourier Transforms to
compute products F ~ G in O(N log N) operations.
x1.2. Key Creation. To create an NTRU key, Dan randomly chooses 2 polynomials f ; g 2 Lg . The polynomial f must satisfy the additional requirement
that it have inverses modulo q and modulo p. For suitable parameter choices,
this will be true for most choices of f , and the actual computation of these inverses is easy using a modication of the Euclidean algorithm. We will denote
these inverses by Fq and Fp, that is,
Fq ~ f  1 (mod q) and Fp ~ f  1 (mod p): (1)
Dan next computes the quantity
h  Fq ~ g (mod q): (2)
Dan's public key is the polynomial h. Dan's private key is the polynomial f ,
although in practice he will also want to store Fp.
x1.3. Encryption. Suppose that Cathy (the encrypter) wants to send a message to Dan (the decrypter). She begins by selecting a message m from the set
of plaintexts Lm. Next she randomly chooses a polynomial  2 L and uses
Dan's public key h to compute
e  p ~ h + m (mod q):
This is the encrypted message which Cathy transmits to Dan.
x1.4. Decryption. Suppose that Dan has received the message e from Cathy
and wants to decrypt it using his private key f . To do this eciently, Dan should
have precomputed the polynomial Fp described in Section 1.1.
In order to decrypt e, Dan rst computes
a  f ~ e (mod q);
where he chooses the coecients of a in the interval from q=2 to q=2. Now
treating a as a polynomial with integer coecients, Dan recovers the message
by computing
Fp ~ a (mod
Remark. For appropriate parameter values, there is an extremely high probability that the decryption procedure will recover the original message. However, some parameter choices may cause occasional decryption failure, so one
should probably include a few check bits in each message block. The usual
cause of decryption failure will be that the message is improperly centered. In
this case Dan will be able to recover the message by choosing the coecients of
a  f ~ e (mod q) in a slightly dierent interval, for example from q=2 + x to
q=2 + x for some small (positive or negative) value of x. If no value of x works,
then we say that we have gap failure and the message cannot be decrypted as
easily. For well-chosen parameter values, this will occur so rarely that it can be
ignored in practice.
x1.5. Why Decryption Works. The polynomial a that Dan computes satis-
es
a  f ~ e  f ~ p ~ h + f ~ m (mod q)
= f ~ p ~ Fq ~ g + f ~ m (mod q) from (2),
= p ~ g + f ~ m (mod q) from (1).
Consider this last polynomial p ~ g + f ~ m. For appropriate parameter
choices, we can ensure that (almost always) all of its coecients lie between q=2
and q=2, so that it doesn't change if its coecients are reduced modulo q. This
means that when Dan reduces the coecients of f ~ e modulo q into the interval
from q=2 to q=2, he recovers exactly the polynomial
a = p ~ g + f ~ m in Z[X]=(XN
 1).
Reducing a modulo p then gives him the polynomial f ~ m (mod p), and multiplication by Fp retrieves the message m (mod p).
x2. Parameter Selection
x2.1. Notation and a norm estimate. We dene the width of an element
F 2 R to be
jF j1 = max
1iN
fFig  min
1iN
fFig:
As our notation suggests, this is a sort of L1 norm on R. Similarly, we dene a
centered L2
norm on R by
jF j
2 =
X
N
i=1
(Fi  F
)
2
1=2
; where F =
1
N
X
N
i=1
Fi :
(Equivalently, jF j
2 =
p
N is the standard deviation of the coecients of F .) The
following proposition was suggested to us by Don Copper
Proposition. For any " > 0 there are constants 
1; 
2 > 0, depending on "
and N, such that for randomly chosen polynomials F; G 2 R, the probability is
greater than 1  " that they satisfy

1 jF j
2
jGj
2  jF ~ Gj1  
2 jF j
2
jGj
2
:
Of course, this proposition would be useless from a practical veiwpoint if the
ratio 
2=
1 were very large for small "'s. However, it turns out that even for
moderately large values of N and very small values of ", the constants 
1; 
2 are
not at all extreme. We have veried this experimentally for a large number of
parameter values and have an outline of a theoretical proof.
x2.2. Sample spaces. The space of messages Lm consists of all polynomials
modulo p. Assuming p is odd, it is most convenient to take
Lm =

m 2 R : m has coecients lying between
1
2
(p  1) and 1
2
(p  1)
:
To describe the other samples spaces, we will use sets of the form
L(d1; d2) =
n
F 2 R : F has d1 coecients equal 1,
d2 coecients equal 1, the rest 0
o
:
With this notation, we choose three positive integers df ; dg ; d and set
Lf = L(df ; df  1); Lg = L(dg ; dg ); and L = L(d; d):
(The reason we don't set Lf = L(df ; df ) is because we want f to be invertible,
and a polynomial satisfying f (1) = 0 can never be invertible.) Notice that
f 2 Lf , g 2 Lg , and  2 L have L2
norms
jf j
2 =
q
2df  1  N1
; jgj
2 =
p
2dg ; jj
2 =
p
2d:
Later we will give values for df ; dg ; d which allow decryption while maintaining
various security levels.
x2.3. A Decryption Criterion. In order for the decryption process to work,
it is necessary that
jf ~ m + p ~ gj1 < q:
We have found that this will virtually always be true if we choose parameters so
that
jf ~ mj1  q=4 and jp ~ gj1  q=4;
and in view of the above Proposition, this suggests that we take
jf j
2
jmj
2  q=4
2 and jj
2
jgj
2  q=4p
2 (3)
for a 
2 corresponding to a small value for ". For example, experimental evidence
suggests that for N = 107, N = 167, and N = 503, appropriate values for 
2
are 0:35, 0:27, and 0:17 resp
x3. Security Analysis
x3.1. Brute force attacks. An attacker can recover the private key by trying
all possible f 2 Lf and testing if f ~h (mod q) has small entries, or by trying all
g 2 Lg and testing if g~h1
(mod q) has small entries. Similarly, an attacker can
recover a message by trying all possible  2 L and testing if e   ~ h (mod q)
has small entries. In practice, Lg will be smaller than Lf , so key security is
determined by #Lg , and individual message security is determined by #L.
However, as described in the next section, there is a meet-in-the-middle attack
which (assuming sucient storage) cuts the search time by the usual square
root. Hence the security level is given by

Key
Security

=
p
#Lg =
1
dg !
s
N!
(N  2dg )!

Message
Security

=
p
#L =
1
d!
s
N!
(N  2d)! :
x3.2. Meet-in-the-middle attacks. Recall that an encrypted message looks
like e   ~ h + m (mod q). Andrew Odlyzko has pointed out that there is a
meet-in-the-middle attack which can be used against , and we observe that a
similar attack applies also to the private key f . Brie
y, one splits f in half, say
f = f1 + f2, and then one matches f1 ~ e against f2 ~ e, looking for (f1; f2) so
that the corresponding coecients have approximately the same value. Hence
in order to obtain a security level of (say) 280
, one must choose f , g, and  from
sets containing around 2160 elements. (For further details, see [13].)
x3.3. Multiple transmission attacks. If Cathy sends a single message m
several times using the same public key but dierent random 's, then the attacker Betty will be able to recover a large part of the message. Brie
y, suppose
that Cathy transmits ei  i ~h+m (mod q) for i = 1; 2; : : : ; r. Betty can then
compute (ei  e1) ~ h1
(mod q), thereby recovering i  1 (mod q). However,
the coecients of the 's are so small that she recovers exactly i 1, and from
this she will recover many of the coecients of 1. If r is even of moderate size
(say 4 or 5), Betty will recover enough of 1 to be able to test all possibilities for
the remaining coecients by brute force, thereby recovering m. Thus multiple
transmission are not advised without some further scrambling of the underlying message. We do point out that even if Betty decrypts a single message in
this fashion, this information will not assist her in decrypting any subsequent
messages.
x3.4. Lattice based attacks. The ob ject of this section is to give a brief
analysis of the known lattice attacks on both the public key h and the message
m. We begin with a few words concerning lattice reduction. The goal of lattice
reduction is to nd one or more \small" vectors in a given lattice. In theory,
the smallest vector can be found by an exhaustive search, but in practice this is
not possible if the dimension is large. The LLL algorithm of Lenstra-LenstraLovasz [7], with various improvements due to Schnorr and others, [10
will nd relatively small vectors in polynomial time, but even LLL will take a
long time to nd the smallest vector provided that the smallest vector is not
too much smaller than the expected length of the smallest vector. We will make
these observations more precise below.
x3.4.1. Lattice attack on an NTRU private key. Consider the 2N-by-2N matrix composed of four N-by-N blocks:
0
B
B
B
B
B
B
B
B
B
B
B
B
@
 0    0 h0 h1    hN1
0     0 hN1 h0    hN2
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
0 0     h1 h2    h0
0 0    0 q 0    0
0 0    0 0 q    0
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
0 0    0 0 0    q
1
C
C
C
C
C
C
C
C
C
C
C
C
A
(Here  is a parameter to be chosen shortly.) Let L be the lattice generated by
the rows of this matrix. The determinant of L is qN
N
.
Since the public key is h = g ~ f 1
, the lattice L will contain the vector
 = (f ; g), by which we mean the 2N vector consisting of the N coecients of
f multiplied by , followed by the N coecients of g. By the gaussian heuristic,
the expected size of the smallest vector in a random lattice of dimension n and
determinant D lies between
D1=nr
n
2e
and D1=nr
n
e
:
In our case, n = 2N and D = qN
N
, so the expected smallest length is larger
(but not much larger) than
s =
r
N q
e
:
An implementation of a lattice reduction algorithm will have the best chance
of locating  , or another vector whose length is close to  , if the attacker chooses
 to maximize the ratio s= j j
2
. Squaring this ratio, we see that an attacker
should choose  so as to maximize

2
jf j
2
2 + jgj
2
2
=

 jf j
2
2 + 1
jgj
2
2
1
:
This is done by choosing  = jgj
2 = jf j
2. (Note that jgj
2 and jf j
2 are both public
quantities.)
When  is chosen in this way, we dene a constant ch by setting j j
2 = chs.
Thus ch is the ratio of the length of the target vector to the length of the ex
shortest vector. The smaller the value of ch, the easier it will be to nd the target
vector. Substituting in above, we obtain
ch =
s
2e jf j
2
jgj
2
N q :
For a given pair (f ; g) used to set up the cryptosystem, ch may be viewed as a
measure of how far the associated lattice departs from a random lattice. If ch is
close to 1, then L will resemble a random lattice and lattice reduction methods
will have a hard time nding a short vector in general, and nding  in particular.
As ch decreases, lattice reduction algorithms will have an easier time nding  .
Based on the limited evidence we have obtained, the time required appears to
be (at least) exponential in N, with a constant in the exponent proportional to
ch.
x3.4.2. Lattice attack on an NTRU message. A lattice attack may also be
directed against an individual message m. Here the associated lattice problem
is very similar to that for h, and the target vector will have the form (m; ).
As before, the attacker should balance the lattice using  = jj
2 = jmj
2
, which
leads to the value
cm =
s
2e jmj
2
jj
2
N q :
This constant cm gives a measure of the vulnerability of an individual message
to a lattice attack, similar to the way ch does for a lattice attack on h. An
encrypted message is most vulnerable if cm is small, and becomes less so as cm
gets closer to 1.
In order to make the attacks on h and m equally dicult, we want to take
cm  ch, or equivalently, jf j
2 jgj
2  jmj
2 jj
2. For concreteness, we will now
restrict to the case that p = 3; other values may be analyzed similarly. For p = 3,
an average message m will consist of N=3 each of 1, 0 and 1, so jmj
2 
p
2N=3.
Similarly,  consists of d each of 1 and 1, with the rest 0's, so jj
2 =
p
2d. Thus
we will want to set
jf j
2
jgj
2 
p
4N d=3:
This can be combined with the decryption criterion (3) to assist in choosing
parameters.
x3.4.3. Lattice attack on a spurious key. Rather than trying to nd the private key f , an attacker might use the lattice described above (in Section 3.4.1)
and try to nd some other short vector in the lattice, say of the form 
0 =
(f 0
; g0
). If this vector is short enough, then f 0
will act as a decryption key.
More precisely, if it turns out that with high probability,
f
0
~ e  p ~ g
0
+ m ~ f
0
(mod q)
satises jp ~ g
0 + m ~ f
0
j1 < q, then decryption will succeed; and even if this
width is 2q or 3q, it is possible that the message could be recovered via errorcorrecting techniques, especially if several such 
0
's could be found. This ide
which is due to Coppersmith and Shamir, is described in [2]. However experimental evidence suggests that the existence of spurious keys does not pose a
security threat. See Section 4.2 for a further discussion of this point.
x4. Practical Implementations of NTRU
x4.1. Specic Parameter Choices. We will now present three distinct sets
of parameters which yield three dierent levels of security. The norms of f and
g have been chosen so that decryption failure occurs with probability less than
5  105
(based on extensive computer experimentation).
Case A: Moderate Security
The Moderate Security parameters are suitable for situations in which the intrinsic value of any individual message is small, and in which keys will be changed
with reasonable frequency. Examples might include encrypting of television,
pager, and cellular telephone transmissions.
(N ; p; q) = (107; 3; 64)
Lf = L(15; 14); Lg = L(12; 12); L = L(5; 5) (i.e., d = 5).
(In other words, f is chosen with 15 1's and 14 1's, g is chosen with 12 1's and
12 1's, and  is chosen with 5 1's and 5 1's.) These give key sizes
Private Key = 340 bits and Public Key = 642 bits;
and (meet-in-the-middle) security levels
Key Security = 2
50 and Message Security = 2
26:5
:
(We note again that meet-in-the-middle attacks require large amounts of computer storage; for straight search brute force attacks, these security levels should
be squared.) Substituting the above values into the appropriate formulas yields
lattice values
ch = 0:257; cm = 0:258; and s = 0:422q:
Case B: High Security
(N ; p; q) = (167; 3; 128)
Lf = L(61; 60); Lg = L(20; 20); L = L(18; 18) (i.e., d = 18)
Private Key = 530 bits and Public Key = 1169 bits
Key Security = 2
82:9
and Message Security = 2
77:5
ch = 0:236; cm = 0:225; and s = 0:2
Case C: Highest Security
(N ; p; q) = (503; 3; 256)
Lf = L(216; 215); Lg = L(72; 72); L = L(55; 55) (i.e., d = 55)
Private Key = 1595 bits and Public Key = 4024 bits
Key Security = 2
285 and Message Security = 2
170
ch = 0:182; cm = 0:160; and s = 0:0:365q:
x4.2. Lattice Attacks | Experimental Evidence. In this section we describe our preliminary analysis of the security of the NTRU Public Key Cryptosystem from attacks using lattice reduction methods. It is based on experiments which were performed using version 1.7 of Victor Shoup's implementation
of the Schnorr,Euchner and Hoerner improvements of the LLL algorithm, distributed in his NTL package at http://www.cs.wisc.edu/ e shoup/ntl/. The
NTL package was run on a 200 M Hz Pentium Pro with a Linux operating
system.
This algorithm has several parameters that can be adjusted to give varying
types of results. In general the LLL algorithm can be tuned to either nd a
somewhat short point in a small amount of time or a very short point in a
longer time. The key quantity is the constant ch (or cm) described above. It
is somewhat easier to decrypt messages if these constants are small, somewhat
harder if they are close to 1. The idea is to choose a compromise value which
makes decryption easy, while still making it dicult for LLL to work eectively.
The following tables give the time required for LLL to nd either the target
(f ; g) or a closely related vector in the lattice L of 3.4.1 for various choices of
q; ch and dimension N. As will be elaborated on further in the Appendix, the
algorithm seems to nd either a vector of the correct length, or one considerably
too long to be useful for decryption. Even if it were to nd a spurious key
of length somewhat longer than the target, as discussed by Coppersmith and
Shamir in [2], it appears that the time required to nd such a key would not be
signicantly less than that required to nd the true target.
We have chosen parameters so that cm  ch. (So the time required to break
an individual message should be on the same order as the time required to break
the public key). In all cases we found that when N gets suciently large the
algorithm fails to terminate, probably because of accumulated round o errors.
The tables end roughly at this point.
In this version of LLL there are three parameters that can be ne tuned to
optimize an attack. The tables give typical running times to break a key pair for
the most optimal choices of parameters we have found to date. The two columns
give results for two dierent 
oating point versions of the program, QP1 oering
higher precision. We then use this information to extrapolate running times for
larger values of N, assuming the algorithm were to terminate.
FP QP1
Case A
q=64
c=0.26
N time (secs)
75 561
80 1493
85 2832
90 4435
92 7440
94 12908
96 28534
98 129938
N time (secs)
75 1604
80 3406
85 5168
88 11298
90 16102
95 62321
96 80045
98 374034
100 183307
Case B
q=128
c=0.23
N time (secs)
75 600
80 953
85 1127
90 3816
95 13588
N time (secs)
75 3026
80 5452
85 8171
90 20195
95 57087
100 109706
Case C
q=256
c=0.18
N time (secs)
75 547
80 765
85 1651
90 2414
95 2934
100 7471
102 8648
N time (secs)
75 2293
78 3513
81 3453
84 5061
87 6685
90 9753
93 16946
96 19854
99 30014
102 51207
105 75860
108 145834
We will write t(N) for the time in seconds necessary to break a public key corresponding to a parameter N. When we graph log t(N) against N, the examples
we have done seem to indicate that the graph has a positive slope with a small
positive concavity. This would indicate that t(N) grows at least exponentially
with N, and possibly even with N log N. To extrapolate out to higher values
of N, we have taken the information we have and approximated a lower bound
for the slope of log t(N) against N. This gives the following rough estimates for
t(N) in seconds using FP:
t(N) > 12908 exp[(0:396)(N  94)] (Moderate Security)
t(N) > 13588 exp[(0:291)(N  95)] (High Security)
t(N) > 2414 exp[(0:10)(N  92)] (Highest Security)
The running times for QP1 are longer for small N, but yield a better exponential
constant, so for QP1 we obtain:
t(N) > 80045 exp[(0:207)(N  96)] (Moderate Security)
t(N) > 8171 exp[(0:17315)(N  85)] (High Security)
t(N) > 30014 exp[(0:17564)(N  99)] (Highest Security)
These lower bounds yield the following estimates for the time necessary to break
the dierent levels of NTRU security using QP1 running on one 200 MHz Pentium Pro:
Type Level q c N Time (seconds)
QP 1 Moderate 64 0:26 107 780; 230 (9 days)
QP 1 High 128 0:23 167 1:198  1010 (380 years)
QP 1 Highest 256 0:18 503 1:969  1035 (6:2  1027 years)
A more detailed analysis and description of the lattice experiments is given
in the Appendix.
x5. Additional Topics
x5.1. Improving Message Expansion. The NTRU PKCS's for the sample
parameters presented in Section 4.1 have moderate message expansions. However, as the principal use for PKCS's is the exchange of a private key in a single
message block this is not a signicant problem. It may be worth mentioning,
though, that there is a simple way that the NTRU technique can be used to
convey a very long message, with an expansion of only 1-1 after the rst mesage
block.
With this approach, the rst encrypted message e1 that Cathy sends is decrypted as a sequence of 1's, 0's and 1's (taking p = 3) and interpreted as a 1
for the next message block. The next encrypted message block is 1 ~ e1 + m1,
where m1 is the rst block of the actual message. As Dan knows 1, he can
recover m1 mod q exactly. The next encrypted message block Cathy sends is
e2 = 2~e1+m2, where Cathy derived 2 from m1 by squaring m1 and reducing
it mod 3. Dan can now recover 2 as he knows m1, and hence can derive m2
mod q from e2. This can continue for a message of arbitrary length.
x5.2. Theoretical Operating Specications. In this section we consider
the theoretical operating characteristics of the NTRU PKCS. There ar
integer parameters (N ; p; q), four sets Lf ; Lg ; L; Lm determined respectively by
integers df ; dg ; d; p as described in Sections 1.1 and 2.2. The following table
summarizes the NTRU PKCS operating characteristics in terms of these parameters.
Plain Text Block N log2 p bits
Encrypted Text Block N log2 q bits
Encryption Speed O(N2
) operations
Decryption Speed O(N2
) operations
Message Expansion logp q-to-1
Private Key Length 2N log2 p bits
Public Key Length N log2 q bits

Precisely, 4N2
additions and N divisions by q with remainder
x5.3. Other Implementation Considerations. We brie
y mention some
additional factors which should be considered when implementing NTRU.
(1) It is important that gcd(q; p) = 1. Although in principle NTRU will work
without this requirement, in practice having gcd(q; p) > 1 will decrease
security. At the extreme range, if pjq, then the encrypted message e
satises e  m (mod p), so it is completely insecure.
(2) We want most f 's to have inverses modulo p and modulo q, since otherwise it will be hard to create keys. A rst necessary requirement is that
gcd(f (1); pq) = 1, but if this fails for some chosen f , the code creator
can instead use, say, f (X) + 1 or f (X)  1. Assuming gcd(f (1); pq) = 1,
virtually all f 's will have the required inverses if we take N to be a prime
and require that for each prime P dividing p and q, the order of P in
(Z=NZ)

is large, say either N  1 or (N  1)=2. For example, this will
certainly be true if (N  1)=2 is itself prime (i.e., N is a Sophie Germain
prime). Examples of such primes include 107, 167 and 503.
x5.4. Comparison With Other PKCS's. There are currently a number
of public key cryptosystems in the literature, including the system of Rivest,
Shamir, and Adelman (RSA [9]) based on the diculty of factoring, the system of
McEliece [8] based on error correcting codes, and the recent system of Goldreich,
Goldwasser, and Halevi (GGH [4]) based on the diculty of nding short almostorthogonalized bases in a lattice.
The NTRU system has some features in common with McEliece's system,
in that ~-multiplication in the ring R can be formulated as multiplication of
matrices (of a special kind), and then encryption in both systems can be written
as a matrix multiplication E = AX + Y , where A is the public key. A minor
dierence between the two systems is that for an NTRU encryption, Y is the
message and X is a random vector, while the McEliece system reverses these
assignments. But the real dierence is the underlying trap-door which allows
decryption. For the McEliece system, the matrix A is associated to an error
correcting (Goppa) code, and decryption works because the random contribution
is small enough to be \corrected" by the Goppa code. For NTRU, the matr
is a circulant matrix, and decryption depends on the decomposition of A into
a product of two matrices having a special form, together with a lifting from
mod q to mod p.
As far as we can tell, the NTRU system has little in common with the RSA
system. Similarly, although the NTRU system must be set up to prevent lattice
reduction attacks, its underlying decryption method is very dierent from the
GGH system, in which decryption is based on knowledge of short lattice bases.
In this aspect, GGH actually resembles the McEliece system, since in both cases
decryption is performed by recognizing and eliminating a small random contribution. Contrasting this, NTRU eliminates a much larger random contribution
via divisibility (i.e., congruence) considerations.
The following table compares some of the theoretical operating characteristics of the RSA, McEliece, GGH, and NTRU cryptosystems. In each case the
number N represents a natural security/message length parameter.
NTRU RSA McEliece GGH
Encryption Speed(1;2) N2 N2 N2 N2
Decryption Speed(3) N2 N3 N2 N2
Public Key N N N2 N2
Private Key N N N2 N2
Message Expansion(4) varies 1{1 2{1 1{1
(1) NTRU encryption requires only additions and shifts, no other multiplications
(2) RSA encryption is O(N3
) unless small encryption exponents are used.
(3) Asymptotically, NTRU encryption and decryption are O(N log N) using FFT.
(4) For NTRU, see Section 5.1.
We have made some preliminary timing comparisons between NTRU and
RSA, using information available from RSA's web page. The NTRU program
we used was written in C and not optimized for speed.
The main uses to which PKCS's are applied are the exchange of secret keys
and short messages. Also, RSA, ECC and NTRU all work in units of \message
blocks," and any message block in any of these systems is large enough to hold
a secret key of very high security, or a short message. Thus for comparison
purposes, in the following we interpreted a key encryption or decryption in a
PKCS to be the process of encrypting or decrypting one message block. Numbers
given for encryption and decryption are message blocks processed per second.
The information is summarized in the following tables:
Security Encrypt Decrypt Create
Level (blks/sec) (blks/sec) key (sec)
Moderate 1818 505 0:1080
High 649 164 0:1555
Highest 103 19 0:8571
NTRU: 75 MHz Pentium, running MSDOS
Security Encrypt Decrypt Create
Level (blks/sec) (blks/sec) key (sec)
Moderate 16666 2273 0:0079
High 4762 724 0:0184
Highest 730 79 0:1528
NTRU: 200 MHz Pentium Pro, running Linux
Security Encrypt Decrypt Create
Level (blks/sec) (blks/sec) key (sec)
512 bit 370 42 0:45
768 bit 189 15 1:5
1024 bit 116 7 3:8
RSA: 90MHz Pentium
Security Encrypt Decrypt Create
Level (blks/sec) (blks/sec) key (sec)
512 bit 1020 125 0:26
768 bit 588 42 0:59
1024 bit 385 23 1:28
RSA: 255 MHz Digital AlphaStation
Comparing NTRU and RSA on the Pentium 75 and 90 platforms, adjusting
for clock speed, and comparing the moderate NTRU security level to 512 bit RSA
security level, we nd that NTRU is 5.9 times faster at encryption, 14.4 times
faster at decryption and 5.0 times faster at key creation. Similarly comparing
the highest NTRU security level to the 1024 bit RSA security level, NTRU is the
same speed at encryption, 3.2 times faster at decryption, and 5.3 times faster at
key creation.
The 200 MHz Pentium pro and the 256 MHz Digital Alpha are suciently
dierent that there is no obvious way to precisely compare one to the other. But
simply comparing the raw numbers it is interesting to note that in spite of the
slower clock speed, NTRU comes out 16, 18 and 33 times faster at encryption,
decryption and key creation at moderate security, and 2, 3 and 8 times faster at
high security.
For related timings of ECC, we refer to Certicom's published report: \Certicom Releases Security Builder 1.2 Performance Data" According to their report
(available at http://www.certicom.com/secureb.htm), on a Pentium platform
ECC takes 4.57 times as long as RSA to encrypt a message block, and 0.267
times as long to decrypt a message block. Thus compared to RSA, ECC wins by
a factor of about 4 when decrypting, but loses by a factor of 4 when encrypting.
Acknow ledgments. We would like to thank Don Coppersmith, Johan Hastad,
Hendrik Lenstra Jr., Bjorn Poonen, Adi Shamir, Claus Schnorr and Benne de
Weger for their help with lattice reduction methods, Philip Hirschhorn for his
assistance in implementing NTRU and doing LLL testing, Victor Shoup for his
NTL package, Martin Mohlenkamp for several enlightening conversations about
this package, Andrew Odlyzko for pointing out the meet-in-the-middle attack
and other helpful suggestions, Mike Rosen for his help with polynomial inverses,
and Dan Lieman for his assistance in all phases of this pro ject. In particular, our
analysis of lattice-based attacks is an amalgamation of the suggestions of Don
Coppersmith, Johan Hastad, and Adi Shamir, combined with some thoughts of
our own, although we stress that any oversights or errors in this analysis are
entirely of our own devising.
References
1. M. Blum, S. Goldwasser, An ecient probabilistic public-key encryption scheme which
hides al l partial information, Advances in Cryptology: Proceedings of CRYPTO 84, Lecture Notes in Computer Science, vol. 196, Springer-Verlag, 1985, pp. 289{299.
2. D. Coppersmith, A. Shamir, Lattice attacks on NTRU, Preprint, April 5, 1997; presented
at Eurocrypt 97.
3. W. Die, M.E. Hellman, New directions in cryptography, IEEE Trans. on Information
Theory 22 (1976), 644{654.
4. O. Goldreich, S. Goldwasser, S. Halevi, Public-key cryptosystems from lattice reduction
problems, MIT { Laboratory for Computer Science preprint, November 1996.
5. S. Goldwasser and A. Micali, Probabilistic encryption, J. Computer and Systems Science
28 (1984), 270{299.
6. J. Hostein, J. Pipher, J.H. Silverman, NTRU: A new high speed public key cryptosystem,
Preprint; presented at the rump session of Crypto 96.
7. A.K. Lenstra, H.W. Lenstra, L. Lovsz, Factoring polynomials with polynomial coecients,
Math. Annalen 261 (1982), 515{534.
8. R.J. McEliece, A public-key cryptosystem based on algebraic coding theory, JPL Pasadena,
DSN Progress Reports 42{44 (1978), 114{116.
9. R.L. Rivest, A. Shamir, L. Adleman, A method for obtaining digital signatures and public
key cryptosystems, Communications of the ACM 21 (1978), 120{126.
10. C.P. Schnorr, Block reduced lattice bases and successive minima, Combinatorics, Probability and Computing 3 (1994), 507{522.
11. C.P. Schnorr, M. Euchner, Lattice basis reduction: improved practical algorithms and
solving subset sum problems, Mathematical Programing 66 (1994), 181-199.
12. C.P. Schnorr, H.H. Hoerner, Attacking the Chor Rivest cryptosystem by improved lattice
reduction, Proc. EUROCRYPT 1995, Lecture Notes in Computer Science 921, SpringerVerlag, 1995, pp. 1{12.
13. J.H. Silverman, A Meet-In-The-Midd le Attack on an NTRU Private Key, preprint.
x6. Appendix - Some remarks on the impementation
of the Schnorr-Euchner improvements of LLL
The LLL algorithm produces, from a given basis for a lattice, a reduced basis
whose rst vector is guaranteed to be relatively short. Part of this procedure
involves minimizing the length of linear combinations of basis vectors, taking
\blocks" of two at a time. If one minimized the length of linear combinations of
basis vectors, taking as a block the entire basis, then an actual shortest vector
could be found, but the time to produce it would be exponential in the dimension.
One of Schnorr and Euchner's improvements (see [10, 11, 12] was to add an
extra degree of 
exibility. They minimize over blocks of vectors of size greater
than two, but less than the dimension. This results in shorter vectors than are
generally found by the original LLL algorithm, i.e with block size equal 2, but
causes an increase in running time which is exponential in the block size.
In NTL 1.7 the blocksize  can be chosen, as well as a second parameter p
which Schnorr and Hoerner introduced. This is intended to moderate the increase in running time as  increases. The \pruning" parameter p halts the
minimization process when the probability of nding a shorter vector than already found within a given block falls below a prescribed value which depends on
p. This probability is computed via the gaussian volume heuristic, the validity
of which depends on the randomness of the lattice.
There is a third parameter  which is allowed to vary between 0:5 and 1:0.
This parameter determines how frequently a certain recursive operation is performed. The program recommends setting  = :99, and we have followed this
recommendation.
In our experiments we varied the choice of ch and of the blocksize  and
pruning factor p. We never observed, even for larger values of , a noticeable
improvement from the pruning procedure and nally set p = 0, so the pruning
procedure was not called.
The following tables give a more complete set of information which includes
the choice of  and the ratio of the smallest vector found to the target vector.
We observed that for small values of  the algorithm would fail to nd a vector
useful for decryption. In fact it would most likely produce a q-vector, that is to
say a vector with a single coordinate equal to q and the rest all zero. The initial
basis for L contains N of these vectors, which are in fact not much longer than
the length s =
p
N q=e of the shortest expected vector. As  increased, the
smallest vector found would continue to be a q-vector until a certain threshold
was passed, which depended on N and ch. (Increasing with N, decreasing with
ch). After this threshold, if the algorithm terminated it would usually succeed
in nding the target vector. On some occasions it would nd a vector slightly
smaller than a q-vector and then at the next blocksize succeed in nding the
target. The general pattern is that for xed ch the blocksize would have to
increase with N in order for the algorithm to succeed in nding the target. At
slightly smaller blocksizes the time required would be on the same order as the
time required to nd the target but the vector found | either the q-vector or
slightly smaller | would be useless for decryption purposes.
In Table 1 timings are given for a lattice corresponding to ch = 0:26 with
jf j
2 = jgj
2
. This is the equivalent to the moderate security lattice attack, but
the balancing of f and g makes it possible to work with smaller integers and
the NTL program runs, with some exceptions, more eciently. Notice that
the necessary blocksize increases monotonically with N. In the Tables 2, 3
and 4, timings are given for moderate, high and highest security. These are
again formed with jf j
2 = jgj
2, and the moderate security table is a repeat to
give some idea of the variation that occurs. Finally, Table 5 is formed with
jf j
2 and jgj
2
taking the same ratio as in the actual encryption procedure. The
 = 0:9097 indicates that the lattice has been balanced to optimize the chances of
an attacker. Note that the times are roughly the same as the equivalent situation
in Tables 1 and 2, but timing deteriorates very substantially at N = 98. Notice
some curiously short timings at N = 90 in Tables 2 and 5. These occurred when
the algorithm terminated after locating a particular short vector: (f 0
; f 0 ~ h),
with f
0 = (1; 1; 1; 1; 1; : : : ). The value of f
0 ~ h is then (k; k; k; : : : ), for
some k, with k taking the value 1 or 1 with probability 2=q. If this happens,
(f 0
; f 0 ~ h) is short, but as f 0
is highly non-invertible it is useless for decryption
purpo
N Block Running Actual Smallest Ratio of
size time (sec) Total Norm found to
Norm Found actual
75 6 1910 6:32 6:32 1:0
80 4 1823 6:48 64:00 9:9
80 6 2731 6:78 64:00 9:4
80 8 3285 6:48 64:00 9:9
80 10 3663 6:63 6:63 1:0
85 4 2091 6:93 64:00 9:2
85 6 3661 6:78 64:00 9:4
85 8 5012 6:93 64:00 9:2
85 10 5497 6:78 64:00 9:4
85 12 7438 6:93 64:00 9:2
85 14 7433 7:07 7:07 1:0
90 4 3382 6:93 64:00 9:2
90 6 3305 6:78 64:00 9:4
90 8 5910 6:78 64:00 9:4
90 10 7173 6:78 64:00 9:4
90 12 7367 6:78 64:00 9:4
90 14 12182 6:93 64:00 9:2
90 16 16102 6:78 6:78 1:0
90 18 18920 6:93 6:93 1:0
95 4 3019 7:21 64:00 8:9
95 6 4434 7:07 64:00 9:1
95 8 7707 7:07 64:00 9:1
95 10 9449 7:35 64:00 8:7
95 12 11308 7:21 64:00 8:9
95 14 14520 7:21 64:00 8:9
95 16 22348 7:07 64:00 9:1
95 18 23965 7:21 64:00 8:9
95 20 81028 7:07 64:00 9:1
95 22 62321 7:35 7:35 1:0
100 4 4020 7:21 64:00 8:9
100 6 6307 7:07 64:00 9:1
100 8 9225 7:07 64:00 9:1
100 10 11109 7:07 64:00 9:1
100 12 13381 7:07 64:00 9:1
100 14 19096 7:21 64:00 8:9
100 16 23850 7:07 64:00 9:1
100 18 40670 7:21 50:99 7:1
100 20 72130 7:21 64:00 8:9
100 22 444773 7:21 7:21 1:0
Table 1: BKZ-QP1 with Q = 64, c = 0:26,  = 0:99, and prune = 0
N Block Running Actual Smallest Ratio of
size time (sec) Total Norm found to
Norm Found actual
75 4 1797 6:16 64:00 10:4
75 6 1604 6:48 6:48 1:0
80 6 2776 6:78 64:00 9:4
80 8 3406 6:63 6:63 1:0
85 8 4614 6:93 64:00 9:2
85 10 5898 6:78 64:00 9:4
85 12 7536 6:93 64:00 9:2
85 14 8106 7:21 64:00 8:9
85 16 5168 6:78 6:78 1:0
88 16 11298 6:93 6:93 1:0
90 16 12987 6:93 64:00 9:2
90 18 2 6:78 13:42 2:0
95 18 25908 7:21 64:00 8:9
95 19 36754 7:21 64:00 8:9
95 20 59664 7:21 64:00 8:9
96 20 80045 7:07 7:07 1:0
98 20 75365 7:21 64:00 8:9
98 22 374034 7:07 7:07 1:0
100 22 183307 7:07 7:07 1:0
Table 2: BKZ-QP1 with Q = 64, c = 0:26,  = 0:99, and prune = 0
N Block Running Actual Smallest Ratio of
size time (sec) Total Norm found to
Norm Found actual
75 2 1067 8:00 128:00 16:0
75 4 2699 8:00 121:90 15:2
75 6 3244 8:12 121:04 14:9
75 8 3026 7:87 7:87 1:0
80 8 6022 8:37 124:54 14:9
80 10 5452 8:12 8:12 1:0
85 10 10689 8:37 124:26 14:9
85 12 8171 8:37 8:37 1:0
90 12 15304 8:60 128:00 14:9
90 14 17802 8:83 126:60 14:3
90 16 20195 8:60 8:60 1:0
95 16 31338 9:17 128:00 14:0
95 18 54490 8:94 128:00 14:3
95 20 57087 8:83 8:83 1:0
100 20 109706 9:17 9:17 1:0
Table 3: BKZ-QP1 with Q = 128, c = 0:23,  = 0:99, and prune = 0
N Block Running Actual Smallest Ratio of
size time (sec) Total Norm found to
Norm Found actual
75 4 2293 8:60 8:60 1:0
75 20 1930 8:72 8:72 1:0
78 4 3513 8:94 12:25 1:4
81 4 3422 9:38 221:22 23:6
81 6 3453 9:17 9:17 1:0
84 6 5061 9:17 9:17 1:0
87 6 6685 9:38 9:38 1:0
90 6 7085 9:49 256:00 27:0
90 8 9753 9:59 9:59 1:0
93 8 11900 9:90 254:55 25:7
93 10 14671 9:80 237:58 24:2
93 12 16946 9:70 9:70 1:0
96 12 22684 9:80 231:59 23:6
96 14 19854 9:90 9:90 1:0
99 14 30014 10:00 10:00 1:0
102 14 30817 10:20 239:62 23:5
102 16 64718 10:39 223:64 21:5
102 18 51207 10:39 10:39 1:0
105 18 81336 10:58 244:38 23:1
105 20 75860 10:30 10:30 1:0
108 20 197697 10:30 255:87 24:9
108 22 145834 10:30 10:30 1:0
Table 4: BKZ-QP1 with Q = 256, c = 0:18,  = 0:99, and prune = 0
N Block Running Actual Smallest Ratio of
size time (sec) Total Norm found to
Norm Found actual
75 2 808 6000:00 64000:0 10:7
75 4 1895 6000:00 64000:0 10:7
75 6 2363 6000:00 7857:87 1:3
80 6 3582 6164:41 6164:78 1:0
85 6 5412 6324:56 64000:0 10:1
85 8 7252 6324:56 64000:0 10:1
85 10 8633 6324:56 64000:0 10:1
85 12 10074 6324:56 64000:0 10:1
85 14 12371 6324:56 64000:0 10:1
85 16 17729 6324:56 64000:0 10:1
85 18 16095 6324:56 6630:40 1:0
90 18 4 6480:74 12820:5 2:0
95 18 37998 6633:25 64000:0 9:6
95 20 43108 6633:25 64000:0 9:6
95 22 200195 6633:25 6900:34 1:0
96 22 240563 6633:25 64000:0 9:6
96 24 68054 6633:25 6779:54 1:0
98 24 1369730 6782:33 6852:89 1:0
Table 5: BKZ-QP1 with Q = 64, c = 0:26,
 = 0:9097,  = 0:99, and prune = 0
Jerey Hostein, Mathematics Department, Box 1917, Brown University, Providence, RI 02912 USA. hjho@ntru.comi, hjho@math.brown.edui
Jill Pipher, Mathematics Department, Box 1917, Brown University, Providence,
RI 02912 USA. hjpipher@ntru.comi, hjpipher@math.brown.edui
Joseph H. Silverman, Mathematics Department, Box 1917, Brown University,
Providence, RI 02912 USA. hjhs@ntru.comi, hjhs@math.brown.edui'''
    #Initalizing Timing
    t0 = time.time()

    print("The Message is: ", plaintext, "\n")
    #ASCII Conversion
    asciiString = []
    for character in plaintext:
        asciiString.append((ord(character)))
        
    #Binary Conversion
    binString = []
    for integer in asciiString:
        binString.append(bin(integer).replace("0b", ""))
    ###########################################################################
    #Printing Output 
    binaryStr = []
    testStr = emptyString.join(binString)
    binaryStr.append(int(emptyString.join(binString)))
    print("The binary is: ", spaceString.join(binString))
    print("The length of the binary is: ", len(emptyString.join(binString)))


    mutatedList = []
    mutationRate = 0.325
    binaryStr = list(map(int, str(binaryStr[0])))
    for integer in binaryStr:
        if secrets.SystemRandom().uniform(0.0000,1.0000) < mutationRate:
            integer = integer - (integer * 2)
            mutatedList.append(integer)
        else:
            mutatedList.append(integer)
    t1 = time.time()
    total  = t1 - t0
    overallTime = overallTime + total
    average = overallTime / i
    print(mutatedList)
    print ("The total time to convert the message was: ", total, "s")
    print("The average mapping time was: ", average, "s")



