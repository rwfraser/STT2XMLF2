"""Miscellaneous MED utilities
"""
import inspect

def GenerateImageNumberStrings(batch_size,photos_per):
    print(f'batch_size is {batch_size}, Photos per item: {photos_per}')
    imagenumberstrings = []
    for i in range(1, (batch_size * photos_per) + 1):
        j = str(i)
        if i < 10:
            j = "000" + j
        elif 9 < i < 100:
            j = "00" + j
        else:
            j = "0" + j
        imagenumberstrings.append(j)
    print(f'Created {len(imagenumberstrings)} image strings, Module: {__name__}, Line: {inspect.getframeinfo(inspect.currentframe()).lineno} ')
    return imagenumberstrings
