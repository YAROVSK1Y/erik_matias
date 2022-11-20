

ten_tests = ['element 1','element 2', 'element 3']
print('Tests with OK- result')

if 'element 1' and 'element 2' in ten_tests:
    print('1 Test -OK')
if 'element 0' and 'element X' not in ten_tests:
    print('2 Test -OK')
if 'element 1' or 'element 2' in ten_tests:
    print('3 Test -OK')
if 'element 5' or 'element 4' not in ten_tests:
    print("4 Test -OK True")
if 'element 2' and 'element 1' in ten_tests:
    print("5 Test -OK")
print("-----------------------------------")
print('Tests with !NOT! OK- result')
print("-----------------------------------")
if 'element X' or 'element 1 'in ten_tests:
    print("6 Test isn't OK. X not in ten_tests ")
if 'element 1' or 'element 2' not in ten_tests:
    print("7 Test isn't OK ")

if 'element 1' or 'element 2' not in ten_tests:
    print("8 Test not OK")
if 'element 4' not in ten_tests:
    print("9 Test isn't OK element 4 not hier")
if 'element 1' and 'element X' or 'element 1' in ten_tests:
    print("10 Sotp!")
