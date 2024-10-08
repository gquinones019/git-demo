"""
This type stub file was generated by pyright.
"""

"""
Tools to open .py files as Unicode, using the encoding specified within the file,
as per PEP 263.

Much of the code is taken from the tokenize module in Python 3.2.
"""
cookie_re = ...
cookie_comment_re = ...
def source_to_unicode(txt, errors=..., skip_encoding_cookie=...):
    """Converts a bytes string with python source code to unicode.

    Unicode strings are passed through unchanged. Byte strings are checked
    for the python source file encoding cookie to determine encoding.
    txt can be either a bytes buffer or a string containing the source
    code.
    """
    ...

def strip_encoding_cookie(filelike):
    """Generator to pull lines from a text-mode file, skipping the encoding
    cookie if it is found in the first two lines.
    """
    ...

def read_py_file(filename, skip_encoding_cookie=...):
    """Read a Python file, using the encoding declared inside the file.

    Parameters
    ----------
    filename : str
        The path to the file to read.
    skip_encoding_cookie : bool
        If True (the default), and the encoding declaration is found in the first
        two lines, that line will be excluded from the output.

    Returns
    -------
    A unicode string containing the contents of the file.
    """
    ...

def read_py_url(url, errors=..., skip_encoding_cookie=...):
    """Read a Python file from a URL, using the encoding declared inside the file.

    Parameters
    ----------
    url : str
        The URL from which to fetch the file.
    errors : str
        How to handle decoding errors in the file. Options are the same as for
        bytes.decode(), but here 'replace' is the default.
    skip_encoding_cookie : bool
        If True (the default), and the encoding declaration is found in the first
        two lines, that line will be excluded from the output.

    Returns
    -------
    A unicode string containing the contents of the file.
    """
    ...

