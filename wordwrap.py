#This code is to align words in line with given width
def word_wrap(para, width):

    if not type(para) is str:
        raise TypeError({type(para)}, "Only string is allowed")

    if not type(width) is int:
        raise TypeError("Only int is allowed")

    if width < 1:
        raise ValueError("Width should be greater than 0")

    try:
        words = para.split()
        maxlenword = max(words, key=len)
        ln = len(maxlenword)
        if ln > width:
            raise ValueError("Width should be greater than word length")

        cline = []
        alinedlines = []

        cwidth = 0
        for word in words:
            if cwidth + len(word) + len(cline) > width:
                alinedlines.append(align_line(cline, width))
                cline = [word]
                cwidth = len(word)
            else:
                cline.append(word)
                cwidth += len(word)
        alinedlines.append(align_line(cline, width))

        return alinedlines

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None


def align_line(words, width):
    try:
        tspace = width - sum(len(word) for word in words)
        if len(words) > 1:
            wordspace = tspace // (len(words) - 1)
            extraspace = tspace % (len(words) - 1)

            alinedline = words[0]
            for i in range(1, len(words)):
                spaces = wordspace + (1 if i <= extraspace else 0)
                alinedline += ' ' * spaces + words[i]
        else:
            # Special case: if there is only one word in the line
            alinedline = words[0].ljust(width)

        return alinedline

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None
