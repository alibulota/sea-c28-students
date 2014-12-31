# -*- coding: utf-8 -*-


def p_wrapper(func):
    def return_a_string(*args, **kwargs):
        tag = (u'<p>', '</p>')
        return tag[0] + func(*args, **kwargs) + tag[1]
    return return_a_string
