#Regex classes
#"\d" selectes all Digits
# \D non-digit
#\s	One whitespace
#\S	One non-whitespace
#\w	One word character (letters and digits)
#\W	One non-word character( non letters/digits (symbols))
################################################################
#"\d\d" doubling any makes them take words in pair and odd ones in the end of string not taken
# 1234567  > will select 123456 
# 1 2 3 4 56 > will sellect 56 only
#"\d\s" a number that is after it a space
# "\d\s\d" a number that is after it a space and after that space a number
# "." slects all except newlines
# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# -------------