import re

class RegexText:
    """
    Parses, updates, and deletes text in specific parts of a text file
    """
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        with open(self.path_to_file) as f:
            self.text = f.readlines()
        self.text = "".join(self.text)

    def _get_text(self, span):
        """
        Returns text between two indices
        """
        i0 = span[0]
        i1 = span[1]
        return self.text[i0:i1]

    def _delete_text(self, span):
        """
        Deletes text between two indicies
        """
        i0 = span[0]
        i1 = span[1]
        self.text = self.text[:i0] + self.text[i1:]
        f = open(self.path_to_file, "w")
        f.write(self.text)
        f.close()
    
    def _update_text(self, old_text, new_text, span):
        """
        Applies text update between two indicies
        """
        i0 = span[0]
        i1 = span[1]
        updtd_snip = self.prog[i0:i1].replace(old_text, new_text)
        self.text = self.text[:i0] + updtd_snip + self.text[i1:]
        f = open(self.path_to_file, "w")
        f.write(self.text)
        f.close()

    def get_pattern_at_beginning(self):
        """
        Pattern begins with 'a word' and ends with ')'
        '.*' is any character
        '\' required to escape ')' since it is part of regex syntax
        """
        x = re.search("^a word.*\)", self.text, flags=re.S)  # search across new lines
        return self._get_text(x.span())

    def get_pattern_non_greedy_search(self):
        """
        Pattern begins with 'a word' and ends with '.'
        '.*$\.' means pattern is complete after finding the first '.'
        '$' enables non-greedy search. Without it, the pattern is complete after finding the last '.'
        """
        x = re.search("a word.*;", self.text)
        return self._get_text(x.span())

    def get_list_of_similar_patterns(self):
        list_of_common_patterns = re.finditer("a common word.*;", self.txt, flags=re.S)
        common_pattern_text = ""
        for common_pattern in list_of_common_patterns:
            common_pattern_text += common_pattern + "\n"
        return common_pattern_text



