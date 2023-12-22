#This code is to align words in line with given width
def word_wrap(para, width):

    if not type(para) is str:
        raise TypeError({type(para)}, "Only string is allowed")

    if not type(width) is int:
        raise TypeError("Only int is allowed")

    if width < 1:
        raise TypeError("Width should be greater than 0")

    try:

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None
