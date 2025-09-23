p_v = int(input())
v_v = int(input())
t_v = int(input())
v_all = [('Петя', p_v), ('Вася', v_v), ('Толя', t_v)]
winners = sorted(v_all, key=lambda win: win[1], reverse=True)
# print(winners)
names = [win[0] for win in winners]
# print(names)
print(f'{names[0]:^24}')
print(f'  {names[1]:<22}')
print(f'{names[2]:>22}')
print('   II      I      III   ')