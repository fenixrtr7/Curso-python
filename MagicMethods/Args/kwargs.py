def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='John', age=30, city='New York')
print_info(name='Jane', age=25, country='USA')