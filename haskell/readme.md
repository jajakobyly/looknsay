looknsay-haskell
================

I have decided to learn (try learning) Haskell, so as a warm-up I wrote the Look-and-Say generator in this language.
It should be much, much more faster than its Python version, although it prints all results when computation ends.

Building / running
------------------

 -  Install [Haskell Platform](http://www.haskell.org/platform/)
 -  `cd` to this directory
 -  Run following command:
    -  To run as script: `runhaskell looknsay.hs`
    -  To compile: `ghc looknsay`

Usage
-----

`looknsay seed [steps=20] [-last]` (**argument order is important**)

Argument | Type      | Required | Default value | Description
---------|-----------|----------|---------------|------------
`seed`   | 1,2,...,9 | **yes**  | -             | Sequence seed (starting number).
`steps`  | number    | no       | 20            | Number of sequence steps.
`-last`  | flag      | no       | no            | Print only last step of the computation.