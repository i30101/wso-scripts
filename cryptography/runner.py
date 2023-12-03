# Author: Andrew Kim
# version: 3.1.0
# Since: 25 November 2023
# Runner class for Codebusters ciphers


# import ciphers
from columnar import columnar
from columnar import columnar_key
from fractionated import fractionated
from hill import hill
from hill import hill_3
from nihilist import nihilist
from porta import porta




# CALL CIPHERS HERE
nihilist(10, plain="hellothisisatest", auth="andrew")