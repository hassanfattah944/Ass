#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_digits(n):
    if n //10 == 0:
        return 1
    else:
        return 1+count_digits(n//10)
    
def find_max(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest
        
        
while True:
    choice=input("Please Enter a choice:")
    if choice == "1":
        n1=int(input("Enter an integer:"))
        result=count_digits(n1)
        print("The number of Digits",n1,"is",result)
    elif choice == "2":
        List_one = list(map(int, input("Enter a list of integers: ").split()))
        max_value = find_max(List_one)
        print("Maximum value:", max_value)
        
    elif choice == "3":
        html = """
        <html>
        <head>
        <title>My Website</title>
        </head>
        <body>
        <h1>Welcome to my website!</h1>
        <p>Here you'll find information about me and my hobbies.</p>
        <h2>Hobbies</h2>
        <ul>
        <li>Playing guitar</li>
        <li>Reading books</li>
        <li>Traveling</li>
        <li>Writing cool h1 tags</li>
        </ul>
        </body>
        </html>
        """
        tag = input("Enter a tag: ")
        count = count_tags(html, tag)
        print("Occurrences of the tag:", count)    

    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.\n")  


# In[ ]:




