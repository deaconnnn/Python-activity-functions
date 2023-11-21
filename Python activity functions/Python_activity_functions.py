def english(english_total, english_b, english_a):
    eng_test_1 = int(input("\nenter your result for english test 1: "))
    eng_test_2 = int(input("enter your result for english test 2: "))
    final_eng_mark = eng_test_1 + eng_test_2
    print(f"your final english mark is: {final_eng_mark}" + "/240")
    if final_eng_mark <= english_b:
        print("you achieved grade C in english")
    elif final_eng_mark <= english_a:
        print("You achieved grade B in english")
    elif final_eng_mark <= english_total:
        print("You achieved grade A in english")
    return final_eng_mark

def math(math_total, math_b, math_a):
    math_test_1 = int(input("\nenter your result for math test 1: "))
    math_test_2 = int(input("enter your result for math test 2: "))
    math_test_3 = int(input("enter your result for math test 3: "))
    final_math_mark = math_test_1 + math_test_2 + math_test_3
    print(f"your final math mark is: {final_math_mark}" + "/300")
    if final_math_mark <= math_b:
        print("you achieved grade C in math")
    elif final_math_mark <= math_a:
        print("You achieved grade B in math")
    elif final_math_mark <= math_total:
        print("You achieved grade A in math")
    return final_math_mark

def science(science_total, science_b, science_a):
    science_test_1 = int(input("\nenter your result for science test 1: "))
    science_test_2 = int(input("enter your result for science test 2: "))
    science_test_3 = int(input("enter your result for science test 3: "))
    final_science_mark = science_test_1 + science_test_2 + science_test_3
    print(f"your final science mark is: {final_science_mark}" + "/450")
    if final_science_mark <= science_b:
        print("you achieved grade C in science")
    elif final_science_mark <= science_a:
        print("You achieved grade B in science")
    elif final_science_mark <= science_total:
        print("You achieved grade A in science")
    return final_science_mark

english_c = 64 * 2
english_b = 84 * 2
english_a = 104 * 2
english_total = 120 * 2
english_tests = 2

math_c = 56 * 3
math_b = 64 * 3
math_a = 78 * 3
math_total = 100 * 3
math_tests = 3

science_c = 96 * 3
science_b = 113 * 3
science_a = 128 * 3
science_total = 150 * 3
science_tests = 3

#main
final_eng_mark = english(english_c, english_b, english_a)
final_math_mark = math(math_total, math_b, math_a)
final_science_mark = science(science_total, science_b, science_a)
