import unittest

def encode(strings):
    encoded = ""
    for s in strings:
        encoded += str(len(s)) + "#" + s
    return encoded

def decode(string):
    result = []

    in_str = False
    count_str = ''
    count = 0
    content_str = ''
    for c in string:
        if in_str:
            content_str += c
            count -= 1
            if count == 0:
                result.append(content_str)
                in_str = False
                content_str = ''
        else:
            if c == '#':
                in_str = True
                count = int(count_str)
                count_str = ''
            else:
                count_str += c
    
    return result



class TestEncode(unittest.TestCase):
    def test_simple(self):
        strings = ['abc','def','ghi']
        assert encode(strings) == '3#abc3#def3#ghi'

    def test_different_lengths(self):
        strings = ['abc','defghi', 'giraffe']
        assert encode(strings) == '3#abc6#defghi7#giraffe'

    def test_empty(self):
        assert encode([]) == ''

    def test_special_chars(self):
        strings = ['a#b','d#e','g#h']
        assert encode(strings) == '3#a#b3#d#e3#g#h'

class TestDecode(unittest.TestCase):
    def test_simple(self):
        strings = ['abc','def','ghi']
        encoded = encode(strings)
        decoded = decode(encoded)

        assert len(decoded) == 3
        assert decoded[0] == 'abc'
        assert decoded[1] == 'def'
        assert decoded[2] == 'ghi'

    def test_different_lengths(self):
        strings = ['abc','defghi', 'giraffe']
        decoded = decode(encode(strings))

        assert len(decoded) == 3
        assert decoded[0] == 'abc'
        assert decoded[1] == 'defghi'
        assert decoded[2] == 'giraffe'

    def test_empty(self):
        assert len(decode(encode([]))) == 0

    def test_special_chars(self):
        strings = ['a#b','d#e','g#fasfdkjh']
        decoded = decode(encode(strings))
        assert len(decoded) == 3
        assert decoded[0] == 'a#b'
        assert decoded[1] == 'd#e'
        assert decoded[2] == 'g#fasfdkjh'


if __name__ == '__main__':
    unittest.main()
