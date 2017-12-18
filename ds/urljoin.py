def url_path_join(*args, trailing_slash=False):
    url = '/'.join(map(lambda x: x.strip().strip('/'), args))
    if trailing_slash:
        return url + "/"
    return url
