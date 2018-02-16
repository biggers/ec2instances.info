import urllib


def to_bytes(bytes_or_str):
    """ from "Effective Python"
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode()  # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value  # instance-of bytes


def to_str(bytes_or_str):
    """ from "Effective Python"
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode()  # uses 'utf-8' for encoding
    else:
        value = bytes_or_str
    return value  # instance-of str


def get_openurl(a_url):
    rbytes = urllib.request.urlopen(a_url)
    opurl = to_str(rbytes)
    return opurl
