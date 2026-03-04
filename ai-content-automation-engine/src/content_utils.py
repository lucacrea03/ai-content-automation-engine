"""
Content Processing Utilities
Functions for trimming and formatting article content
"""


def trim(information):
    """
    Trim the information and assign variables to Title and Content
    
    Args:
        information: List containing title and content
        
    Returns:
        tuple: (title, content)
    """
    p = "Related video:"
    title = information[0]
    c = [info.replace(p, "") for info in information[1:]]
    content = c[0]
    
    print("*"*8, "Trimming post and assigning variables to title and content", "*"*8)
    print("-"*100)

    return title, content
