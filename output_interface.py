```python
def output_interface(code_block, file_type='txt'):
    if file_type == 'py':
        with open('output.py', 'w') as f:
            f.write(code_block)
    elif file_type == 'txt':
        with open('output.txt', 'w') as f:
            f.write(code_block)
    else:
        print("Invalid file type. Please choose 'py' or 'txt'.")

# Example usage
# output_interface(final_code_block, 'py')
```