animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

# Print the index of cat

# cat_index = animals.index('cat')
# print('index of cow is:', cat_index) # This will bring an error as there is no cat


# To handle above error we need to handle the exception error
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No Cats Found'
print(cat_index)
