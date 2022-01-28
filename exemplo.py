print('- '*20)
print('Apenas mais um teste\n')

print('Avalie sua experiência: ')
grade = int(input('Nota: '))
if grade >= 8:
    print('\nMuito bom, obrigado!')
elif grade >= 6:
    print('\nShow, mas poderia ser melhor...')
else:
    print('mds, tão ruim assim? :(')