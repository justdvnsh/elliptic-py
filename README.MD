# Elliptic-py

Fast elliptic-curve cryptography in pure Python implementation. This is a port to elliptic js in python. However, it has the ability to do more than what elliptic js does.

NOTE: Please take a look at http://safecurves.cr.yp.to/ before choosing a curve
for your cryptography operations.

## Incentive

ECC is much slower than regular RSA cryptography, the pythonic implementations are
even slower.

## API

You can read the docs [here](https://justdvnsh.github.io/elliptic-py)

## Supported curves

Following curve 'presets' are embedded into the library:

* `secp256k1`
* `p192`
* `p224`
* `p256`
* `p384`
* `p521`

## Acknowledgements

This project is heavily inspired by the javascript implementation of elliptic . you can find it [here](https://github.com/indutny/elliptic). Also, the naming conventions and references have also been taken from [here](https://github.com/warner/python-ecdsa). The ellitpic curve details can be found [here](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography).