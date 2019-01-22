#!/usr/bin/python

################################################################################################################################################################
#
#Switch Number Calculator v.01
#
#This tool is used to calculate the number of switches given the number of RJ 45 modules, switch-port number, and allowance
#
################################################################################################################################################################
# Note: This license has also been called the "New BSD License" or "Modified BSD License". See also the 2-clause BSD License.
#
# Copyright 2019 City of Whitehorse Business and Technology Systems (BTS)
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; # OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# -------------------------------------------------- Changelog --------------------------------------------------
#
# 02-Jan 2019: Created base code with basic calculations and program flow control.
#              Program still require input verification and automatic (x) variable calculation
#              Varaibles need to be updated to camel case.
#
# 03-Jan 2019: Removed "b" input an replaced with b = x * 0.2 for the 20% allowance. Left input statement for future changes.
#
################################################################################################################################################################


#Py Modules
import math
import time

# Introduction

print ("Switch Port Calculator v. 01")
print ("")
print ("Copyright © 2019")
print ("City of Whitehorse Business and Technology Systems (BTS)")
print ("All rights reserved.")
print ("")
#print ("Where:")
print ("")
#print ("a = number of RJ 45 modules")
#print ("b = 20% of ports in an x-port switch")
#print ("x = number of usable ports in a switch")
print ("")

# While loop

while True:

# Define variables for input value

     a = float (input ("Enter the total number of RJ 45 ports: "))
#    b = float (input ("Enter b: "))
     x = float (input ("Enter the switch port number: "))


#Operations
     b = x * 0.2
     
     z = (a / x) + (((a / x ) * b)/ x)

#Print Output. Round off to the nearest whole number.

     print ("Total number of switches:" , round(z))

# User Prompt to continue or terminate
     time.sleep(1)
     print ("")
     res  = str(input(" Would you like to continue?[y/n]: "))
     print ("")

#Condition statement
     if res.strip() == 'N' or res == 'n':
         break
