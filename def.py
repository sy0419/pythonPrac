def add_number(n1, n2):
    ret = n1 + n2
    #print(ret)
    return ret


def add_txt(t1, t2):
    print(t1 + t2)

ans = add_number(10, 15)
print(ans)

text1 = 'Republic of Korea~'
text2 = 'Fighting!'
add_txt(text1, text2)

# Function is the set which has purpose and it can make as independently.
# i) declare function with value and reture value.
#   def def_name(v1, v2):
#      code
#      code
#      return result
#  ㄴ call function
#     variable = def_name(value1, value2, ...)
#
# ii) declare function with return value.
#     def def_name():
#       code
#       code
#       return result
#
# iii) declare function without value and return value.
#      def def_name():
#        code
#        code
#        return (or skip)
#  ㄴ call function which does not have return value
#     def_name(value1, value2, ...)
#  ㄴ call function which does not have value and return value
#     def_name()