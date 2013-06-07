# coding: utf-8
#
# utility
#

import functools
from os import listdir, walk
from os.path import splitext, dirname, abspath, join as path_join
from fnmatch import fnmatch
from inspect import getmembers, isclass
from hashlib import md5
from datetime import datetime


NOW = lambda f="%Y-%m-%d %H:%M:%S %f": datetime.now().strftime(f)


def get_files(path, file_filter):
    return (splitext(n)[0] for n in listdir(path) if file_filter(n))



def get_members(path, member_filter):
    file_filter = lambda f: all((not f.startswith("__"), fnmatch(f, "*.py")))
    modules = []
    
    for f_path, f_dir, files in walk(path):
        for f_name in files:
            if file_filter(f_name):
                m_name = f_name[:f_name.rindex(".")]
                module_name = ".".join((".".join(f_path.split("/")), m_name))
                module = __import__(module_name)
                if "/" in f_path:
                    module = getattr(module, f_path.split("/")[-1])

                b_handlers = getattr(module, m_name)
                members = getmembers(b_handlers)
                for k, v in members:
                    if member_filter(k, v):
                        modules.append((k, v))

    return modules



def get_handlers(view_dir="view"):
    handler_class = __import__("core.web")
    BaseHandler = handler_class.web.BaseHandler
    member_filter = lambda k, v:isclass(v) and issubclass(v, BaseHandler) and hasattr(v, "_my_url")
    return [(v._my_url, v) for k, v in get_members(view_dir, member_filter)]



def url(path):
    def wrap(cls):
        cls._my_url = path
        return cls
    return wrap
